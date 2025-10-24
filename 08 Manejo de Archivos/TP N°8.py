#Ejercicio 1
ruta_de_acceso = r"C:\Users\franc\OneDrive\Escritorio\UTN\Programacion 1\UTN-TUPaD-Programacion1\08 Manejo de Archivos\productos.txt"
#La ruta de acceeso debe ser modificada segun la ubicacion del archivo en su computadora
#Y fue asi porque por alguna razon no admitia el nombre del archivo, osea aparecia un error aunque estubiera en la misma carpeta
with open(ruta_de_acceso, "r") as archivo:
    #Ejercicio 2
    for linea in archivo:
        linea = linea.strip()

        if not linea:
            continue

        partes = linea.split(",")

        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]

        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
#Ejercicio 3
productos = []
with open(ruta_de_acceso, "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split(",")
        nombre = partes[0].lower()
        precio = float(partes[1])
        cantidad = int(partes[2])
        productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

with open(ruta_de_acceso, "a") as archivo:
    nombre = input("Ingrese el nombre del producto: ").lower()
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese el cantidad del producto: "))
    archivo.write(f"{nombre},{precio},{cantidad}\n")
    nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(nuevo)
#Ejercicio 5
with open(ruta_de_acceso, "r") as archivo:
    busqueda = input("Ingrese el nombre del producto a buscar: ").lower()
    encontrado = False
    for linea in archivo:
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split(",")
        nombre = partes[0].lower()
        precio = partes[1]
        cantidad = partes[2]
        if nombre == busqueda:
            print(f"Producto: {partes[0]} | Precio: {precio} | Cantidad: {cantidad}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")
#Ejercicio 6
with open(ruta_de_acceso, "w") as archivo:
    for p in productos:
        nombre = p.get("nombre")
        precio = str(p.get("precio"))
        cantidad = str(p.get("cantidad"))
        archivo.write(f"{nombre},{precio},{cantidad}\n")
print("Archivo actualizado correctamente.")
