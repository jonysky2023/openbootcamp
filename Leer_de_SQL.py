import sqlite3
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

# seleccionar todos los datos de la tabla
cursor.execute("SELECT * FROM estudiantes")

# Mostrar solo uno
usuarios = cursor.fetchone()
print(usuarios)

# Mostrar todos
usuarios = cursor.fetchall()
print(usuarios)