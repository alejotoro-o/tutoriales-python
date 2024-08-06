############
## CLASES ##
############
from abc import ABC
import statistics

class Persona(ABC):

    def __init__(self, nombre, apellido, id):
        
        self.nombre = nombre
        self.apellido = apellido
        self.id = id

class Estudiante(Persona):

    def __init__(self, nombre, apellido, id, notas=[]):

        super().__init__(nombre, apellido, id)

        self.notas = notas
        self.promedio = None
        self.estado = None

        self._calcular_promedio()

    def _calcular_promedio(self):
        
        self.promedio = statistics.mean(notas)

        if self.promedio >= 3.0:
            self.estado = "Aprobado"
        else:
            self.estado = "Reprobado"

class Clase():

    def __init__(self):
        
        self.estudiantes = []
        self.num_aprobados = 0
        self.num_reprobados = 0
        self.promedio = None

    def añadir_estudiante(self, estudiante):

        self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, id_del):

        indice_estudiante = None

        for i in range(len(self.estudiantes)):

            if self.estudiantes[i].id == id_del:
                indice_estudiante = i
        
        if indice_estudiante is not None:
            self.estudiantes.pop(indice_estudiante)
            print("El estudiante fue eliminado")
        else:
            print("El estudiante no existe")

    def mostrar_clase(self):

        indent_len = 10

        print(f"| %s | %s | %s | %s | %s | %s | %s |" % ("Nombre".ljust(indent_len), "Apellido".ljust(indent_len), "ID".ljust(indent_len), "Nota 1".ljust(indent_len), "Nota 2".ljust(indent_len), "Promedio".ljust(indent_len), "Estado".ljust(indent_len)))

        for estudiante in self.estudiantes:

            print(f"| %s | %s | %s | %s | %s | %s | %s |" % (estudiante.nombre.ljust(indent_len), estudiante.apellido.ljust(indent_len), str(estudiante.id).ljust(indent_len), str(estudiante.notas[0]).ljust(indent_len), str(estudiante.notas[1]).ljust(indent_len), str(estudiante.promedio).ljust(indent_len), estudiante.estado.ljust(indent_len)))

    def mostrar_estadisticas(self):

        self.__calcular_promedio()
        self.__calcular_num_aprobados_reprobados()

        print("Las estadisticas de la clase son:")
        print(f"Promedio de la clase: %.2f" % self.promedio)
        print("El numero de estudiantes aprobados es:", self.num_aprobados)
        print("El numero de estudiantes reprobados es:", self.num_reprobados)

    def __calcular_num_aprobados_reprobados(self):

        self.num_aprobados = 0
        self.num_reprobados = 0
        
        for estudiante in self.estudiantes:

            if estudiante.promedio >= 3.0:
                self.num_aprobados += 1
            else:
                self.num_reprobados += 1
        

    def __calcular_promedio(self):
        
        acum = 0
        
        for estudiante in self.estudiantes:

            acum += estudiante.promedio

        self.promedio = acum/len(self.estudiantes)

    def ordenar_estudiantes_alfabetico(self):

        self.estudiantes.sort(key=lambda estudiante : estudiante.nombre)

    def ordenar_estudiantes_promedio(self):

        self.estudiantes.sort(key=lambda estudiante : estudiante.promedio, reverse=True)

#####################
## CICLO PRINCIPAL ##
#####################

clase = Clase()
init = False
id = 0

while 1:

    print("")

    if init == False:
        print("-------------------------------------------------------")
        print("Bienvenido a la applicación de registro de estudiantes.")
        init = True

    print("-------------------------------------------------------")

    print("Seleccione que operación desea realizar:")
    print("a - Mostrar lista de estudiantes.")
    print("b - Ordenar lista de estudianes en orden alfabetico.")
    print("c - Ordenar lista de estudiantes por calificación.")
    print("d - Añadir estudiante.")
    print("e - Eliminar estudiante.")
    print("f - Calcular estadisticas de la clase.")
    print("q - Salir de la aplicación.")

    opcion = input()

    print("")

    if opcion == "a":

        if not clase.estudiantes:
            print("No hay estudiantes en la lista.")
            continue

        clase.mostrar_clase()

    elif opcion == "b":

        if not clase.estudiantes:
            print("No hay estudiantes en la lista.")
            continue

        clase.ordenar_estudiantes_alfabetico()
        clase.mostrar_clase()

    elif opcion == "c":

        if not clase.estudiantes:
            print("No hay estudiantes en la lista.")
            continue

        clase.ordenar_estudiantes_promedio()
        clase.mostrar_clase()

    elif opcion == "d":

        print("Ingrese el nombre y el apellido del estudiante separados por ',': ")
        nombre, apellido = input().split(",")
        # print("Ingrese la identificación del estudiante: ")
        # id = input()
        print("Ingrese las notas del estudiante: ")
        notas = []
        print("Nota 1: ")
        notas.append(float(input()))
        print("Nota 2: ")
        notas.append(float(input()))

        estudiante = Estudiante(nombre, apellido, id, notas)
        id += 1

        clase.añadir_estudiante(estudiante)

    elif opcion == "e":

        print("Ingrese la id del estudiante que desea eliminar:")

        id_del = input()
        clase.eliminar_estudiante(float(id_del))

    elif opcion == "f":

        if not clase.estudiantes:
            print("No hay estudiantes en la lista.")
            continue

        clase.mostrar_estadisticas()

    elif opcion == "q":

        break

    else:

        print("La opción ingresada no existe.")
