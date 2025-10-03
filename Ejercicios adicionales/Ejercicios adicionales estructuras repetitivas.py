#Ejercicio 1
palabra = input("Ingrese una plabra: ")
for i in range(11):
    print(palabra)
#Ejercicio 2
year = int(input("Ingrese su edad: "))
for i in range(year):
    print("Cumpliste el año: ", i + 1)
#Ejercicio 3
numero = int(input("Ingrese el tamaño del triangulo: "))
for i in range(numero + 1):
    print ("*" * i)
#Ejercicio 4
for i in range(10):
    for y in range(11):
        print((i + 1), " x ", y, " = ", (i + 1) * y)
#Ejercicio 5
contrasena_correcta = "franco123"
while True:
    contrasena = input("Ingrese su contraseña: ")
    if contrasena == contrasena_correcta:
        print("Contraseña correcta") 
        break
    else:
        print("Contraseña incorrecta vuelva a intentar")
#Ejercicio 6
acumulador = ""
while True:
    palabra = input("Escribe algo (o 'salir' para terminar): ")
    if palabra.lower() == "salir":
        break
    if acumulador:
        acumulador += " " + palabra
    else:
        acumulador = palabra
    print(acumulador)
#Ejercicio 7
for i in range(2, 21, 2):
    print(i)
#Ejercicio 8
for i in range(100):
    i += 1
    if (i % 3) == 0 and (i % 5) == 0:
        print("FizzBuzz")
    elif (i % 3) == 0:
        print("Fizz")
    elif (i % 5) == 0:
        print("Buzz")
    else:
        print(i)
#Ejercicio 9
suma = 0.0
for i in range(10):
    numero = float(input("Ingrese un numero: "))
    if i >= 5:
        suma += numero
print("La suma de los ultimos 5 numeros es: ", suma)
#Ejercicio 10
# t = triangulo
t_equilatero = 0.0
t_isosceles = 0.0
t_escaleno = 0.0
while True:
    lado1 = float(input("Ingrese el primer lado del traingulo: "))
    lado2 = float(input("Ingrese el segundo lado del traingulo: "))
    lado3 = float(input("Ingrese el tercer lado del traingulo: "))
    if lado1 > 0 and lado2 > 0 and lado3 > 0:
     if lado1 == lado2 and lado2 == lado3:
       t_equilatero += 1
     elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
       t_isosceles += 1
     else:
       t_escaleno +=1
     while True:
       otra_operacion = input("Desea ver otro triangulo? S (Si), o N (No): ").strip().lower()#.strip para eliminar espacios y .lower para simplificar una parte del codigo
       if otra_operacion in ("s", "n"):
        break
       print("Las opciones solo son S o N")
     if otra_operacion == "n":
       break
    else:
      print("Los lados solo deben de ser positivos")
print("Triangulos equilateros: ", t_equilatero)
print("Triangulos isosceles: ", t_isosceles)
print("Triangulos escalenos: ", t_escaleno)