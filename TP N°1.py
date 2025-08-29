#Ejercicio 1
print("Hola Mundo!")
#Ejercicio 2
nombre = input("Ingresa tu nombre: ")
print("Hola",nombre,"!")
#Ejercicio 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa yu apellido: ")
edad = input("Ingresa tu edad: ")
lugar_de_residencia = input("Ingresa tu lugar de residencia: ")
print("Soy",nombre,apellido,", tengo", edad, "años y vivo en", lugar_de_residencia)
#Ejercicio 4
import math
radio = float(input("Ingrese el raio de un circulo: "))
area = radio * math.pi ** 2
perimetro = 2 * math.pi * radio
print("El area el circulo es: ",area)
print("El perimetro el circulo es: ",perimetro)
#Ejercicio 5
segundos = int(input("Ingrese una cantidad en segundos: "))
minutos = segundos // 60
horas = minutos // 60
print("Los segundos equivalentes a horas es: ",horas)
#Ejercicio 6
num_multiplicado = int(input("Ingrese un número: "))
num1 = num_multiplicado * 1
num2 = num_multiplicado * 2
num3 = num_multiplicado * 3
num4 = num_multiplicado * 4
num5 = num_multiplicado * 5
num6 = num_multiplicado * 6
num7 = num_multiplicado * 7
num8 = num_multiplicado * 8
num9 = num_multiplicado * 9
num10 = num_multiplicado * 10
print(num_multiplicado, " x 1 = ", num1)
print(num_multiplicado, " x 2 = ", num2)
print(num_multiplicado, " x 3 = ", num3)
print(num_multiplicado, " x 4 = ", num4)
print(num_multiplicado, " x 5 = ", num5)
print(num_multiplicado, " x 6 = ", num6)
print(num_multiplicado, " x 7 = ", num7)
print(num_multiplicado, " x 8 = ", num8)
print(num_multiplicado, " x 9 = ", num9)
print(num_multiplicado, " x 10 = ", num10)
#Ejercicio 7
num1 = int(input("Ingresa un número distinto a 0: "))
num2 = int(input("Ingresa otro número distinto a 0: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 // num2
print (num1, " + ", num2, " = ", suma)
print (num1, " - ", num2, " = ", resta)
print (num1, " x ", num2, " = ", multiplicacion)
print (num1, " / ", num2, " = ", division)
#Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso_kg = float(input("Ingrese su peso en kg: "))
indice_de_masa_corporal = peso_kg / altura ** 2
print("Su indice de masa corporal es: ",indice_de_masa_corporal)
#Ejercicio 9
celsius = float(input("Ingrese la temperatura en Celsius: "))
Fahrenhei = (celsius * 1.8) + 32
print("Los graos equivalentes e Celsius a Fahrenhei es: ",Fahrenhei)
#Ejercicio 10
num1 = float(input("Ingresa número 1: "))
num2 = float(input("Ingresa número 2: "))
num3 = float(input("Ingresa número 3: "))
promedio = (num1 + num2 + num3) / 3
print("El promeio de los 3 números es: ", promedio)