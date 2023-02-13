class vehiculo:
    color="rojo"
    ruedas= "Michelin"
    puertas= 5

class coche(vehiculo):
    velocidad= 240
    cilindrada= 110

hyundai = coche()
print("la velocidad es de:", hyundai.velocidad,"km/h")


