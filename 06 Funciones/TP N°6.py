#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo")
imprimir_hola_mundo()
#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)
#Ejercicio 3
def  informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
#Ejercicio 4
import math
def calcular_area_circulo(radio):
    return math.pi * radio**2
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
radio = float(input("Ingrese el radio del circulo: "))
print("El area del circulo es:", calcular_area_circulo(radio))
print("El perimetro del circulo es:", calcular_perimetro_circulo(radio))
#Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600
segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"La cantidad de horas es: {segundos_a_horas(segundos)}")
#Ejercicio 6
def  tabla_multiplicar(numero):
    for i in range(10):
        resultado = 0
        resultado = numero * (i + 1)
        print(f"{numero} x {i} = {resultado}")
numero = int(input("Ingrese un numero para mostrar la tabla de multiplicar: "))
tabla_multiplicar(numero)
#Ejercicio 7
def operaciones_basicas(a, b):
    resultado = 0
    resultado = a + b
    print(f"{a} + {b} = {resultado}")
    resultado = a - b
    print(f"{a} - {b} = {resultado}")
    resultado = a * b
    print(f"{a} x {b} = {resultado}")
    resultado = a / b
    print(f"{a} / {b} = {resultado}")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
operaciones_basicas(num1, num2)
#Ejrcicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
print("Por favor ingrese su peso y altura para calcular el Indice de Masa Croporal(IMC)")
peso = float(input("ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"El indice de Masa Corporal(IMC) es: {calcular_imc(peso, altura)}")
#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return celsius * 2 + 30
celsius = float(input("Ingrese una temperatura en Celsius: "))
print(f"La tempratura {celsius} en celsius, es {celsius_a_fahrenheit(celsius)} en Fahrenheit.")
#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
print("Ingresar 3 numeros para calcular l promedio")
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))
num3 = float(input("Ingrese otro numero: "))
print(f"Promedio: {calcular_promedio(num1, num2, num3)}")