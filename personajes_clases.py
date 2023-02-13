class personaje:
    nombre = "Default"
    inteligencia = 0
    fuerza = 0
    defensa = 0
    vida = 0

    def __init__(self, nombre, fuerza, inteligencia, vida, defensa):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida
        self.defensa = defensa

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("fuerza:", self.fuerza)
        print("vida:", self.vida)
        print("inteligencia:", self.inteligencia)
        print("defensa:", self.defensa)

    def subir_nivel(self, fuerza, vida, defensa, inteligencia):
        self.fuerza = self.fuerza + fuerza
        self.vida = self.vida + vida
        self.defensa = self.defensa + defensa
        self.inteligencia = self.inteligencia + inteligencia

mi_personaje = personaje("jonysky", 20, 1, 90, 50)
mi_personaje.subir_nivel(10, 10, 10, 10)
mi_personaje.atributos()
