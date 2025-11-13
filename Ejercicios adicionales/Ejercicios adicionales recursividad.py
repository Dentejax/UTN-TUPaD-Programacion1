#Ejercicio 1
def  suma_pares(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return n + suma_pares(n - 2)
    else:
        return suma_pares(n - 1)

num = int(input("Ingrese un numero: "))
print(f"La suma de los numeros pares desde 0 hasta {num} es: {suma_pares(num)}")

print("-------------------------------")

#Ejercicio 2
def contar_letra(palabra, letra, contador=0):
    if len(palabra) == 0:
        return contador
    else:
        ultima_letra = palabra[-1]
        if ultima_letra == letra:
            contador += 1
        return contar_letra(palabra[:-1], letra, contador)

palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra a buscar: ")
print(f"La letra {letra} aparece {contar_letra(palabra, letra)} veces en la palabra {palabra}")

print("-------------------------------")

#Ejercicio 3
def invertir_cadena(texto):
    if len(texto) == 0:
        return ""
    else:
        return texto[-1] + invertir_cadena(texto[:-1])

texto = input("Ingrese una cadena de texto para invertirla: ")
print(f"La cadena invertida es: {invertir_cadena(texto)}")

print("-------------------------------")

#Ejercicio 4
def contar_elementos(lista):
    if not lista:
        return 0
    else:
        return 1 + contar_elementos(lista[1:])
    
lista = [28, "hola", True, 3.14, "mundo", False]
print(f"La lista tiene {contar_elementos(lista)} elementos")

print("-------------------------------")

#Ejercicio 5
def contiene_letra(palabra, letra):
    if len(palabra) == 0:
        return False
    else:
        ultima_letra = palabra[-1]
        if ultima_letra == letra:
            return True
        return contiene_letra(palabra[:-1], letra)

palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra a buscar: ")
if contiene_letra(palabra, letra):
    print(f"La letra {letra} está dentro de la palabra {palabra}")
else:
    print(f"La letra {letra} no está dentro de la palabra {palabra}")

print("-------------------------------")

#Ejercicio 6
def multiplicar(a, b):
    if b == 0:
        return 0
    else:
        return a + multiplicar(a, b - 1)

num1 = int(input("Ingrese el primer número para multiplicar: "))
num2 = int(input("Ingrese el segundo número para multiplicar: "))
print(f"El resultado de la multiplicación es: {multiplicar(num1, num2)}")

print("-------------------------------")

#Ejercicio 7
def cuenta_regresiva(n):
    if n == 0:
        return 0
    else:
        print(n)
        return cuenta_regresiva(n - 1)

num = int(input("Ingrese el numero desde donde empezara la cuenta regresiva: "))
print(cuenta_regresiva(num))

print("-------------------------------")

#Ejercicio 8
def mostrar_letras(palabra):
    if len(palabra) == 0:
        return ""
    else:
        primera_letra = palabra[0]
        print(primera_letra)
        return mostrar_letras(palabra[1:])

palabra = input("Ingrese una palabra: ")
print(mostrar_letras(palabra))