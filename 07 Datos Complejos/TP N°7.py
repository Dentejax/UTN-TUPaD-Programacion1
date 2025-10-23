#Ejercicio 1
precios_frutas = {"Banana":1200, "Ananá":2500, "Melon":3000, "Uva":1450}
print(f"Antes: {precios_frutas}")
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(f"Despues: {precios_frutas}")

print("------------------")

#Ejercicio 2
print(f"Antes: {precios_frutas}")
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800
print(f"Despues: {precios_frutas}")

print("------------------")

#Ejercicio 3
frutas = precios_frutas.keys()
print(f"Lista de frutas: {frutas}")

print("------------------")

#Ejercicio 4
numeros_personas = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    telefono = int(input(f"Ingrese el numero telefonico de {nombre}: "))
    numeros_personas[nombre] = telefono
busqueda_nombre = input("Ingrese el nombre de una persona para consultar su numero telefonico: ")
if busqueda_nombre in numeros_personas:
    print(f"Nombre: {busqueda_nombre}")
    print(f"Numero telefonico: {numeros_personas[busqueda_nombre]}")
else:
    print(f"La persona {busqueda_nombre} no existe dentro de los contactos")

print("------------------")

#Ejercicio 5
frase = input("Ingrese una frase: ")
palabras_unicas = set(frase.split())
print(f"Palabras únicas: {palabras_unicas}")
palabras_lista = frase.split()
contador_palabras = {}
for palabra in palabras_lista:
    contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1
print(f"Frecuencia de palabras: {contador_palabras}")

print("------------------")

#Ejercicio 6
alumnos_notas = {}
for i in range(3):
    nombre_alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1} de {nombre_alumno}: "))
        notas.append(nota)
    alumnos_notas[nombre_alumno] = tuple(notas)
promedios = {}
for alumno, notas in alumnos_notas.items():
    suma = 0
    for i in range(len(notas)):
        suma += notas[i]
    promedio = suma / len(notas)
    promedios[alumno] = promedio
for clave, valor in promedios.items():
    print(f"El promedio de {clave} es {valor}")

print("------------------")

#Ejercicio 7
parcial1 = {'Ana', 'Beto', 'Carla', 'Diego'}
parcial2 = {'Beto', 'Carla', 'Eva', 'Federico'}
ambos = parcial1.intersection(parcial2)
al_menos_uno = parcial1.union(parcial2)
solo_uno = al_menos_uno.difference(ambos)
print("Aprobados en ambos parciales:", ambos)
print("Aprobados en solo uno de los dos:", solo_uno)
print("Aprobados en al menos un parcial:", al_menos_uno)

print("------------------")

#Ejercicio 8
#stock inicial
stock_productos = {
    "Fideos": 150,
    "Arroz": 130,
    "Salsas": 75,
    "Jabon": 90
}
while True:
    print("--- Gestor de Stock ---")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    opcion = int(input("Seleccione una opción (1-4): "))
    if opcion == 1:
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in stock_productos:
            print(f"El stock de {producto} es {stock_productos[producto]}")
        else:
            print(f"El producto {producto} no existe")
    elif opcion == 2:
        producto = input("Ingrese el nombre del producto a actualizar: ")
        if producto in stock_productos:
            cantidad = int(input(f"Ingrese la cantidad a agregar al stock de {producto}: "))
            stock_productos[producto] += cantidad
            print(f"Stock actualizado de {producto}: {stock_productos[producto]}")
        else:
            print(f"El producto {producto} no existe")
    elif opcion == 3:
        producto = input("Ingrese el nombre del nuevo producto: ")
        cantidad = int(input(f"Ingrese la cantidad inicial de {producto}: "))
        stock_productos[producto] = cantidad
        print(f"Producto {producto} agregado con stock {cantidad}")
    elif opcion == 4:
        print("Saliendo del gestor de stock.")
        break
    else:
        print("Opción inválida.")

print("------------------")

#Ejercicio 9
agenda = {}
while True:
    print("Agenda de evento: ")
    print("1. Ingresar eventos")
    print("2. consultar que actividad hay en cierto día y hora")
    print("3. Salir")
    opcion = int(input("Seleccione una opción (1-3): "))
    if opcion == 1:
        dia = input("Ingrese el día del evento (por ejemplo, lunes): ")
        hora = input("Ingrese la hora del evento (por ejemplo, 10:00): ")
        evento = input("Ingrese el nombre del evento: ")
        agenda[(dia, hora)] = evento
        print("Evento agregado a la agenda.")
    elif opcion == 2:
        dia = input("Ingrese el día a consultar: ")
        hora = input("Ingrese la hora a consultar: ")
        clave = (dia, hora)
        if clave in agenda:
            print(f"En {dia} a las {hora} hay: {agenda[clave]}")
        else:
            print(f"No hay eventos programados para {dia} a las {hora}.")
    elif opcion == 3:
        print("Saliendo de la agenda.")
        break
    else:
        print("Opción inválida.")
print("------------------")

#Ejercicio 10
paises = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Japón': 'Tokio',
    'Brasil': 'Brasilia'
}
capitales = {capital: pais for pais, capital in paises.items()}
print(f"Antes: {paises}")
print(f"Después: {capitales}")