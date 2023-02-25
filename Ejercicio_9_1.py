paises = []

def añadirpaises():
    pais = input("Añada un pais:")
    paises.append(pais)

añadirpaises()
preguntarañadir = input("desea agregar mas paises? Y/N")

while preguntarañadir == "Y" or preguntarañadir == "y":
    añadirpaises()
    preguntarañadir = input("desea agregar mas paises? Y/N")

unicos = list(set(paises))
print(sorted(unicos))
