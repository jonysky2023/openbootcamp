modalidades=["3d","olimpico","desnudo","2D","campo"]
print(modalidades)

#cambio de elementos de la lista
modalidades[2]="compuesto"
print(modalidades)

#Solo mostrar el elemento de la posicion 3
print(modalidades[3])

#Solo mostrar el elemento de la posicion ultima
print(modalidades[-1])

#entre el segundo y cuarto elemento
print(modalidades[2:4])

#solo 2 elementos desde el inicio
print(modalidades[:3])

#agregar contenido a la lista
modalidades.append("tradicional")
modalidades.append("tradicional")
print(modalidades)

#agregar contenido a la lista en una posicion concreta
modalidades.insert(2,"ballesta")
print(modalidades)

#agregar varios contenidos de una sola vez
modalidades.extend(["flechas","culatines","plumas","puntas"])
print(modalidades)

#buscar contenido dentro de la lista
print(modalidades.index("plumas"))

#eliminar contenido de la lista
modalidades.remove("ballesta")
print(modalidades)

#contabilizar contenido de la lista
print(modalidades.count("tradicional"))