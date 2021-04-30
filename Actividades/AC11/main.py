import os

def buscar_archivo(nombre, cwd=os.getcwd()):
    for root, dirs, nombre in os.walk(".", topdown=False):
        for name in nombre:
            var = os.path.join(root, name).split("/")
            for i in var:
                if i == "himno.shrek":
                    print("entre")
                    print(os.path.join(root, name)[2:])
                    return os.path.join(root, name)[2:]
    return nombre


def leer_archivo(path):

    with open(path, "rb") as himno:
        suma =0
        arch = himno.read()
        arch = arch.split()
        lista_aux = []

        for i in range(len(arch)):
            if i == 0:
                lista_aux.append(arch[i:i + 2])
            elif i < (len(arch) - 2):
                lista_aux.append(arch[i + 1:i + 2])




            # envio linea a descomprimir
def decodificar(bits):
    pass


def escribir_archivo(ruta, chunks):
    pass


# Aquí puedes crear todas las funciones extra que requieras.


if __name__ == "__main__":
    nombre_archivo_de_pista = "himno.shrek"
    ruta_archivo_de_pista = buscar_archivo(nombre_archivo_de_pista)

    chunks_corruptos_himno = leer_archivo(ruta_archivo_de_pista)

    chunks_himno = [decodificar(chunk) for chunk in chunks_corruptos_himno]

    nombre_ubicacion_himno = "himno.png"
    escribir_archivo(nombre_ubicacion_himno, chunks_himno)
