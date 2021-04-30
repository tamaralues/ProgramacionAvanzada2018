"""
server.py -- un simple servidor
"""

import pickle
from socket import socket
import os

HOST = '127.0.0.1'


class Server:
    """
    Una clase que representa un servidor.
    """

    def __init__(self, port):
        self.host = HOST
        self.port = port
        self.client = None
        self.socket = socket()

        self.commands = {
            "ls": self.list_filenames,
            "download": self.send_file,
            "upload": self.save_file,
            "logout": self.disconnect,
        }

    def run(self):
        """
        Enciende el servidor que puede conectarse
        y recibir comandos desde un único cliente.
        """

        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Escuchando en {self.host}:{self.port}.")

        while self.client is None:
            self.client, _ = self.socket.accept()
            print("¡Un cliente se ha conectado!")

            while self.client:
                command, args = pickle.loads(self.receive())
                self.commands[command](*args)

        print("Arrivederci.")

    def send(self, message):
        """
        [COMPLETAR]
        Envía datos binarios al cliente conectado por el socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """
        # (int.to_bytes transforma un entero en una cantidad de bytes por el primer parámetro)
        self.client.sendall(len(message).to_bytes(4, byteorder='big') +
                             message)

    def receive(self):
        """
        [MODIFICAR]
        Recibe datos binarios del cliente, a través del socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """

        print("Conexión entrante aceptada.")

        # Leemos los 4 bytes del tamaño del archivo.
        # Con esto transformamos una serie de bytes en un int.
        largo_archivo = int.from_bytes(self.client.recv(4), byteorder='big')
        datos = bytearray()

        # Ahora leemos el archivo por chunks, de máximo 4096 bytes.
        while len(datos) < largo_archivo:
            # El último recv será probablemente más chico que 4096
            bytes_leer = min(4096, largo_archivo - len(datos))
            datos_recibidos = self.client.recv(bytes_leer)
            datos.extend(datos_recibidos)

        return datos  # maldición, esto es poco.

    def list_filenames(self):
        """
        [COMPLETAR]
        Envía al cliente una lista que contiene los nombres de
        todos los archivos existentes en la carpeta del servidor.
        """
        var = pickle.dumps(os.listdir(os.getcwd()))
        self.send(var)

    def send_file(self, filename):
        """
        [COMPLETAR]
        Envía al cliente un archivo ubicado en el directorio del servidor.
        """
        with open(filename, "rb") as file:
            self.send(file.read())

    def save_file(self, filename):
        """
        [COMPLETAR]
        Guarda un archivo recibido desde el cliente.
        """
        with open(filename, "wb") as file:
            file.write(self.receive())

    def disconnect(self):
        self.client = None
        print("El cliente se ha desconectado.")


if __name__ == '__main__':
    port_ = input("Escriba el puerto: ")
    server = Server(int(port_))
    server.run()
