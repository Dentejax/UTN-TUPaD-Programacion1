#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
elif edad >= 0 and edad <= 18:
    print("Es menor de edad")
else:
    print("Ingrese una edad valida")
#Ejercicio 2
nota = float(input("Ingrese su calificacion: "))
if nota >= 6 and nota <= 10:
    print("Aprobado")
elif nota >= 0 and nota <= 5:
    print("Desaprobado")
else:
    print("ingrese una calificcion valida")
#Ejercicio 3
num = int(input("Ingree un numero: "))
if (num % 2) == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")
#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad < 12:
    print("Es niño")
elif edad >= 12 and edad < 18:
    print("Es adolescente")
elif edad >= 18 and edad < 30:
    print("Es adulto joven")
elif edad >= 30:
    print("Es adulto")
else:
    print("ingrese una edad valida")
#Ejercicio 5
contraseña = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print( "Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#Ejercicio 6
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if moda > mediana > media:
    print("Sesgo positivo o a la derecha")
elif moda < mediana < media:
    print("Sesgo negativo o a la izquierda")
elif moda == mediana == media:
    print("Sin sesgo")
else:
    print("No fue pocible determinar el Sesgo")
#Ejercicio 7
palabra = input("Ingrese una palabra: ")
if palabra[-1] in "aeiou":
    print(palabra,"!")
else:
    print(palabra)
#Ejercicio 8
nombre = input("Ingrese su nombre: ")
print("Que quiere realizar?")
print("1) Convertir todas las letras a mayusculas")
print("2) Convertir todas las letras a minuculas")
print("3) Convertir las primeras letras a mayuscula")
opcion = int(input("Ingrese el numero para realizar la operacion: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Las opciones solo son 1, 2 o 3")
#Ejercicio 9
magnitud = float(input("Ingrese la magnitud de un terremoto en escala Richter: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
#Ejercicio 10
hemisferio = input("Ingrese el emisferio N (Norte), S (Sur): ")
mes = int(input("Ingrese el mes del año(en numeros): "))
dia = int(input("Ingrese el dia del año(en numeros): "))
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        print("Estás en Invierno.")
    else:
        print("Estás en Verano.")
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        print("Estás en Primavera.")
    else:
        print("Estás en Otoño.")
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        print("Estás en Verano.")
    else:
        print("Estás en Invierno.")
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        print("Estás en Otoño.")
    else:
        print("Estás en Primavera.")
else:
    print("Fecha inválida.")