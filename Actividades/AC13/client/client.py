"""
client.py -- un simple cliente
"""

import pickle
from socket import socket, SHUT_RDWR
import os

HOST = '127.0.0.1'


class Client:
    """
    Una clase que representa un cliente.
    """

    def __init__(self, port):
        self.host = HOST
        self.port = port
        self.socket = socket()
        self.connected = False
        self.file_name = ""

        # Este diccionario tiene los comandos disponibles.
        # Puedes modificarlo para agregar nuevos comandos.
        self.commands = {
            "help": self.help,
            "logout": self.logout, "ls":self.ls,"upload": self.upload,
            "download": self.download
        }

    def run(self):
        """
        Enciende el cliente que puede conectarse
        para enviar algunos comandos al servidor.
        """

        self.socket.connect((self.host, self.port))
        self.connected = True

        while self.connected:
            command, *args = input('$ ').split()
            function = self.commands.get(command)

            if function is None:
                print(f"El comando '{command}' no existe.")
                print("Escribe 'help' para obtener ayuda.")
            elif command == 'help':
                self.help()
            else:
                print(*args, command)
                self.send(pickle.dumps((command, args)))
                function(*args)

    def send(self, message):
        """
        [MODIFICAR]
        Envía datos binarios al servidor conectado por el socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """
        self.socket.sendall(len(message).to_bytes(4, byteorder='big') + message)

    def receive(self):
        """
        [COMPLETAR]
        Recibe datos binarios del servidor, a través del socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """
        # Leemos los 4 bytes del tamaño del archivo.
        # Con esto transformamos una serie de bytes en un int.
        largo_archivo = int.from_bytes(self.socket.recv(4), byteorder='big')
        datos = bytearray()

        # Ahora leemos el archivo por chunks, de máximo 4096 bytes.
        while len(datos) < largo_archivo:
            # El último recv será probablemente más chico que 4096
            bytes_leer = min(4096, largo_archivo - len(datos))
            datos_recibidos = self.socket.recv(bytes_leer)
            datos.extend(datos_recibidos)

        return datos

    def help(self):
        print("Esta es la lista de todos los comandos disponibles.")
        print('\n'.join(f"- {command}" for command in self.commands))

    def ls(self):
        """
        [COMPLETAR]
        Este comando recibe una lista con los archivos del servidor.

        Ejemplo:
        $ ls
        - doggo.jpg
        - server.py
        """

        lista = pickle.loads(self.receive())

        for i in lista:
            print("-" + str(i) + "\n")

    def upload(self, filename):
        """
        [COMPLETAR]
        Este comando envía un archivo hacia el servidor.
        """
        with open(filename, "rb") as file:
            self.send(file.read())

    def download(self, filename):
        """
        [COMPLETAR]
        Este comando recibe un archivo ubicado en el servidor.
        """
        with open(filename, "wb") as file:
            file.write(self.receive())

    def logout(self):
        self.connected = False
        self.socket.shutdown(SHUT_RDWR)
        self.socket.close()
        print("Arrivederci.")


if __name__ == '__main__':
    port_ = input("Escriba el puerto: ")
    client = Client(int(port_))
    client.run()
