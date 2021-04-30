__author__ = "jnhasard & pnheinsohn"

import sys
import threading as th
import socket
import json
from frontend import *
from PyQt5.QtWidgets import QApplication
from datetime import datetime

HOST = "localhost"
PORT = 12921

class Cliente:
    '''
    Esta es la clase encargada de conectarse con el servidor e intercambiar información
    '''

    def __init__(self):
        print("Inicializando cliente...")
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = HOST
        self.port = PORT
        self.color = ""
        self.frontend = MainWindow(self)
        self.frontend.show()
        self.master = False
        self.name = ""

        try:
            self.socket_cliente.connect((self.host, self.port))
            print("Cliente conectado exitosamente al servidor")

            self.conectado = True

            escuchar_servidor = th.Thread(target=self.escuchar, daemon=True)
            escuchar_servidor.start()
            print("Escuchando al servidor...")

        except ConnectionRefusedError:
            self.socket_cliente.close()
            self.terminar_conexion()

    def escuchar(self):
        '''
        Este método es usado en el thread y la idea es que reciba lo que
        envía el servidor. Implementa el protocolo de agregar los primeros
        4 bytes, que indican el largo del mensaje
        '''

        while self.conectado:
            try:
                # Recibimos los 4 bytes del largo
                tamano_mensaje_bytes = self.socket_cliente.recv(4)
                tamano_mensaje = int.from_bytes(tamano_mensaje_bytes,
                                                byteorder="big")

                contenido_mensaje_bytes = bytearray()

                # Recibimos el resto de los datos
                while len(contenido_mensaje_bytes) < tamano_mensaje:
                    contenido_mensaje_bytes += self.socket_cliente.recv(256)

                # Decodificamos y pasamos a JSON el mensaje
                contenido_mensaje = contenido_mensaje_bytes.decode("utf-8")
                mensaje_decodificado = json.loads(contenido_mensaje)

                # Manejamos el mensaje
                self.manejar_comando(mensaje_decodificado)

            except ConnectionResetError:
                self.terminar_conexion()


    def manejar_comando(self, diccionario):
        '''
        Este método toma el mensaje decodificado de la forma:
        {"status": tipo del mensaje, "data": información}
        '''

        print(f"Mensaje recibido: {diccionario}")
        print(diccionario)

        if diccionario["status"] == "mensaje":
            data = diccionario["data"]
            usuario = data["usuario"]
            contenido = data["contenido"]
            usuario = f"({datetime.now().hour}:{datetime.now().minute}) {usuario}"
            self.frontend.actualizar_chat(
                f"{usuario}: {contenido}")

        if diccionario["status"] == "no existe":
            self.color = diccionario["color"]
            self.name = diccionario["name"]
            self.frontend.spell_checker.check(["no existe", diccionario[
                "color"]])
            if diccionario["master"] == "Si":
                self.master = True

        elif diccionario["status"] == "existe":
            self.frontend.spell_checker.check(["existe"])

        elif diccionario["status"] == "sin acceso":
            self.frontend.spell_checker.check(["sin acceso"])

        elif diccionario["status"] == "acceso":
            self.name = diccionario["name"]
            self.color = diccionario["color"]
            self.frontend.spell_checker.check(["acceso", diccionario[
                "color"]])

            if diccionario["master"] == "Si":
                self.master = True

        elif diccionario["status"] == "iniciar":
            self.frontend.spell_checker.check(["iniciar"])

        if diccionario["status"] == "draw":
            self.frontend.spell_checker.check(diccionario)
            print("hola")

    def send(self, mensaje):
        '''
        Este método envía la información al servidor. Recibe un mensaje del tipo:
        {"status": tipo del mensaje, "data": información}
        '''

        # Codificamos y pasamos a bytes
        mensaje_codificado = json.dumps(mensaje)
        contenido_mensaje_bytes = mensaje_codificado.encode("utf-8")

        # Tomamos el largo del mensaje y creamos 4 bytes de esto
        tamano_mensaje_bytes = len(contenido_mensaje_bytes).to_bytes(4,
                                                                     byteorder="big")
        # Enviamos al servidor

        if len(tamano_mensaje_bytes) > 0:
            self.socket_cliente.send(tamano_mensaje_bytes +
                                     contenido_mensaje_bytes)

    def terminar_conexion(self):
        print("Conexión terminada")
        self.connected = False
        self.socket_cliente.close()
        exit()


if __name__ == "__main__":
    app = QApplication([])
    cliente = Cliente()
    sys.exit(app.exec_())