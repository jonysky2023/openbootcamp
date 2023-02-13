# Crearemos la tabla SQL (Joan basicamente es crear las columnas y las filas)

import sqlite3
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

# Crearemos una tabla llamada estudiantes
cursor.execute("CREATE TABLE estudiantes (email VARCHAR(100),carrera VARCHAR(100),nombre VARCHAR(100),edad INTEGER)")
conexion.close()


