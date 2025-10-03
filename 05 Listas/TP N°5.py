#Ejercicio 1
lista_multiplos_4 = list(range(0, 100, 4))
print(lista_multiplos_4)
#Ejercicio 2
numeros = [1, 2, 3, 4, 5]
print(numeros[3])
#Ejercicio 3
lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("Mundo")
lista_vacia.append("Python")
print(lista_vacia)
#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)
#Ejercicio 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#Este codigo remueve el elemento mas grande de la lista numeros en este caso el 22
#Ejercicio 6
numeros = [10, 15, 20, 25, 30]
print(numeros[:2])
#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1:3] = ["coupé", "SUV"]
print(autos)
#Ejercicio 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)
#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)
#Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)