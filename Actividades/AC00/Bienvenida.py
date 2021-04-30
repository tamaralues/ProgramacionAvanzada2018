print("Bienvenid@ a IIC2233")



class Circulo():

    def __init__(self, radio):
        self.radio=radio
        self.area=0
        self.perimetro=0

    def obtener_area(self):
        self.area= (3.14)*self.radio**2

    def obtener_perimetro(self):
        self.perimetro=2*(3.14)*self.radio

    def __str__(self):
        self.obtener_perimetro()
        self.obtener_area()
        return str(self.perimetro) + " , "+ str(self.area)

circulo=Circulo(2)
print(circulo)



