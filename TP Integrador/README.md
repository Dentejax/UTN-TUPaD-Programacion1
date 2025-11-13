# Gestión de Países

# Descripción del Programa
Este programa permite **gestionar y analizar información sobre países** almacenada en un archivo CSV (`paises.csv`).  
A través de un menú interactivo, el usuario puede crear el archivo, buscar, filtrar, ordenar, agregar o eliminar países, y también generar estadísticas básicas sobre la población y superficie.

El sistema fue desarrollado en **Python**, utilizando estructuras de datos simples (listas, diccionarios) y funciones modulares que facilitan la comprensión y el mantenimiento del código.

# Instrucciones de Uso

1. **Ejecutar el programa** desde una consola o entorno como IDLE, Visual Studio Code o Replit. Y seleccionar la opcion 1 para que todo funcione a la perfección

2. **Seleccionar una opción del menú principal**:

   ------MENU DE OPCIONES DEL MUNDO------
   1. Crear archivo
   2. Buscar un país
   3. Filtrar países
   4. Ordenar países
   5. Mostrar estadísticas
   6. Actualizar archivo (agregar/eliminar país)
   7. Salir

3. **Operaciones disponibles**:

   * **1. Crear archivo:** genera el archivo `paises.csv` con datos iniciales.
   * **2. Buscar país:** permite encontrar un país por nombre (coincidencia parcial o exacta).
   * **3. Filtrar países:** filtra por continente, rango de población o superficie.
   * **4. Ordenar países:** organiza los países por nombre, población o superficie (ascendente o descendente).
   * **5. Mostrar estadísticas:** calcula promedios, máximos, mínimos y conteo por continente.
   * **6. Actualizar archivo:** permite agregar o eliminar países.
   * **7. Salir:** finaliza el programa.

# Ejemplos de Entradas y Salidas

# Ejemplo 1: Buscar un país

**Entrada:**

Ingrese el país a buscar: arg

**Salida:**

El país Argentina está dentro del archivo, y su contenido es:
Población: 45851378
Superficie: 2780400
Continente: America

# Ejemplo 2: Filtrar países por población

**Entrada:**

Qué filtro desea realizar: 2
Ingrese el valor mínimo de población: 40000000
Ingrese el valor máximo de población: 60000000

**Salida:**

- Argentina: Población 45851378, Superficie 2780400, Continente America
- España: Población 49442844, Superficie 505978, Continente Europa

# Ejemplo 3: Mostrar estadísticas

**Salida:**

País con mayor población: Japon (123103479)
País con menor población: Nueva Zelanda (5251899)
Promedio de población: 66391400.0
Promedio de superficie: 1024270.8
Cantidad de países por continente:
- America: 1
- Europa: 1
- Asia: 1
- Oceania: 1
- Africa: 1

## Participación de los Integrantes

| Integrante       | Rol / Aporte principal
| **Franco Pagés** | Desarrollo completo del código, validaciones de datos, estructura del menú, y       
|                  | documentación técnica (README e informe teórico). 