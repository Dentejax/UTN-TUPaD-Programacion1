#Ejercicio 1
compañeros = ["Agustin", "Joel", "Marcos", "David", "Mayra"]
print(f"Primer elemento: {compañeros[0]}")
print(f"Ultimo elemento: {compañeros[-1]}")

print("-------------------------------")

#Ejercicio 2
numeros = [52, 72, 35, 2, 48]
print(f"Antes: {numeros}")
numeros[2] = 99
print(f"Despues: {numeros}")

print("-------------------------------")

#Ejercicio 3
numeros = [10, 20, 30, 40, 50, 60, 70]
print(f"Primeros 3 elementos: {numeros[:3]}")
print(f"Ultimos 2 elementos: {numeros[5:]}")
print(f"Elementos del índice 2 al 4: {numeros[2:5]}")

print("-------------------------------")

#Ejercicio 4
frutas = ["manzana", "banana", "pera"]
print(f"Antes: {frutas}")
frutas.append("uva")
añadir_fruta = input("Ingrese una fruta: ")
frutas.append(añadir_fruta)
frutas.remove("banana")
print(f"Despues: {frutas}")

print("-------------------------------")

#Ejercicio 5
numeros = [3, 6, 9, 12, 15]
suma = 0
for i in range(len(numeros)):
    suma += numeros[i]
print(f"Suma de los elementos de la lista: {suma}")

print("-------------------------------")

#Ejercicio 6
matriz = [[1, 2, 3], [4, 5, 6]]
print(f"Elemento [1][2]: {matriz[1][2]}")
print(f"Elemento [0][0]: {matriz[0][0]}")
print(f"Elemento [0][2]: {matriz[0][2]}")