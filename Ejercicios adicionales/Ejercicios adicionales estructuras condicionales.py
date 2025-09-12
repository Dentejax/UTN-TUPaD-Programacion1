#Ejercicio 1
#1. Lee el siguiente código y explica qué hace:
contrasena_correcta = "programacion1" 
contrasena_usuario = input("Introduce la contraseña: ") 
if contrasena_usuario == contrasena_correcta: 
 print("Contraseña correcta. Bienvenido.") 
else: 
 print("Contraseña incorrecta. Intenta de nuevo.") 
#Este codigo compara la contraseña ingresada por un usuario y si es correcta el usuario entra, si no, no
#Ejercicio 2
letra = input("Ingrese una letra: ")
if letra in ["a", "e", "i", "o", "u"] or letra in ["A", "E", "I", "O", "U"]:
 print("La letra ingresada es una vocal")
else:
 print("La letra ingresada no es una vocal")
#Ejercicio 3
numero = float(input("Ingrese un numero: "))
if numero > 0:
 print("El numero es positivo")
elif numero < 0:
 print("El numero es negativo")
else:
 print("El numero es cero")
#Ejercicio 4
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))
if num1 > num2:
 print("El primer numero ingresado es mayor")
elif num1 < num2:
 print("El primer numero ingresado es menor")
else:
 print("Los numeros ingresados son iguales")
#Ejercicio 5
temperatura = float(input("Ingrese la temperatura en °C: "))
if temperatura <= 10:
 print("Hace frio")
elif temperatura > 10 and temperatura <= 25:
 print("Esta templado")
else:
 print("Hace calor")
#Ejercicio 6
year = int(input("Ingrese un año: "))
if year > 0:
 if ((year % 4) == 0 and (year % 100) != 0) or (year % 400) == 0:
  print("Se ingreso un año bisiesto")
 else:
  print("Se ingreso un año no bissiesto")
else:
 print("años negativos no")
#Ejercicio 7
palabra = input("Ingrese una palabra: ")
if not palabra.endswith("."):
 palabra += "."
print("Resultado: ", palabra)
#Ejercicio 8
contrasena =input("Cree una contraseña: ")
if len(contrasena) <= 20 and len(contrasena) >= 8:
 if contrasena.isupper():
  if contrasena.isdigit():
   print("¡Felicitaciones! Creaste tu contraseña.")
  else:
   print("La contraseña no es segura.")
 else:
  print("La contraseña no es segura.")
else:
 print("La contraseña no es segura.")
#Ejercicio 9
#vesion mejorada
contrasena =input("Cree una contraseña: ")
if 8 >= len(contrasena) <= 20:
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)
    if tiene_mayuscula and tiene_numero:
        print("¡Felicitaciones! Creaste tu contraseña.")
    elif not tiene_mayuscula:
        print("La contraseña debe contener al menos una mayúscula.")
    elif not tiene_numero:
        print("La contraseña debe contener al menos un número.")
else:
    if len(contrasena) < 8:
        print("La contraseña no es segura. Debe tener al menos 8 caracteres.")
    else:
        print("No más de 20 caracteres.")
#Ejercicio 10
jugador1 = input("Jugador 1: Piedra, Papel o Tijera?: ")
jugador2 = input("Jugador 2: Piedra, Papel o Tijera?: ")
if (jugador1 == "Piedra" or jugador1 == "piedra") and (jugador2 == "Piedra" or jugador2 == "piedra"):
 print("Empate")
elif (jugador1 == "Papel" or jugador1 == "papel") and (jugador2 == "Papel" or jugador2 == "papel"):
 print("Empate")
elif (jugador1 == "Tijera" or jugador1 == "tijera") and (jugador2 == "Tijera" or jugador2 == "tijera"):
 print("Empate")
elif (jugador1 == "Piedra" or jugador1 == "piedra") and (jugador2 == "Papel" or jugador2 == "papel"):
 print("Gana jugador 2")
elif (jugador1 == "Piedra" or jugador1 == "piedra") and (jugador2 == "Tijera" or jugador2 == "tijera"):
 print("Gana jugador 1")
elif (jugador1 == "Papel" or jugador1 == "papel") and (jugador2 == "Piedra" or jugador2 == "piedra"):
 print("Gana jugador 1")
elif (jugador1 == "Papel" or jugador1 == "papel") and (jugador2 == "Tijera" or jugador2 == "tijera"):
 print("Gana jugador 2")
elif (jugador1 == "Tijera" or jugador1 == "tijera") and (jugador2 == "Piedra" or jugador2 == "piedra"):
 print("Gana jugador 2")
elif (jugador1 == "Tijera" or jugador1 == "tijera") and (jugador2 == "Papel" or jugador2 == "papel"):
 print("Gana jugador 1")
else:
 print("Es piedra, Papel o Tijera")