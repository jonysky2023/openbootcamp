class alumno:
    def puntuacion(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def resultado(self):
        if self.nota >= 5:
            print('\033[1m',self.nombre,'\033[0m',"tu puntuacion es:", self.nota, '\033[1m',"has aprobado",'\033[0m',)
        else:
            print('\033[1m',self.nombre,'\033[0m',"tu puntuacion es:", self.nota, '\033[1m',"has suspendido",'\033[0m',)

alumno1 = alumno()
alumno2 = alumno()
alumno3 = alumno()

alumno1.puntuacion("Juan",6)
alumno2.puntuacion("Laura",3)
alumno3.puntuacion("Sheila",5)

alumno1.resultado()
alumno2.resultado()
alumno3.resultado()

