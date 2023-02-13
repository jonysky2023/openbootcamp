import sqlite3
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()
conexion.close()