# Ejercicio 1
# 1. Entender el problema
"""
Entrada: una lista de enteros
Proceso: recorrer una vez, acumular varios contadores y retornar un dict
Salida: un diccionario con las estadísticas
Ejemplo de entrada: [8, 5, 12, 7, 3, 10]
Salida esperada: {"total": 45, "promedio": 7.5, "max": 12, "min": 3, "pares": 3} 
"""
# 2. Bosquejo a mano
"""nums = [8, 5, 12, 7, 3, 10]
Un solo recorrido:
  suma acumula: 8, 13, 25, 32, 35, 45
  máximo se actualiza si es mayor
  mínimo se actualiza si es menor
  pares: incrementa contador si n % 2 == 0
Al final construyo el diccionario con los 5 valores."""
# 3. Descubrir el patrón
"""Aunque Python tiene sum(), max(), min(), hacerlo con un solo recorrido y patrones (acumulador, campeón, contador) muestra 
que dominas el concepto de dict como valor de retorno. Retornar un dict es más útil que retornar una tupla: quien llama 
la función se refiere a los valores por nombre, no por posición."""""
# 4. Escribir el codigo
def estadisticas(numeros):
    if not numeros:
        return {"total": 0, "promedio": 0, "max": None, "min": None, "pares": 0}

    total = 0
    maximo = numeros[0]
    minimo = numeros[0]
    pares = 0

    for n in numeros:
        total += n
        if n > maximo: maximo = n
        if n < minimo: minimo = n
        if n % 2 == 0: pares += 1

    return {
        "total": total,
        "promedio": total / len(numeros),
        "max": maximo,
        "min": minimo,
        "pares": pares
    }
# Uso
r = estadisticas([8, 5, 12, 7, 3, 10])
print(r)
print(f"Promedio: {r['promedio']:.2f}")

# Ejercicio 2
# 1. Entender el problema
""""
Entrada: una cadena de texto
Proceso: dividir en palabras, limpiar, contar cada aparición
Salida: un diccionario con palabras y frecuencias
Ejemplo de entrada: "Python es genial. Python es potente. Python es simple."
Salida esperada: {"python": 3, "es": 3, "genial": 1, "potente": 1, "simple": 1}
"""
# 2. Bosquejo a mano
"""
texto = "Python es genial. Python es potente. Python es simple."
Paso 1: paso a minúsculas
Paso 2: quito signos
Paso 3: divido por espacios
  palabras = ["python", "es", "genial", "python", "es", "potente", "python", "es", "simple"]
Paso 4: cuento
  "python" aparece 3 veces
  "es" aparece 3 veces
  ...
"""
# 3. Descubrir el patrón
"""
El patrón para contar apariciones se llama diccionario contador: la clave es el elemento; el valor es cuántas veces apareció.
El truco elegante es d[palabra] = d.get(palabra, 0) + 1: get devuelve el valor actual o 0 si no existe, y le sumamos 1. Sin get el primer += 1 da KeyError.
Aún más elegante: collections.Counter. Lo veremos en el módulo 5.
"""
# 4. Escribir el codigo
def contar_unicas(texto):
    # Normalizamos
    texto = texto.lower()
    for signo in ".,;:!?\"'()":
        texto = texto.replace(signo, "")

    # Contamos con dict
    frecuencias = {}
    for palabra in texto.split():
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias


# Uso
texto = "Python es genial. Python es potente. Python es simple."
r = contar_unicas(texto)
for palabra, cant in r.items():
    print(f"{palabra}: {cant}")

# Ejercicio 3
"""
Función guardar_config(datos, archivo) y cargar_config(archivo). Si el archivo no existe al cargar, retornar un dict vacío.
"""
# 1. Entender el problema
"""
Entrada: un nombre de archivo y un diccionario de datos
Proceso: guardar y abrir el archivo en formato JSON, utilizando el dumps para convertir el formato JSON a un diccionario.
Salida: un diccionario con los datos guardados o cargados

Ejemplo de entrada: cargar_config('config.json')
Salida esperada {'tema': 'oscuro', 'idioma': 'es'}
"""
# 2. Bosquejo a mano
"""
guardar_config({'tema': 'oscuro', 'idioma': 'es'}, 'config.json')
abrir archivo config.json en modo escritura
json.dump(datos, archivo)
el archivo quedaria con el contenido {"tema": "oscuro", "idioma": "es"}
cargar_config('config.json')
intentar abrir archivo
si existe el archivo se retornara el diccionario cargado con los datos
si no existe el archivo se retornara un diccionario vacio
"""
# 3. Descubrir el patrón
"""
Esto es un patron de serializacion y deserializacion de datos, utilizando el formato JSON para guardar y cargar los datos de un archivo. 
los datos guardados en guardados en la forma de un diccionario, se traducen a formato JSON y se guardan en un archivo, y al cargar se traduce de formato JSON a un
diccionario.    
"""
# 4. Escribir el codigo
import json 
import os 
def guardar_config(datos, archivo):
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent = 2)

def cargar_config(archivo):
    if not os.path.exists(archivo):
        return {}
    with open(archivo, 'r') as f:
        return json.load(f)

#Uso
config = cargar_config('config.json')
config ["tema"] = 'oscuro'
config ["idioma"] = 'es'
guardar_config(config, 'config.json')

# Ejercicio 4
"""
Función sin_duplicados(lista) que retorne una lista nueva sin duplicados pero conservando el orden de la primera aparición.
"""
# 1. Entender el problema
"""
Entrada: una lista de elementos
Proceso: recorrer la lista y agregar a una nueva lista solo los elementos que no se han visto
Salida: una lista sin duplicados, conservando el orden de la primera aparición
Ejemplo de entrada: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
Salida esperada: [3, 1, 4, 5, 9, 2, 6]
"""
# 2. Bosquejo a mano
"""
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
visto = set()
resultado = []
Recorremos la lista:
x = 3: no está en visto, lo agregamos a visto y a resultado
x = 1: no está en visto, lo agregamos a visto y a resultado
x = 4: no está en visto, lo agregamos a visto y a resultado
x = 1: ya está en visto, lo ignoramos
x = 5: no está en visto, lo agregamos a visto y a resultado
x = 9: no está en visto, lo agregamos a visto y a resultado
x = 2: no está en visto, lo agregamos a visto y a resultado
x = 6: no está en visto, lo agregamos a visto y a resultado
x = 5: ya está en visto, lo ignoramos
x = 3: ya está en visto, lo ignoramos
Al final, resultado = [3, 1, 4, 5, 9, 2, 6]
"""
# 3. Descubrir el patrón
"""
El patrón es usar un conjunto (set) para llevar un registro de los elementos que ya hemos visto, 
y una lista para almacenar los elementos únicos en el orden de su primera aparición.
"""
# 4. Escribir el codigo
def sin_duplicados(lista):
    visto = set()
    resultado = []
    for x in lista:
        if x not in visto:
            visto.add(x)
            resultado.append(x)
    return resultado

# Alternativa (Python 3.7+): dict.fromkeys mantiene orden
def sin_duplicados_v2(lista):
    return list(dict.fromkeys(lista))

print(sin_duplicados([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))

# Ejercicio 5
"""
En vez de una cascada if/elif, usa un dict donde la clave es la operación y el valor es la función que la implementa.
"""
# 1. Entender el problema
"""
Entrada: dos números y un operador
Proceso: realizar la operación correspondiente según el operador
Salida: el resultado de la operación
Ejemplo de entrada: a = 5, b = 3, operador = "+"
Salida esperada: 8
"""
# 2. Bosquejo a mano
"""
operaciones = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else None,
}
Usuario ingresa "+"  -> busco operaciones["+"]  -> obtengo la función suma
Usuario ingresa 5, 3 -> ejecuto función(5, 3)   -> 8.0
Usuario ingresa "q"  -> rompo el loop
Usuario ingresa "%"  -> no está en el dict -> mensaje de error, continúo el loop
"""
# 3. Descubrir el patrón
"""
El patrón es usar un diccionario para mapear operadores a funciones, lo que permite evitar una cascada de if/elif 
y hace que el código sea más limpio y fácil de mantener.
"""
# 4. Escribir el codigo
def calculadora():
    operaciones = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else None,
    }

    while True:
        op = input("Operador (+ - * / o q para salir): ")
        if op == "q":
            break
        if op not in operaciones:
            print("Operador inválido"); continue

        a = float(input("a: "))
        b = float(input("b: "))
        r = operaciones[op](a, b)
        print(f"Resultado: {r}")

calculadora()

