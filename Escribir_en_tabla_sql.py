# Escribir varios datos a la vez

import sqlite3
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

usuarios = [
    ("js.serra@gmail.com","diseño","Joan",47),
    ("tbarrante@dunasoftpc.com","programador","Toni",34),
    ("soporte@dunasoftpc.com","diseño","Laura",30),
    ("soporte4@dunasoftpc.com","helpdesk","Marc",28)
]

cursor.executemany("INSERT INTO estudiantes VALUES (?,?,?,?)", usuarios)

conexion.commit()

conexion.close()


# Escribir un solo dato en la SQL
# OJO Aqui con las comillas dentro d3e la funcion de cursor.execute (tiene importancia que sea diferente)

import sqlite3
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

cursor.execute("INSERT INTO estudiantes VALUES ('maguilar@dunasoftpc.com','administracion','Monica', 50)")

conexion.commit()
conexion.close()

