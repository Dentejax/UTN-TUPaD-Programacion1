#Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        
num = int(input("Ingrese un número entero positivo: "))
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}")

print("-------------------------------")

#Ejercicio 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Ingrese un número entero positivo: "))
print(f"Numero de Fibonacci: {fibonacci(num)}")

print("-------------------------------")

#Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente -1)

base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))
print(f"{base} ^ {exponente} = {potencia(base, exponente)}")

print("-------------------------------")

#Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
num = int(input("Ingrese un numero para convertio a binario: "))
print(f"El binario de {num} es: {decimal_a_binario(num)}")

print("-------------------------------")

#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    
palabra = input("Ingrese una palabra: ").strip()
if es_palindromo(palabra):
    print(f"La palabra {palabra} es un palíndromo")
else:
    print(f"La palabra {palabra} no es un palíndromo")

print("-------------------------------")

#Ejercicio 6
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

num = int(input("Ingrese un número entero positivo: "))
print(f"Suma de todos los dígitos: {suma_digitos(num)}")

print("-------------------------------")

#Ejercicio 7
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)
    
num = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print(f"Total de bloques en la pirámide: {contar_bloques(num)}")

print("-------------------------------")

#Ejercicio 8
def contar_digito(numero, digito, contador=0):
    if numero == 0:
        return contador
    else:
        ultimo_digito = numero % 10
        if ultimo_digito == digito:
            contador += 1
        return contar_digito(numero // 10, digito, contador)

num = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a contar: "))
print(f"El dígito {digito} aparece {contar_digito(num, digito)} veces en el número {num}")