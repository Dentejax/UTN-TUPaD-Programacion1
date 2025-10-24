
#Ejercicio 1
def crear_archivo_notas():
    with open("notas.txt", "w") as archivo:
        archivo.write("Sofia,9\n")
        archivo.write("Marcos,7\n")
        archivo.write("Ana,10\n")
    print("Archivo creado con notas iniciales.")

def leer_archivo_notas():
    with open("notas.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            nombre, nota = linea.split(",")
            print(f"Estudiante: {nombre} | Nota: {nota}")

def agregar_nota():
    with open("notas.txt", "a") as archivo:
        while True:
            nombre = input("Ingrese el nombre del estudiante (o 'n' para salir): ")
            if nombre.lower() == 'n':
                break
            nota = input("Ingrese la nota del estudiante: ")
            archivo.write(f"{nombre},{nota}\n")

def reescribir_archivo_notas():
    with open("notas.txt", "w") as archivo:
        archivo.write("Agustina,10\n")
        archivo.write("Diego,6\n")
        archivo.write("Valentina,8\n")
    print("Archivo reescrito con nuevas notas.")

while True:
    print("--------------------------")
    print("Menu de opciones de notas:")
    print("--------------------------")
    print("1. Crear archivo")
    print("2. Leer archivo")
    print("3. Agregar nota")
    print("4. Reescribir archivo")
    print("5. Salir")

    print("Es necesario crear el archivo antes de leerlo o agregar notas.")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_archivo_notas()
    elif opcion == "2":
        leer_archivo_notas()
    elif opcion == "3":
        agregar_nota()
    elif opcion == "4":
        reescribir_archivo_notas()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")

#Ejercicio 2
def crear_archivo_helados():
    with open("heladeria.csv", "w") as archivo:
        archivo.write("Dulce de leche,1000,si\n")
        archivo.write("Chocolate,900,si\n")
        archivo.write("Vainilla,700,no\n")
    print("Archivo de helados creado con datos iniciales.")

def leer_archivo_helados():
    with open("heladeria.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            nombre, precio, disponible = linea.split(",")
            print(f"Producto: {nombre} | Precio: {precio} | Disponible: {disponible}")

def agregar_sabor_helado():
    with open("heladeria.csv", "a") as archivo:
        nombre = input("Ingrese el nombre del helado: ")
        precio = input("Ingrese el precio del helado: ")
        disponible = input("¿Está disponible? (si/no): ")
        archivo.write(f"{nombre},{precio},{disponible}\n")

def escribir_nuevos_helados():
    with open("heladeria.csv", "a") as archivo:
        archivo.write("Frutilla,800,si\n")
        archivo.write("Pistacho,900,no\n")
        archivo.write("Banana,700,si\n")
    print("Archivo de helados escrito con nuevos datos.")
    with open("heladeria.csv", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            nombre, precio, disponible = linea.split(",")
            print(f"Producto: {nombre} | Precio: {precio} | Disponible: {disponible}")

while True:
    print("--------------------------------")
    print("Menu de opciones para Heladeria:")
    print("--------------------------------")
    print("1. Crear archivo")
    print("2. Leer archivo")
    print("3. Agregar sabor de helado")
    print("4. Reescribir con nuevos helados")
    print("5. Salir")

    print("Es necesario crear el archivo antes de leerlo o agregar sabores.")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_archivo_helados()
    elif opcion == "2":
        leer_archivo_helados()
    elif opcion == "3":
        agregar_sabor_helado()
    elif opcion == "4":
        escribir_nuevos_helados()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")

#Ejercicio 3
def crear_archivo_cine():
    with open("cine.csv", "w") as archivo:
        archivo.write("Matrix,150,si\n")
        archivo.write("El Senor de los Anillos,180,si\n")
        archivo.write("Interstellar,170,no\n")
    print("Archivo de cine creado con datos iniciales.")

def mostrar_contenido_archivo_cine():
    with open("cine.csv", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo cine.csv:")
        print(contenido)

def agregar_pelicula():
    with open("cine.csv", "a") as archivo:
        nombre = input("Ingrese el nombre de la película: ")
        taquillas = input("Ingrese la cantidad de taquillas: ")
        disponible = input("¿Está disponible? (si/no): ")
        archivo.write(f"{nombre},{taquillas},{disponible}\n")

def mostrar_contenido_actualizado_cine():
    with open("cine.csv", "r") as archivo:
        contenido = archivo.read()
        print("Contenido actualizado del archivo cine.csv:")
        print(contenido)

while True:
    print("------------------------------")
    print("Menu de opciones para el cine:")
    print("------------------------------")
    print("1. Crear archivo")
    print("2. Mostrar contenido del archivo")
    print("3. Agregar película")
    print("4. Mostrar contenido actualizado")
    print("5. Salir")

    print("Es necesario crear el archivo antes de leerlo o agregar películas.")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_archivo_cine()
    elif opcion == "2":
        mostrar_contenido_archivo_cine()
    elif opcion == "3":
        agregar_pelicula()
    elif opcion == "4":
        mostrar_contenido_actualizado_cine()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")

#Ejercicio 4
def crear_archivo_pacientes():
    with open("pacientes.csv", "w") as archivo:
        archivo.write("Juan,30,no\n")
        archivo.write("Maria,25,si\n")
        archivo.write("Luis,40,si\n")
    print("Archivo de pacientes creado con datos iniciales.")

def mostrar_contenido_archivo_pacientes():
    with open("pacientes.csv", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo pacientes.csv:")
        print(contenido)

def agregar_paciente():
    with open("pacientes.csv", "a") as archivo:
        nombre = input("Ingrese el nombre del paciente: ")
        edad = input("Ingrese la edad del paciente: ")
        turno = input("¿Tiene turno? (si/no): ")
        archivo.write(f"{nombre},{edad},{turno}\n")
        print("Paciente agregado correctamente")

def mostrar_contenido_actualizado_pacientes():
    with open("pacientes.csv", "r") as archivo:
        contenido = archivo.read()
        print("Contenido actualizado del archivo pacientes.csv:")
        print(contenido)

while True:
    print("-------------------------------")
    print("Menu de opciones para Pacientes:")
    print("-------------------------------")
    print("1. Crear archivo")
    print("2. Mostrar contenido del archivo")
    print("3. Agregar paciente")
    print("4. Mostrar contenido actualizado")
    print("5. Salir")

    print("Es necesario crear el archivo antes de leerlo o agregar pacientes.")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_archivo_pacientes()
    elif opcion == "2":
        mostrar_contenido_archivo_pacientes()
    elif opcion == "3":
        agregar_paciente()
    elif opcion == "4":
        mostrar_contenido_actualizado_pacientes()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")

#Ejercicio 5
def crear_archivo_excursiones():
    with open("excursiones.csv", "w") as archivo:
        archivo.write("Bariloche,2000,si\n")
        archivo.write("Cataratas,1500,no\n")
        archivo.write("Mendoza,1800,si\n")
    print("Archivo de excursiones creado con datos iniciales.")

def mostrar_contenido_archivo_excursiones():
    with open("excursiones.csv", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo excursiones.csv:")
        print(contenido)

def agregar_excursion():
    with open("excursiones.csv", "a") as archivo:
        nombre = input("Ingrese el nombre del destino: ")
        precio = input("Ingrese el precio: ")
        disponible = input("¿Está disponible? (si/no): ")
        archivo.write(f"{nombre},{precio},{disponible}\n")
        print("Excursión agregada correctamente")

def escsribir_nueva_linea_excursion():
    with open("excursiones.csv", "a") as archivo:
        archivo.write("Santiago,2200,si\n")
        archivo.write("Salta,1600,no\n")
        archivo.write("Cordoba,1700,si\n")
    print("Archivo de excursiones escrito con nuevas líneas.")

def mostrar_contenido_actualizado_excursiones():
    with open("excursiones.csv", "r") as archivo:
        contenido = archivo.read()
        print("Contenido actualizado del archivo excursiones.csv:")
        print(contenido)

while True:
    print("---------------------------------")
    print("Menu de opciones para Excursiones:")
    print("---------------------------------")
    print("1. Crear archivo")
    print("2. Mostrar contenido del archivo")
    print("3. Agregar excursión")
    print("4. Escribir nuevas líneas de excursiones")
    print("5. Mostrar contenido actualizado")
    print("6. Salir")

    print("Es necesario crear el archivo antes de leerlo o agregar películas.")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_archivo_excursiones()
    elif opcion == "2":
        mostrar_contenido_archivo_excursiones()
    elif opcion == "3":
        agregar_excursion()
    elif opcion == "4":
        escsribir_nueva_linea_excursion()
    elif opcion == "5":
        mostrar_contenido_actualizado_excursiones()
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")