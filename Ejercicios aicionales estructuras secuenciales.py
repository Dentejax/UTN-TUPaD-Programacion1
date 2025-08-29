#Ejercicio 1
ancho = float(input("Ingrese el ancho de un rectangulo: "))
alto = float(input("Ingrese el ancho de un alto: "))
area = ancho * alto
perimetro = (ancho * 2) + (alto * 2)
print("El area el rectangulo es: ",area)
print("El perimetro el rectangulo es: ",perimetro)
#Ejercicio 2
celsius = float(input("Ingrese la temperatura en Celsius: "))
Fahrenhei = (celsius * 1.8) + 32
print("Los graos equivalentes e Celsius a Fahrenhei es: ",Fahrenhei)
#Ejercicio 3
a = True
b = False
print(a and b)
print(a or b)
print(not a, not b)
#Ejercicio 4
a = 5
b = 3
c = a + b
a = 2
print(c)
# Lin  |   a   |        b        |        c        |
# 19(1)|   5   | sin inicializar | sin inicializar |          
# 20(2)|   5   |        3        | sin inicializar |           
# 21(3)|   5   |        3        |        8        |
# 22(4)|   2   |        3        |        8        |
# 23(5)|   2   |        3        |        8        |
#El programa imprime por pantalla el valor de c osea 8
#Ejercicio 5
num = int(input("Ingrese un numero: "))
cuadrado = num ** 2
print("Elevado al cuadrado: ", cuadrado)
#Ejercicio 6
x = 10
y = 20
print("Antes, x :", x)
print("Antes, y :", y)
y = y - x
x = x + y
print("Despues, x: ", x)
print("Despues, y: ", y)
#Ejercicio 7
altura = float(input("Ingrese su altura en metros: "))
peso_kg = float(input("Ingrese su peso en kg: "))
indice_de_masa_corporal = peso_kg / altura ** 2
print("Su indice de masa corporal es: ",indice_de_masa_corporal)
#Ejercicio 8
nombre = input("Ingresa tu nombre completo: ")
nombre_sin_espacios = nombre.replace(" ", "")
primeras_tres = nombre[:3]
alternado = "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(nombre))
print("Cantidad de letra (sin espacios): ", len(nombre_sin_espacios))
print("Primera 3 letras: ", primeras_tres)
print("Nombre con mayusculas y minusculas alternadas: ", alternado)
#Ejercicio 9
a = 7.5
b = 3.2
print("Suma: ", a + b)
print("Redondeo de divicion: ", round(a / b))
print("Potenciacion: ", a ** b)
#Ejercicio 10
precio_original = float(input("Ingrese el precio original: "))
descuento = int(input("Ingrese el porcentaje de descuento: "))
precio_final = precio_original * (1 - (descuento / 100))
print("El precio con descuento es: ", precio_final)