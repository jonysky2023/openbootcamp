import sqlite3

conn = sqlite3.connect('Alumnos.db')
cursor = conn.cursor()

listaid = [1, 2, 3, 4, 5, 6, 7, 8]
listanombre = ["Joan", "Monica", "Martina", "Mariona", "Toni", "Jessica", "Sheila", "Angels"]
listaapellido = ["Serra", "Montero", "Serra", "Serra", "Barrante", "Masso", "Masso", "Serra"]

for i in range(len(listaid)):
    query = 'INSERT INTO Alumnos (id, nombre, apellido) VALUES (?, ?, ?)'
    values = (listaid[i], listanombre[i], listaapellido[i])
    cursor.execute(query, values)

rows = cursor.execute('SELECT * FROM Alumnos WHERE nombre="Joan"')
for row in rows:
    print(row)

conn.commit()
cursor.close()
conn.close()

