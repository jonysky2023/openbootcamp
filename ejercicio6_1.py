class vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class coche(vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def atributos(self):
       print("-Color:", self.color)
       print("-Ruedas:", self.ruedas)
       print("-Puertas:", self.puertas)
       print("-Velocidad:", self.velocidad)
       print("-Cilindrada:", self.cilindrada)

coche = coche("Rojo", 4, 5, 240, 1200)
coche.atributos()
