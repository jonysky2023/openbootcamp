nEdad = int(input("su edad?"))

# OPERADOR AND
if nEdad>=1 and nEdad<=10:
    print("es un niño")
elif nEdad>=11 and nEdad<=17:
    print("es joven")
else:
    print("es adulto")


# OPERADOR OR
if nEdad==1 or nEdad==10:
    print("mi edad esta entre los 1 y 10 años")
else:
    print("no tengo definida la edad")

# OPERADOR OR (da una respuesta contraria)
if not nEdad==10:
    print("Mi edad es de 10 años")
else:
    print("Mi edad no esta catalogada")