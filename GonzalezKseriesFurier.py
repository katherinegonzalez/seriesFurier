# ----------------------------------------------------------------------------------------
# PROGRAMA: Ondas Sinoidales
# ----------------------------------------------------------------------------------------
# Descripción: Este programa presenta un menú con 3 tipos de onda: cuadrada, triangular y
# diente de sierra. Al seleccionar una de ellas el programa se encarga de dibujar su
# aproximación (teniendo en cuenta las Series de Furier).

# ----------------------------------------------------------------------------------------
# Autor: Katherine Xiomar González Santacruz
# Version: 1.0
# [05.11.2022]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------------------
# FUNCIÓN: ondaCuadrada
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para definir la función de la serie de furier para
# una onda cuadrada
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) n, (numpy.ndarray) w
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           n % 2 == 0 -> a = 0, n > 1 and n % 2 != 0 ->  a = 1 / ((2 * n) + 1),
#           n == 1 -> fn = np.sin(w)
#       Valor de retorno: (numpy.ndarray) fn - resultado de la función
# ----------------------------------------------------------------------------------------
def ondaCuadrada(n, w):
    a = 0
    if (n % 2 == 0):
        a = 0
    elif (n > 1 and n % 2 != 0):
        a = 1 / ((2 * n) + 1)

    if (n == 1):
        fn = np.sin(w)
    else:
        fn = a * np.sin(((2 * n) + 1) * w)

    return fn

# ----------------------------------------------------------------------------------------
# FUNCIÓN: cuadrada
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para realizar la sumatoria e imprimir la onda cuadrada
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada:  (int) L, (int) ciclos, (int) num
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Muestra el dibujo de una aproximación de la onda cuadrada.
# ----------------------------------------------------------------------------------------
def cuadrada(L, ciclos, num):
    n = 1
    f = 0
    w = np.linspace(-0.001, 2 * ciclos * L, num)
    while n < 10:
        f += ondaCuadrada(n, w)
        n += 1

    plt.plot(w, f)
    plt.show()

# ----------------------------------------------------------------------------------------
# FUNCIÓN: ondaTriangular
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para definir la función de la serie de furier para
# una onda triangular
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) n, (numpy.ndarray) w
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           n % 2 == 0 -> a = 0, n > 1 and n % 2 != 0 -> (-1) ** n / ((2 * n) + 1)**2,
#           n == 1 -> fn = np.sin(w)
#       Valor de retorno: (numpy.ndarray) fn - resultado de la función
# ----------------------------------------------------------------------------------------
def ondaTriangular(n, w):
    a = 0
    if (n % 2 == 0):
        a = 0
    elif (n % 2 != 0 and n > 1):
        a = (-1) ** n / ((2 * n) + 1)**2

    if (n == 1):
        fn = np.sin(w)
    else:
        fn = a * np.sin(((2 * n) + 1) * w)
    return fn

# ----------------------------------------------------------------------------------------
# FUNCIÓN: triangular
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para realizar la sumatoria e imprimir la onda triangular
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada:  (int) L, (int) ciclos, (int) num
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Muestra el dibujo de una aproximación de la onda triangular.
# ----------------------------------------------------------------------------------------
def triangular(L, ciclos, num):
    n = 1
    f = 0
    w = np.linspace(-0.001, 2* ciclos * L, num)
    while n < 40:
        f += ondaTriangular(n, w)
        n += 1
    plt.plot(w, f)
    plt.show()

# ----------------------------------------------------------------------------------------
# FUNCIÓN: ondaDienteSierra
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para definir la función de la serie de furier para
# una onda diente de sierra
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (int) n, (numpy.ndarray) w
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           n >= 1 -> a = (-1) ** (n+1) / n
#       Valor de retorno: (numpy.ndarray) fn - resultado de la función
# ----------------------------------------------------------------------------------------
def ondaDienteSierra(n, w):
    a = 0
    if (n >= 1):
        a = (-1) ** (n+1) / n

    fn = a * np.sin(n * w)
    return fn

# ----------------------------------------------------------------------------------------
# FUNCIÓN: sierra
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para realizar la sumatoria e imprimir la onda diente de sierra
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada:  (int) L, (int) ciclos, (int) num
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Muestra el dibujo de una aproximación de la onda diente de sierra.
# ----------------------------------------------------------------------------------------
def sierra(L, ciclos, num):
    n = 1
    f = 0
    w = np.linspace(-0.001, 2* ciclos * L, num)
    while n < 30:
        f += ondaDienteSierra(n, w)
        n += 1

    plt.plot(w, f)
    plt.show()

# ----------------------------------------------------------------------------------------
# FUNCIÓN: validarInput
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar el valor ingresado por el usuario
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) mensaje, (function) condicion
#       variable auxiliar: (bool) seguirPreguntando
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si seguir preguntando es false, el ciclo se rompe y se retorna el valor ingresado
#           por el usuario.
#           Si la condición no se cumple imprime un mensaje en pantalla
#       Valor de retorno: (str) opcionIngresada
# ----------------------------------------------------------------------------------------
def validarInput (mensaje, condicion):
    seguirPreguntando = True
    while seguirPreguntando:
        opcionIngresada = input(mensaje)
        if (condicion(opcionIngresada)):
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido')
    return opcionIngresada

# ----------------------------------------------------------------------------------------
# FUNCIÓN: condicionInput
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar el input ingresado por el usuario
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) opcionIngresada
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       Valor de retorno: bool
# ----------------------------------------------------------------------------------------
def condicionInput(opcionIngresada):
    return opcionIngresada == '1' or opcionIngresada == '2' or \
           opcionIngresada == '3' or opcionIngresada == '0'

# ----------------------------------------------------------------------------------------
# Ejecutar Programa
# ----------------------------------------------------------------------------------------
opcion = ''
L = np.pi
ciclos = 2

while (opcion != '0'):
    print('\n')
    print('Programa para imprimir ondas cuadrada, triangular y diente de sierra a través de Series de Furier.')
    print('Seleccione el tipo de onda que desea dibujar: ')
    print('1. Onda Cuadrada')
    print('2. Onda Triangular')
    print('3. Onda Diente de Sierra')
    print('0. Salir')

    opcion = validarInput('Ingrese opción: ', condicionInput)

    print('\n')
    if (opcion == '1'):
        cuadrada(L, ciclos, 100)
    elif (opcion == '2'):
       triangular(L, ciclos, 1000)
    elif (opcion == '3'):
        sierra(L, ciclos, 100)

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------
