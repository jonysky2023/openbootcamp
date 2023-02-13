lista = [1,4,6,2,4,3,1,1,3,5,6,7,3,4,5,5,5,3,3,2,1,2,1,1,1,2,6,6]
def max_repetido(lista):
    all = len(lista)
    repet = []
    for i in range(all):
        k = i + 1
        for j in range(k, all):
            if lista[i] == lista[j] and lista[i] not in repet:
                repet.append(lista[i])
                return repet

print(max_repetido(lista))