#cargamos modulo de exportacion a binario
import pickle

#creamos la clase y el objeto
class vehiculo:
    marca = ""
    modelo = ""
    potencia = ""

    def __init__(self, marca, modelo, potencia):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia

    def getmarca(self):
        return self.marca

    def getmodelo(self):
        return self.modelo

v1 = vehiculo("Hyundai", "I30", 110)

#Creamos variable para Crear fichero y generamos el fichero .bin
f = open("vehiculo.bin", "wb")
pickle.dump(v1, f)
f.close()

#llamamos al fichero .bin y cargamos una variable con las propiedades del objeto
f = open("vehiculo.bin", "rb")
coche = pickle.load(f)
f.close()

#Cargamos propiedades del objeto desde la variable creada a traves de la carga del fichero (no desde la clase creada en este fichero)
print("Mi coche es un:", coche.getmarca(), coche.getmodelo(),"y tiene una potencia de", (coche.potencia),"CV")


