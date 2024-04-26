#COMENTARIOS
#EJEMPLO 1 CON #
#Args: - año (int): Año que se desea comprobar.

#EJEMPLO 2 CON """ (3 veces comillas dobles)
"""
Args: - a (float): Coeficiente de x. - b (float): Término constante.
Returns: - float: Solución de la ecuación.
"""

#EJERCICIO 1
"""
Escribi una función que tome dos números enteros y calcule su división, devolviendo si la división es exacta o no.
"""
#Para definir una funcion en python debo comenzar con "def" (FUNCION = def)
#luego el nombre de la funcion
#Entre parentesis declaro los argumentos o variables que debe tomar
#CUALQUIER FUNCION NO USA LLAVES { }, SE USA : (dos puntos)
def division (a, b):
       resultado = a / b
       return resultado

print(division(4, 2))
#-----------------------------------------------------------------------#
print(division(7, 3))
#-----------------------------------------------------------------------#

#EJERCICIO 2
"""
Escribi una función que tome un año y devuelva si es bisiesto o no.
"""
#Args: - año (int): Año que se desea comprobar.
#Returns: - bool: True si el año es bisiesto, False si no lo es.
def bisiesto(a):
 
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        return True
    else:
        return False
    
print(bisiesto(2012))
#-----------------------------------------------------------------------#
print(bisiesto(2017))
#-----------------------------------------------------------------------#

#EJERCICIO 3
"""
Escribi una función que tome los coeficientes de una ecuación de primer grado (a x + b = 0) y devuelva la solución.
"""
#Args: - a (float): Coeficiente de x. - b (float): Término constante.
#Returns: - float: Solución de la ecuación.
def solucion(a, b):
    if a == 0:
       raise ValueError("El coeficiente 'a' no puede ser cero.")
    else:
       return -b / a
    
a = 2
b = -4

resultado = solucion(a, b)

print(f"La solución de la ecuación {a}x + {b} = 0 es: x = {resultado}") 
#Otra forma de llamar a format-string
print("La solución de la ecuación {}x + {} = 0 es: x = {}".format(a, b, resultado))
#-----------------------------------------------------------------------#
resultado = solucion(2, 4)
print(f"La solución de la ecuación {a}x + {b} = 0 es: x = {resultado}") 
#-----------------------------------------------------------------------#
resultado = solucion(3, 5)
print(f"La solución de la ecuación {a}x + {b} = 0 es: x = {resultado}") 
#-----------------------------------------------------------------------#
resultado = solucion(2, 0)
print(f"La solución de la ecuación {a}x + {b} = 0 es: x = {resultado}") 
#-----------------------------------------------------------------------#

#EJERCICIO 4
"""
Escribi una función que simule un juego en el que dos jugadores tiran un dado. El que saque el valor más alto, gana. Si la puntuación coincide, empatan.
"""
import random

def juego(jugador1, jugador2):

    # Mostrar los resultados de los dados
    print(f"El jugador 1 tira el dado y obtiene: {jugador1}")
    print(f"El jugador 2 tira el dado y obtiene: {jugador2}")
    
    # Determinar el resultado del juego
    if jugador1 > jugador2:
        print("¡El jugador 1 gana!")
    elif jugador2 > jugador1:
        print("¡El jugador 2 gana!")
    else:
        print("¡Empate!")
    
# Simular tirada de dados
tirada_jugador1 = random.randint(1, 6)
tirada_jugador2 = random.randint(1, 6)

# Ejecutar la función con los valores de los dados
juego(tirada_jugador1, tirada_jugador2)
#-----------------------------------------------------------------------#
juego(343, 545)
#-----------------------------------------------------------------------#

#EJERCICIO 5
"""
Escribi una función que tome dos números enteros y devuelva qué número es pares y cuál impar.
"""
def par_impar(num1, num2):
    if num1 % 2 == 0:
        print(f"{num1} es un número par")
    else:
        print(f"{num1} es un número impar")
        
    if num2 % 2 == 0:
        print(f"{num2} es un número par")
    else:
        print(f"{num2} es un número impar")

# Ejemplo de uso
par_impar(7, 10)
#-----------------------------------------------------------------------#
par_impar(4, 5)
#-----------------------------------------------------------------------#
par_impar(4, 10)

#EJERCICIO 6
"""
Escribi una función que tome una lista de números y calcule su suma.
"""
def suma_numeros(lista):
    suma = sum(lista)
    return suma

# Ejemplo de uso
numeros = [1, 2, 3, 4, 5]
resultado = suma_numeros(numeros)

print("La suma de los números es:", resultado)
#-----------------------------------------------------------------------#
resultado = suma_numeros([1, 4, 5, 7, 8, 9])
print(f"La suma de los números es: {resultado}")

#EJERCICIO 7
"""
Escribi una función que tome dos palabras y diga si riman o no. Si coinciden las tres últimas letras debe devolver que riman.
Si coinciden sólo las dos últimas tiene que decir que riman algo y si no, que no riman.
"""
def riman(palabra1, palabra2):
    # Obtener las últimas tres letras de cada palabra
    ultimas_letras_palabra1 = palabra1[-3:]
    ultimas_letras_palabra2 = palabra2[-3:]

    # Verificar si coinciden las tres últimas letras
    if ultimas_letras_palabra1 == ultimas_letras_palabra2:
        return "Las palabras riman"
    # Verificar si coinciden las dos últimas letras
    elif ultimas_letras_palabra1[-2:] == ultimas_letras_palabra2[-2:]:
        return "Las palabras riman algo"
    else:
        return "Las palabras no riman"
    
# Se modifican los argumentos palabra1 y palabra2
# Las palabras riman
resultado = riman('hola', 'cacerola')
print(resultado)
#-----------------------------------------------------------------------#
# Las palabras no riman
resultado = riman('jirafa', 'roja')
print(resultado)
#-----------------------------------------------------------------------#
# Las palabras riman algo
print(riman('computadora', 'cabecera'))

#EJERCICIO 8
"""
Escribi una función para convertir temperatura de grados celsius a fahrenheit (Formula : F = C * 9/5 + 32) 
"""
def convert_grados(gradosCelsius):
    gradosFahrenheit = gradosCelsius * 9/5 +32
    return gradosFahrenheit

temperatura_fahrenheit = convert_grados(24)
print(f"24 grados Celsius equivalen a {temperatura_fahrenheit} grados Fahrenheit")