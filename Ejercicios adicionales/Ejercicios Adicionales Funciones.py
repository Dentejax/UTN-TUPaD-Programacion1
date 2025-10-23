#Ejercicio 1
def  tabla_multiplicar(numero):
    for i in range(10):
        resultado = 0
        resultado = numero * (i + 1)
        print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un numero para mostrar la tabla de multiplicar: "))
tabla_multiplicar(numero)
#Ejrcicio 2
def suma_pares(numeros):
    suma_entre_pares = 0
    for i in range(len(numeros)):
        if (numeros[i] % 2) == 0:
            suma_entre_pares += numeros[i]
    return suma_entre_pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Suma entre los pares del 1 al 10 = {suma_pares(numeros)}")
#Ejrcicio 3
def area_rectángulo(longitud, ancho):
    area = longitud * ancho
    return area

def perímetro_rectángulo(longitud, ancho):
    perímetro = 2 * (longitud + ancho)
    return perímetro

longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))
print(f"El área del rectángulo es: {area_rectángulo(longitud, ancho)}")
print(f"El perímetro del rectángulo es: {perímetro_rectángulo(longitud, ancho)}")
#Ejrcicio 4
def convertir_temperatura(celsius, unidad_destino):
    if unidad_destino == "F" or unidad_destino == "f":
        return celsius * 9/5 + 32
    elif unidad_destino == "K" or unidad_destino == "k":
        return celsius + 273.15
    else:
        return None
    
celsius = float(input("Ingrese la temperatura en Celsius: "))
unidad_destino = input("Ingrese la unidad de destino Fahrenheit o Kelvin (F o K): ")
temperatura_convertida = convertir_temperatura(celsius, unidad_destino)
if temperatura_convertida is not None:
    print(f"La temperatura convertida es: {temperatura_convertida}")
else:
    print("Unidad de destino no es válida")
#Ejercicio 5
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Verificar si un número es primo")
numero = int(input("Ingrese un número entero positivo: "))
if es_primo(numero):
    print(f"El numero {numero} es un número primo.")
else:
    print(f"El numero {numero} no es un número primo.")
#Ejercicio 6
def promedio_calificaciones(notas):
    suma = 0
    if len(notas) == 0:
        return 0
    else:
        for i in range(len(notas)):
            suma += notas[i]
        promedio = suma / len(notas)
        return promedio
    
notas = []
num_notas = int(input("Ingrese la cantidad de calificaciones: "))
for i in range(num_notas):
    calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
    notas.append(calificacion)
print(f"El promedio de las calificaciones es: {promedio_calificaciones(notas)}")
#Ejercicio 7
def validar_entrada(numero):
    if numero < 0:
        return False
    return True

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)#Este ejercicio no le vi otra solucion para no usar recursividad

numero = int(input("Ingrese un número entero no negativo: "))
if validar_entrada(numero):
    print(f"El factorial de {numero} es: {factorial(numero)}")
else:
    print("Entrada no válida. Por favor, ingrese un número entero no negativo.")
#Ejercicio 8
def es_divisible(a, b):
    return a % b == 0

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if es_divisible(numero, i):
            return False
    return True

print("Verificar si un número es primo")
numero = int(input("Ingrese un número entero positivo: "))
if es_primo(numero):
    print(f"El numero {numero} es un número primo.")
else:
    print(f"El numero {numero} no es un número primo.")
#Ejercicio 9
def convertir_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def convertir_a_kelvin(celsius):
    return celsius + 273.15

def menu_conversion():
    print("Seleccione la unidad de conversión:")
    print("1. Fahrenheit")
    print("2. Kelvin")
    opcion = input("Ingrese 1 o 2: ")
    if opcion == "1":
        return convertir_a_fahrenheit(celsius)
    elif opcion == "2":
        return convertir_a_kelvin(celsius)
    else:
        return None
    
resultado = menu_conversion()
celsius = float(input("Ingrese la temperatura en Celsius: "))
if resultado is not None:
    print(f"La temperatura convertida es: {resultado}")
else:
    print("Opción no válida.")
#Ejercicio 10
def validar_dimensiones(longitud, ancho):
    return longitud > 0 and ancho > 0

def calcular_area(longitud, ancho):
    return longitud * ancho

def calcular_perimetro(longitud, ancho):
    return 2 * (longitud + ancho)

longitud = float(input("Ingrese la longitud del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))
if validar_dimensiones(longitud, ancho):
    print(f"Área: {calcular_area(longitud, ancho)}")
    print(f"Perímetro: {calcular_perimetro(longitud, ancho)}")
else:
    print("Dimensiones no válidas.")