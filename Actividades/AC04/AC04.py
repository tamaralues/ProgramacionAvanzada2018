class Aventurero:

    def __init__(self, nombre, vida, ataque, velocidad):

        self.nombre = nombre
        self._vida = vida
        self.ataque = ataque
        self.velocidad = velocidad

    # Atributo
    @property
    def poder(self):
        return self.ataque + self.velocidad + self.vida

    # Atributo
    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, vida):
        # Requisitos de vida
        pass

    def __str__(self):
        return "{} : Gloria al Tini".format(self.nombre)


class Guerrero(Aventurero):

    def __init__(self, defensa):
        self._defensa = defensa
        super().__init__(vida, ataque, velocidad)

    #Atributo
    @property
    def defensa(self):
        return self.defensa

    @defensa.setter
    def defensa(self, defensa):
        # Requisitos de refensa
        pass

    @property
    def poder(self):
        return self.poder

    @poder.setter
    def poder(self, poder):
        # Cambios a poder
        pass


class Mago(Aventurero):

    def __init__(self, magia):
        self._magia = magia
        super().__init__(vida, ataque, velocidad)

    @property
    def magia(self):
        return self._magia

    @magia.setter
    def magia(self, magia):
        #Formula magia
        pass


class Monstruo:

    def __init__(self, nombre, vida, poder, jefe):
        self.nombre = nombre
        self._vida = vida
        self._poder = poder
        self._jefe = jefe

    @property
    def poder(self):
        return self._poder

    @poder.setter
    def poder(self, poder):
        # Operaciones de poder
        pass

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, vida):
        # Operaciones vida
        pass


class Clan(Aventurero):

    def __init__(self, nombre, lista_aventureros, rango):
        super().__init__(vida, ataque, velocidad)
        self._nombre = nombre
        self.lista_aventureros = lista_aventureros
        self._rango = rango

    def revisador(self):

        lista= []
        for i in self.lista_aventureros:
            if isinstance(i, Aventurero) == False :

                print("No es posible agregar a monstruos a clanes")
            else:
                pass



    @property
    def rango(self):
        return self._rango

    @rango.setter
    def rango(self, rango):
        # Restricciones de rango
        pass

    @property
    def poder(self):
        return self.poder

    @poder.setter
    def poder(self, poder):

        c= 0
        ponderador = 0
        if rango == "Bronce":
            ponderador = 0.5
        # Par todos los rangos

        for i in self.lista_aventureros:
            c+= i.poder*ponderador

        self.poder = c


class Mazmorra(Monstruo):
    def __init__(self, nombre, lista_monstruo):
        super().__init__(vida, ataque, velocidad)
        self._nombre = nombre
        self.lista_monstruo = lista_monstruo

    @property
    def poder(self):
        return self.poder

    @poder.setter
    def poder(self, poder):

        c = 0
        for i in self.lista_monstruo:
            c+= i.poder

        self.poder = c









