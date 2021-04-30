__author__ = "jnhasard & pnheinsohn"

import threading as th
import socket
import json
from csv import DictReader
from os import urandom
import hashlib

HOST = "localhost"
PORT = 12921

class Servidor:

    def __init__(self):

        self.host = HOST
        self.port = PORT
        self.master = False
        self.colores = {"blue": 0, "pink":0, "yellow":0, "red":0, "purple":0}

        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen(5)
        print(f"Servidor escuchando en {self.host}:{self.port}...")

        thread = th.Thread(target=self.aceptar_conexiones_thread, daemon=True)
        thread.start()
        self.sockets = {}
        self.check_master = {}
        print("Servidor aceptando conexiones...")


    def aceptar_conexiones_thread(self):
        '''
        Este método es utilizado en el thread para ir aceptando conexiones de
        manera asíncrona al programa principal
        :return:
        '''

        while True:
            client_socket, _ = self.socket_servidor.accept()
            self.sockets[client_socket] = None
            print("Servidor conectado a un nuevo cliente...")

            listening_client_thread = th.Thread(
                target=self.escuchar_cliente_thread,
                args=(client_socket,),
                daemon=True)
            listening_client_thread.start()

            if len(self.sockets) == 5:
                break

    def escuchar_cliente_thread(self, client_socket):
        '''
        Este método va a ser usado múltiples veces en threads pero cada vez con
        sockets de clientes distintos.
        :param client_socket: objeto socket correspondiente a algún cliente
        :return:
        '''

        while True:
            try:
                # Primero recibimos los 4 bytes del largo
                response_bytes_length = client_socket.recv(4)

                # Los decodificamos
                response_length = int.from_bytes(response_bytes_length,
                                                 byteorder="big")

                # Luego, creamos un bytearray vacío para juntar el mensaje
                response = bytearray()

                # Recibimos datos hasta que alcancemos la totalidad de los datos
                # indicados en los primeros 4 bytes recibidos.
                while len(response) < response_length:
                    response += client_socket.recv(256)

                # Una vez que tenemos todos los bytes, entonces ahí decodificamos
                # Una vez que tenemos todos los bytes, entonces ahí decodificamos

                if len(response) > 0:
                    response = response.decode()
                    response = json.loads(response)
                    self.manejar_comando(response, client_socket)

                    # Luego, debemos cargar lo anterior utilizando json
                    # decoded = json.loads(response)
                    # Para evitar hacer muy largo este método, el manejo del
                    # mensaje se
                    # realizará en otro método

            except ConnectionResetError:
                decoded_message = {"status": "cerrar_sesion"}
                self.manejar_comando(decoded_message, client_socket)
                break

    def manejar_comando(self, recibido, client_socket):
        '''
        Este método toma lo recibido por el cliente correspondiente al socket pasado
        como argumento.
        :param recibido: diccionario de la forma: {"status": tipo, "data": información}
        :param client_socket: socket correspondiente al cliente que envió el mensaje
        :return:
        '''

        # Podemos imprimir para verificar que toodo anda bien
        print("Mensaje Recibido: {}".format(recibido))
        print(type(recibido))

        if recibido['status'] == "mensaje":
            msj = {"status": "mensaje",
                   "data": {"usuario": self.sockets[client_socket],
                            "contenido": recibido["data"]["contenido"]}}
            for skt in self.sockets.keys():
                self.send(msj, skt)

        elif recibido['status'] == 'nuevo_usuario':
            count = 0
            with open("usuarios.csv", "r") as file:
                file_ = DictReader(file)
                for i in file_:
                    if list(i.values())[0] == str(recibido["nombre_usuario"]):
                        count = 1
                        break

            if count == 1:
                self.send({"status": "existe"}, client_socket)

            else:

                with open("usuarios.csv", "a") as file:
                    file.write("\n" + recibido["nombre_usuario"] + ","
                    + recibido["clave"] + "," + recibido["la_salt"])

                color = "yellow"
                for i in self.colores:
                    if self.colores[i] == 0:
                        color = i
                        self.colores[i] = 1
                        break

                if self.master == False:
                    self.send({"status": "no existe", "color": color,
                               "master": "Si"},
                              client_socket)
                    self.master = True
                    self.check_master[client_socket]= True

                else:
                    self.send({"status": "no existe", "color": color,
                               "master":"No"},
                          client_socket)
                    self.check_master[client_socket] = False

            # self.sockets[client_socket] = recibido["data"]

        elif recibido['status'] == "usuario_antiguo":
            password = ""
            la_salt = ""

            with open("usuarios.csv", "r") as file:
                file_ = DictReader(file)
                for i in file_:
                    if list(i.values())[0] == recibido["nombre"]:
                        count = 1
                        password = list(i.values())[1]
                        la_salt = list(i.values())[2]

            hashing = hashlib.sha256()
            clave = bytes(str(recibido["clave"]), 'utf-8')
            hashing.update((str(clave) + str(la_salt)).encode("utf-8"))

            print(clave, hashing.hexdigest())

            if hashing.hexdigest() == password:

                color = "yellow"
                for i in self.colores:
                    if self.colores[i] == 0:
                        color = i
                        self.colores[i] = 1
                        break

                if self.master == False:
                    self.send({"status": "acceso", "color": color,
                               "master": "Si", "name": recibido["nombre"]},
                              client_socket)
                    self.master = True
                    self.check_master[client_socket] = True

                else:
                    self.send({"status": "acceso", "color" : color,
                               "name":recibido["nombre"], "master": "No"},
                              client_socket)
                    self.check_master[client_socket] = False
            else:
                self.send({"status": "sin acceso"}, client_socket)

        elif recibido['status'] == "cerrar sesion":
            if self.check_master[client_socket]:
                self.master= False
            del self.sockets[client_socket]
            del self.check_master[client_socket]
            self.send({"status": "cerrar"}, client_socket)

        elif recibido["status"] == "iniciar":
            for i in self.sockets.keys():
                self.send({"status": "iniciar"}, i)

        elif recibido["status"] == "draw":
            for i in self.sockets.keys():
                self.send(recibido, i)


    @staticmethod
    def send(valor, socket):
        '''
        Este método envía la información al cliente correspondiente al socket.
        :param msg: diccionario del tipo {"status": tipo del mensaje, "data": información}
        :param socket: socket del cliente al cual se le enviará el mensaje
        :return:
        '''

        # Le hacemos json.dumps y luego lo transformamos a bytes
        msg_json = json.dumps(valor)
        msg_bytes = msg_json.encode()

        # Luego tomamos el largo de los bytes y creamos 4 bytes de esto
        msg_length = len(msg_bytes).to_bytes(4, byteorder="big")

        # Finalmente, los enviamos al servidor
        socket.send(msg_length + msg_bytes)

if __name__ == "__main__":

    server = Servidor()
    # Mantenemos al server corriendo
    while True:
        pass
