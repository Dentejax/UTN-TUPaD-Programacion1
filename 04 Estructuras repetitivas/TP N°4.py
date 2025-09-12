#Ejercicio 1
for i in range(101):
    print(i)
#Ejercicio 2
numero = input("Ingrese un numero: ")
digitos = len(numero)
print("La cantidad de dijitos es: ", digitos)
#Ejercicio 3
resultado = 0
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num1 += 1
for i in range(num1,num2):
    resultado += i
num1 -= 1
print("La suma de los numeros entre", num1 ," y ", num2 ," es: ", resultado)
#Ejercicio 4
numero = 1
while numero != 0:
    if numero == 1:
        numero = 0
    numero = int(input("Ingrese un numero para sumar: "))
    print  ("Si quiere terminar con las sumas ingrese 0 (Cero)")
    resultado += numero
print("El resultado de la suma de todos los numeros es: ", resultado)
#Ejercicio 5
import random
num_aleatorio = random.randint(0, 9)
num = 10
intentos = 0
while num == 10:
    num = int(input("Ingresa un numero entre 0 y 9: "))
    intentos += 1
    if num < 0:
        print("No puede ser un numero menor a 0")
    elif num > 9:
        print("No puede ser un numero mayor a 9")
    elif num == num_aleatorio:
        break
    num = 10
print("FELICIDADES!")
print("La cantidad de intentos fueron: ", intentos)
#Ejercicio 6
for i in range(101):
    if (i % 2) == 0:
        print(i)
#Ejercicio 7
limite = int(input("Ingrese un numero para sumar todos los numeros entre 0 y el numero que ingresaras: "))
if limite < 0:
    print("Tiene que ser un numero positivo")
for i in range(limite):
    resultado += i
print ("El resultado es: ", resultado)
#Ejercicio 8
es_par = 0
es_impar = 0
positivos = 0
negativos = 0
cero = 0
print("Advertencia tendra que ingresar 100 nuumeros")
for i in range(10):
    num = int(input("Ingrese un numero: "))
    if (num % 2) == 0:
        es_par += 1
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
    elif (num % 2) != 0:
        es_impar += 1
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
print("Pares: ", es_par)
print("Impares: ", es_impar)
print("Positivos: ", positivos)
print("Negativos: ", negativos)
#Ejercicio 9
media = 0
temp = 0
print("Advertencia tendra que ingresar 100 nuumeros")
for i in range(10):
    num = int(input("Ingrese un numero entero: "))
    temp += num
    media = temp / 10
print("Media de los 100 numeros:", media)
#Ejercicio 10
digito = 0
inverso = 0
num = int(input("Ingrese un numero entero para invertirlo: "))
while num != 0:
    digito = num % 10
    num = num._round(num / 10)
    inverso *= 10 + digito
print("El numero inverso: ", inverso)
#Mientras num <> 0 Hacer
#		digito = num mod 10
#		num = trunc(num / 10)
#		inverso = inverso * 10 + digito
#	FinMientras	
#	Escribir "El numero inverso es: ", inverso

#Acordate de cambiar los 10 por 100 en el 8 y 9