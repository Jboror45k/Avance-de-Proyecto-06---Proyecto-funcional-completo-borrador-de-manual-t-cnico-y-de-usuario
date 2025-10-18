# Lista de cursos disponiblcursos = []
# es opcinonal la siguiente lista
mi_lista_cursos = [
    "Contabilidad 2", "Precalculo", "Algoritmos", "Algebra lineal",
    "Matematica discreta", "Programacion 1", "Programacion 2",
    "Fisica 1", "Fisica 2", "Calculo 1", "Calculo 2"
]
cursos = []  # <-- Agregar esto al inicio

#aqui se registra las notas que ya se han guardado y nos devuelve en la pantalla
#todas las cantidades guardadaes
def registrar_curso_y_nota():
    while True:
        usar_lista = input("¿Quieres verificar si un curso esta disponible en la lista UMG? (S/N): ").strip().lower()
        
        if usar_lista == "s":
            print("\nAcontinuacion la lista de Cursos Disponilbes:")
            for i, elem in enumerate(mi_lista_cursos, start=1):
                   print(i, ".", elem)

            try:
                indice = int(input("Selecciona el número del curso: "))
                if 1 <= indice <= len(mi_lista_cursos):
                    curso = mi_lista_cursos[indice-1]
                else:
                    print("Número fuera de lo establecido.\n")
                    continue
            except ValueError:
                print("Debes ingresar un número válido.\n")
                continue
        else:
            curso = input("Ingrese el curso: ").strip()
            if not curso:
                print("El curso no puede estar vacío.\n")
                continue

        try:
            nota = float(input("Ingrese la nota del curso (0 a 100): "))
            if 0 <= nota <= 100:
                historial.append(curso)  # guardamos en el historial
                cursos.append({"curso": curso, "nota": nota})
                print("Registro exitoso ........")
                print("Nombre del Curso", curso, "registrado con la nota de ", nota, "\n")
                

            else:
                print("Error: la nota debe estar entre 0 y 100.\n")
                continue
        except ValueError:
            print("Error: debes ingresar un número válido.\n")
            continue

        opcion = input("¿Registrar otro curso? (S/N): ").strip().lower()
        if opcion != "s":
            break
#aqui en esta funcion nos va a mostrar todas las notas guardadas y las mostrara en la consola
#muestra las notas registradas en la unidad guardada
def mostrar_todas_las_notas():
    if cursos:
        print("\nRegistro de notas por curso:")
        for i, c in enumerate(cursos, start=1):
            print(f"{i}. {c['curso']}:{c['nota']}")
        print()
    else:
        print("No se han registrado cursos.\n")

#aqui vamos a calcular el promedio por medio de una funcion que suma todas las notas y las divide
#dentro de las canctidades de notas y nos regresa el promedio
def calcular_promedio_general():
    if cursos:
        promedio = sum(c["nota"] for c in cursos) / len(cursos)
        print(" El promedio general es: \n", promedio)
    else:
        print("No fue posible calcular el promedio (no hay cursos registrados).\n")

# esta es la funcion que nos sirve para buscar una nota que este guardada en el sistema
# esta funcion nos motrara la nota registrada
def buscar_nota_por_curso():
    if not cursos:
        print("No has registrado cursos.\n")
        return
    curso_buscar = input("Ingrese el curso a buscar: ")
    for c in cursos:
        if c["curso"].lower() == curso_buscar.lower():
            print(f"Registro encontrado: {c['curso']}, Nota: {c['nota']}\n")
            return
    print("Curso no encontrado.\n")

# esta es la funcion que nos sirve para eliminar el curso que estemos usando o el curso que 
# queramos quitar del programa
def eliminar_curso():
    if not cursos:
        print("No hay cursos para eliminar.\n")
        return
    eliminar = input("Nombre del curso a eliminar: ")
    for i in range(len(cursos)):
        if cursos[i]["curso"].lower() == eliminar.lower():
            cursos.pop(i)
            print("Curso", eliminar, " eliminando.\n")
            return
    print("No se encontró ese curso.\n")

#aqui es donde se guardara el historial de los cursos que lleva
#historial cursos
# historial cursos
# historial cursos
historial = []

def historial_curso():
    if historial:
        print("\nHistorial de cursos:")
        for i, curso in enumerate(historial, start=1):
            print(i, ".", curso)
    else:
        print("El historial está vacío.\n")

# aqui tenesmo el menu principal del proyecto de la unidad
# Simulación de cola de solicitudes de revisión de los cursos que desee
def cola_revision():
    cola = []  # Lista para simular la cola de cursos

    # Ingreso de cursos que va a Revisar
    while True:
        curso = input("Ingrese curso para revisión y 'fin' para terminar:\n> ")
        if curso.lower() == "fin":
            break
        # Agregar al final de la cola
        cola.append(curso) 

    # Procesar la cola que esta mandando el usuario
    print("\nProcesando las solicitudes:")
    while cola:
        curso_actual = cola.pop(0)  # Sacar el primer elemento (FIFO)
        print("Revisando el curso de: ", curso_actual)

# aqui comienza la opcion de ordenado de Burbuja que de notas
def ordenar_burbuja(cursos):
    n = len(cursos)
    for i in range(n):
        for h in range(0, n-i-1):
            if cursos[h]["nota"] > cursos[h+1]["nota"]:
                cursos[h], cursos[h+1] = cursos[h+1], cursos[h]
    return cursos

# aqui comienza el ordenamiento por interseccion de los cursos guardados
def ordenar_insercion(cursos):
    n = len(cursos)
    for i in range(1, n):
        clave = cursos[i]
        m = i - 1
        # Comparar los nombres de los cursos alfabéticamente
        while m >= 0 and cursos[m]["curso"].lower() > clave["curso"].lower():
            cursos[m + 1] = cursos[m]
            m -= 1
        cursos[m + 1] = clave
        print("                             ")
    return cursos
print("                             ")

# esta opcion es simple solo mostrara los cursos que fueron aprobados mayor a 61
def cursos_aprobados():
    print("\n--- Cursos Aprobados ---")
    aprobados = [c for c in cursos if c['nota'] >= 61]
    if aprobados:
        for c in aprobados:
            print("Curso:", c['curso'], "Nota:", c['nota'])
    else:
        print("Ningún curso aprobado.")
    print()

# esta opcion va permitir al usuario actualizar su curso final y su historial final
def actualizar_nota():
    if not cursos:
        print("\nNo has registrado cursos aún.\n")
        return

    print("\n Cursos registrados:")
    for i, c in enumerate(cursos, 1):
        print(f"{i}. {c['curso']} (Nota actual: {c['nota']})")

    curso_buscar = input("\nIngresa el nombre de curso que quieres actualizar:\n> ").strip()
    encontrado = False

    for c in cursos:
        if c["curso"].lower() == curso_buscar.lower():
            try:
                nota_actualizada = float(input("Ingrese la nueva nota para el curso:\n> "))
                c["nota"] = nota_actualizada
                print(f"\nLa nota del curso {c['curso']} ha sido actualizada a {nota_actualizada}.\n")
                encontrado = True
                break
            except ValueError:
                print(" Error: la nota debe ser un número válido.\n")
                return

    if not encontrado:
        print(f" No se encontró el curso '{curso_buscar}'.\n")


#aqui esta el menu de revision del proyecto
while True:
    print("        MENÚ PRINCIPAL      ")
    print("1. Registrar curso nuevo y nota")
    print("2. Mostrar todas las notas")
    print("3. Calcular promedio general")
    print("4. Buscar nota por curso")
    print("5. Eliminacion de curso")
    print("6. Actualizar la nota de un curso") 
    print("7. Mostrar cursos aprobados")
    print("8. historial de cursos")
    print("9. Solicitud de Revicion de Cursos")
    print("10. Ordenacion de cursos en Burbuja")
    print("11. Ordenacion de cursos en insercion")
    print("12. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        registrar_curso_y_nota()
    elif opcion == "2":
        mostrar_todas_las_notas()
    elif opcion == "3":
        calcular_promedio_general()
    elif opcion == "4":
        buscar_nota_por_curso()
    elif opcion == "5":
        eliminar_curso()
    elif opcion == "6": 
        actualizar_nota()
    elif opcion == "7":
        cursos_aprobados()
    elif opcion == "8":
        historial_curso()
    elif opcion == "9":
        cola_revision()
    elif opcion == "10":
        cursos_ordenados = ordenar_burbuja(cursos)
        print("\nCursos ordenados por nota de menor a mayor:")
        for c in cursos_ordenados:
            print(f"{c['curso']}: {c['nota']}")
        print()
    elif opcion == "11":
        cursos_ordenados = ordenar_insercion(cursos)
        print("Cursos ordenados por nombre:")
        for c in cursos_ordenados:
            print(f"{c['curso']}: {c['nota']}")
            print("                             ")
    elif opcion == "12":    
        print("Saliendo...")
        print("                             ")
        break
    else:
        print("Opción no válida.\n")
        print("                             ")
