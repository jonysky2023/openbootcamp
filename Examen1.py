"""
L = [1, 5, 10, 20]
entero = 3
def agregar_entero(L, entero):
    L.append(entero)
    L.sort()
    return L

nueva_lista = agregar_entero(L, 3)
print(nueva_lista)
"""


lista = [1,4,6,2,4,3,1,1,3,5,6,7,3,4,5,5,5,3,3,2,1,2,1,1,1,2,6,6]

def max_repetido(lista):
    count = {}
    for num in lista:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return max(count.values())
print(lista)