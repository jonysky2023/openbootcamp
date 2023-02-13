persona ={"nombre":"Joan","Apellido":"Serra","Edad":47,"Sueldo":1200.15}
print(persona)
print(persona["Sueldo"])

# cambiar contenido de una  llave
persona["Edad"]=40
print(persona)

# eliminar una llave
del persona["Edad"]
print(persona)

# buscar contenido de una llave
print(persona.get("nombre1","Clave no encontrada"))

# Mostrar valores y llaves
print(persona.keys())
print(persona.values())