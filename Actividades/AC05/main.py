from abc import ABC, abstractmethod


class Propiedades(ABC):
    def __init__(self, ki,resistencia, fuerza, vida,capacidad):
        self.ki = ki
        self.resistencia = resistencia
        self.fuerza = fuerza
        self._vida = vida
        self.capacidad = capacidad

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, value):
        if value < 0:
            self._vida = 0
        else:
            self._vida = value


class Humano(Propiedades):

    def __init__(self, inteligencia, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.inteligencia = inteligencia

    def atacar_(self, enemigo):
        enemigo.vida -= enemigo.ki*(enemigo.fuerza-enemigo.resistencia)/2

    def meditar_(self):
        self.ki += self.inteligencia/100


class Extraterrestre(Propiedades):

    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)

    def atacar_(self, enemigo):
        enemigo.vida -= enemigo.ki*(enemigo.fuerza-enemigo.resistencia)/2


class Supersayayin(Humano, Extraterrestre):

    def __init__(self, cola , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cola = cola

    def perder_cola(self):
        self.fuerza = (self.fuerza)*0.6
        self.cola -= 1


class Hakashi(Extraterrestre):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def robar_ki(self, *args):
        for i in args:
            self.ki += (i.ki)*0.5


if __name__ == '__main__':

    hakashi1 = Hakashi(21, 2 ,3, 1,100)
    hakashi2 = Hakashi(22, 2, 3, 1, 100)
    humano = Humano(22, 2, 3, 1, 100,2)
    superyayasines1 = Supersayayin(1, 2 ,3, 1,100,4, 1)
    superyayasines2 = Supersayayin(1, 2, 4, 3, 100, 4, 1)

    superyayasines1.atacar_(hakashi1)
    superyayasines1.perder_cola()
    hakashi1.atacar_(superyayasines2)
    print(hakashi1.__dict__)
    hakashi1.atacar_(superyayasines2)
    humano.meditar_()
    print(hakashi1.__dict__)
    print(superyayasines1.__dict__)

    pass
