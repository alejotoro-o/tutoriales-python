###########################################
########## FUNDAMENTOS DE PYTHON ##########
## APLICACIÓN DE REGISTRO DE ESTUDIANTES ##
###########################################

###############
## FUNCIONES ##
###############
def calcular_promedio_estudiante(estudiante):
    
    accum = 0

    for i in range(1,len(estudiante)):
        accum += float(estudiante[i])

    promedio = accum/(len(estudiante)-1)

    return str(promedio)

def buscar_estudiante(nombre, estudiantes):

    indice_estudiente = None
    
    for i in range(len(estudiantes)):
        
        if estudiantes[i][0].lower() == nombre.lower():
            indice_estudiente = i

    return indice_estudiente

def calcular_estadisticas_clase(estudiantes):
    
    accum = 0
    num_aprobados = 0
    num_reprobados = 0

    for estudiante in estudiantes:

        accum += float(estudiante[-1])

        if float(estudiante[-1]) >= 3.0:
            num_aprobados += 1
        else:
            num_reprobados += 1

    promedio_clase = accum/len(estudiantes)

    return promedio_clase, num_aprobados, num_reprobados


def mostrar_tabla(estudiantes):

    max_string_len = dar_formato(estudiantes)
    
    #print(max_string_len)

    print("Nombre".ljust(max_string_len), "|", "N1".ljust(max_string_len), "|", "N2".ljust(max_string_len), "|", "Promedio".ljust(max_string_len))

    for estudiante in estudiantes:

        print(estudiante[0].ljust(max_string_len), "|", estudiante[1].ljust(max_string_len), "|", estudiante[2].ljust(max_string_len), "|", estudiante[3].ljust(max_string_len))

def dar_formato(estudiantes):

    max_len = 0

    for estudiante in estudiantes:

        if len(estudiante[0]) > max_len:
            max_len = len(estudiante[0])

    return max_len

########################
## VARIABLES GLOBALES ##
########################
init = False
estudiantes = [] # estudiantes = [[nombre1,nota1,nota2,promedio],[nombre2,nota1,nota2,promedio]]

#####################
## CICLO PRINCIPAL ##
#####################
while 1:

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

    if opcion == "a":

        if not estudiantes:
            print("No hay estudiantes en la lista.")
            continue

        mostrar_tabla(estudiantes)

    elif opcion == "b":

        if not estudiantes:
            print("No hay estudiantes en la lista.")
            continue

        estudiantes.sort(key=lambda estudiante : estudiante[0])
        mostrar_tabla(estudiantes)

    elif opcion == "c":

        if not estudiantes:
            print("No hay estudiantes en la lista.")
            continue

        estudiantes.sort(key=lambda estudiante : estudiante[-1], reverse=True)
        mostrar_tabla(estudiantes)

    elif opcion == "d":

        print("Ingrese la información del estudiante de la siguiente forma <nombre,nota1,nota2>: ")

        estudiante = input().split(",") ## estudiante = [nombre, n1, n2]
        estudiante.append(calcular_promedio_estudiante(estudiante)) ## -> estudiante = [nombre, n1, n2, promedio]
        estudiantes.append(estudiante)


    elif opcion == "e":

        print("Ingrese el nombre del estudiante que desea eliminar.")

        nombre = input()
        indice_estudiante = buscar_estudiante(nombre, estudiantes)

        if indice_estudiante is not None:
            
            estudiantes.pop(indice_estudiante)
            print("Estudiante eliminado.")

        else:

            print("El estudiante no esta en la lista.")

    elif opcion == "f":

        if not estudiantes:
            print("No hay estudiantes en la lista.")
            continue

        promedio_clase, num_aprobados, num_reprobados = calcular_estadisticas_clase(estudiantes)

        print("Las estadisticas de la clase son:")
        print(f"Promedio de la clase: %.2f" % promedio_clase)
        print("Número de estudiantes aprobados: ", num_aprobados)
        print("Número de estudiantes reprobados: ", num_reprobados)

    elif opcion == "q":

        break

    else:

        print("La opción ingresada no existe.")
