# Crea el archivo CSV inicial con datos de países
def crear_archivo():
    with open("paises.csv", "w") as archivo:
        archivo.write("PAIS,POBLACION,SUPERFICIE,CONTINENTE\n")
        archivo.write("Argentina,45851378,2780400,America\n")
        archivo.write("España,49442844,505978,Europa\n")
        archivo.write("Japon,123103479,377969,Asia\n")
        archivo.write("Nueva Zelanda,5251899,268838,Oceania\n")
        archivo.write("Egipto,116538000,1002450,Africa\n")
    print("Archivo creado correctamente")

# Busca un país dentro del archivo (coincidencia parcial o exacta)
def buscar_pais():
    with open("paises.csv", "r") as archivo:
        pais_buscado = input("Ingrese el país a buscar: ").lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        encontrado = False

        for linea in archivo:
            pais, poblacion, superficie, continente = linea.strip().split(",")
            if pais == "PAIS":
                continue
            # Permite coincidencia parcial (por ejemplo, "arg" encuentra "Argentina")
            elif pais_buscado in pais.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u"):
                print(f"El país {pais} está dentro del archivo, y su contenido es:")
                print(f"""Población: {poblacion}
Superficie: {superficie}
Continente: {continente}""")
                encontrado = True

        if not encontrado:
            print(f"El país {pais_buscado} no está dentro del archivo")

# Filtra países según continente, rango de población o rango de superficie
def filtrar_paises():
    with open("paises.csv", "r") as archivo:
        next(archivo)
        lineas = []
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 4:
                lineas.append(partes)

    print("1. Filtrar por continente")
    print("2. Filtrar por población entre dos valores")
    print("3. Filtrar por superficie entre dos valores")
    opcion_filtro = input("Qué filtro desea realizar: ")

    if opcion_filtro == "1":
        cual_continente = input("En qué continente desea aplicar el filtro?: ").strip().lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        encontrado = False
        encontrados = False
        for pais, poblacion, superficie, continente in lineas:
            if continente.lower() == cual_continente:
                print(f"- {pais}: Población {poblacion}, Superficie {superficie}, Continente {continente}")
                encontrados = True
        if not encontrados:
            print("No se encontraron países en ese continente.")

    elif opcion_filtro == "2":
        try:
            valor_min = int(input("Ingrese el valor mínimo de población: "))
            valor_max = int(input("Ingrese el valor máximo de población: "))
        except ValueError:
            print("Debe ingresar valores numéricos.")
            return
        if valor_min > valor_max:
            print("El valor mínimo no puede ser mayor que el valor máximo.")
            return
        encontrados = False
        for pais, poblacion, superficie, continente in lineas:
            if valor_min <= int(poblacion) <= valor_max:
                print(f"- {pais}: Población {poblacion}, Superficie {superficie}, Continente {continente}")
                encontrados = True
        if not encontrados:
            print("No se encontraron países con población en ese rango.")

    elif opcion_filtro == "3":
        try:
            valor_min = float(input("Ingrese el valor mínimo de superficie: "))
            valor_max = float(input("Ingrese el valor máximo de superficie: "))
        except ValueError:
            print("Debe ingresar valores numéricos.")
            return
        if valor_min > valor_max:
            print("El valor mínimo no puede ser mayor que el valor máximo.")
            return
        encontrados = False
        for pais, poblacion, superficie, continente in lineas:
            if valor_min <= float(superficie) <= valor_max:
                print(f"- {pais}: Población {poblacion}, Superficie {superficie}, Continente {continente}")
                encontrados = True
        if not encontrados:
            print("No se encontraron países con superficie en ese rango.")
    else:
        print("Opción de filtro inválida.")

# Ordena los países por nombre, población o superficie (ascendente o descendente)
def ordenar_paises():
    with open("paises.csv", "r") as archivo:
        next(archivo)
        lineas = []
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 4:
                lineas.append(partes)

    print("1. Ordenar por nombre")
    print("2. Ordenar por población")
    print("3. Ordenar por superficie")
    opcion_orden = input("¿Cómo desea ordenar los países?: ")

    sentido = input("Desea orden ascendente (A) o descendente (D)?: ").strip().lower()
    descendente = (sentido == "d")

    n = len(lineas)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if opcion_orden == "1":  # nombre
                if (lineas[j][0].lower() < lineas[min_index][0].lower()) != descendente:
                    min_index = j
            elif opcion_orden == "2":  # población
                if (int(lineas[j][1]) < int(lineas[min_index][1])) != descendente:
                    min_index = j
            elif opcion_orden == "3":  # superficie
                if (float(lineas[j][2]) < float(lineas[min_index][2])) != descendente:
                    min_index = j
            else:
                print("Opción inválida.")
                return
        lineas[i], lineas[min_index] = lineas[min_index], lineas[i]

    print("\n--- Lista de países ordenada ---")
    print(f"{'PAÍS':12} | {'POBLACIÓN':12} | {'SUPERFICIE':12} | {'CONTINENTE'}")
    print("------------------------------------------------------------")
    for pais, poblacion, superficie, continente in lineas:
        print(f"{pais:12} | {poblacion:12} | {superficie:12} | {continente}")

# Muestra estadísticas básicas del archivo (promedios, máximos, mínimos, conteos)
def mostrar_estadisticas():
    with open("paises.csv", "r") as archivo:
        next(archivo)  # saltar encabezado
        lineas = [linea.strip().split(",") for linea in archivo]

    if not lineas:
        print("No hay datos disponibles para mostrar estadísticas.")
        return

    # Extraer columnas en listas individuales
    paises = []
    poblaciones = []
    superficies = []
    continentes = []

    for fila in lineas:
        paises.append(fila[0])
        poblaciones.append(int(fila[1]))
        superficies.append(float(fila[2]))
        continentes.append(fila[3])

    # Buscar país con mayor y menor población
    indice_mayor = 0
    indice_menor = 0
    for i in range(1, len(poblaciones)):
        if poblaciones[i] > poblaciones[indice_mayor]:
            indice_mayor = i
        if poblaciones[i] < poblaciones[indice_menor]:
            indice_menor = i

    pais_mayor_poblacion = paises[indice_mayor]
    pais_menor_poblacion = paises[indice_menor]

    # Calcular promedios
    promedio_poblacion = sum(poblaciones) / len(poblaciones)
    promedio_superficie = sum(superficies) / len(superficies)

    # Contar países por continente
    conteo_continentes = {}
    for cont in continentes:
        if cont in conteo_continentes:
            conteo_continentes[cont] += 1
        else:
            conteo_continentes[cont] = 1

    # Mostrar resultados
    print(f"País con mayor población: {pais_mayor_poblacion} ({poblaciones[indice_mayor]})")
    print(f"País con menor población: {pais_menor_poblacion} ({poblaciones[indice_menor]})")
    print(f"Promedio de población: {promedio_poblacion}")
    print(f"Promedio de superficie: {promedio_superficie}")
    print("Cantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"- {continente}: {cantidad}")

# Permite agregar o eliminar países del archivo CSV
def actualizar_archivo():
    print("\n--- ACTUALIZAR ARCHIVO ---")
    print("1. Agregar un país")
    print("2. Eliminar un país")
    print("3. Volver al menú")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        pais = input("Ingrese el nombre del país: ").strip()
        poblacion = input("Ingrese la población: ").strip()
        superficie = input("Ingrese la superficie: ").strip()
        continente = input("Ingrese el continente: ").strip()

        # Validar que el nombre no esté vacío
        if pais == "":
            print("El nombre del país no puede estar vacío.")
            return

        # Validar que el país no exista ya (evita duplicados)
        existe = False
        with open("paises.csv", "r") as archivo:
            for linea in archivo:
                if linea.strip().split(",")[0].lower() == pais.lower():
                    existe = True
                    break

        if existe:
            print(f"El país {pais} ya existe en el archivo.")
            return

        # Validar que población y superficie sean valores numéricos
        es_valido = True

        # Validar población (solo dígitos)
        for caracter in poblacion:
            if caracter < "0" or caracter > "9":
                es_valido = False
                break

        # Validar superficie (permite un punto decimal)
        punto_encontrado = 0
        for caracter in superficie:
            if caracter == ".":
                punto_encontrado += 1
                if punto_encontrado > 1:
                    es_valido = False
                    break
            elif caracter < "0" or caracter > "9":
                es_valido = False
                break

        if not es_valido:
            print("Población y superficie deben ser valores numéricos.")
            return

        # Si todo está bien, agregar el país
        with open("paises.csv", "a") as archivo:
            archivo.write(f"{pais},{poblacion},{superficie},{continente}\n")
        print(f"País {pais} agregado correctamente.")

    elif opcion == "2":
        pais_a_eliminar = input("Ingrese el país que desea eliminar: ").strip().lower()
        with open("paises.csv", "r") as archivo:
            lineas = archivo.readlines()
        nuevas_lineas = []
        eliminado = False
        for linea in lineas:
            partes = linea.strip().split(",")
            if partes[0].lower() == pais_a_eliminar:
                eliminado = True
                continue
            nuevas_lineas.append(linea)
        if eliminado:
            with open("paises.csv", "w") as archivo:
                for linea in nuevas_lineas:
                    archivo.write(linea)
            print(f"El país {pais_a_eliminar} fue eliminado correctamente.")
        else:
            print(f"No se encontró el país {pais_a_eliminar} en el archivo.")

    elif opcion == "3":
        print("Volviendo al menú principal...")

    else:
        print("Opción inválida.")

# Menú principal que permite al usuario elegir la acción a realizar
while True:
    print("""------MENU DE OPCIONES DEL MUNDO------
          1. Crear archivo
          2. Buscar un pais
          3. Filtrar paises
          4. Ordenar paises
          5. Mostrar estadisticas
          6. Actualizar archivo(agregar/eliminar pais)
          7. Salir""")

    opcion = input("Ingrese una opcion a realizar: ")

    if opcion == "1":
        crear_archivo()
    elif opcion == "2":
        buscar_pais()
    elif opcion == "3":
        filtrar_paises()
    elif opcion == "4":
        ordenar_paises()
    elif opcion == "5":
        mostrar_estadisticas()
    elif opcion == "6":
        actualizar_archivo()
    elif opcion == "7":
        print("Hasta luego!")
        break
    else:
        print("Opcion invalida")