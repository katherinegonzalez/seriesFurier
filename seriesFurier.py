import numpy as np
import matplotlib.pyplot as plt

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

def cuadrada():
    L = np.pi
    ciclos = 2
    n = 1
    f = 0
    w = np.linspace(-0.001, 2 * ciclos * L, 100)
    while n < 10:
        f += ondaCuadrada(n, w)
        n += 1

    plt.plot(w, f)
    plt.show()

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

def triangular():
    L = np.pi
    ciclos = 2
    n = 1
    f = 0
    w = np.linspace(-0.001, 2* ciclos * L, 1000)
    while n < 40:
        f += ondaTriangular(n, w)
        n += 1
    plt.plot(w, f)
    plt.show()

def ondaDienteSierra(n, w):
    a = 0
    if (n >= 1):
        a = (-1) ** (n+1) / n

    fn = a * np.sin(n * w)
    return fn

def sierra():
    L = np.pi
    ciclos = 2
    n = 1
    f = 0
    w = np.linspace(-0.001, 2* ciclos * L, 100)
    while n < 30:
        f += ondaDienteSierra(n, w)
        n += 1

    plt.plot(w, f)
    plt.show()

# ----------------------------------------------------------------------------------------
# Ejecutar Programa
# ----------------------------------------------------------------------------------------
opcion = ''
longitudLista = 10

def validarInput (mensaje, condicion):
    seguirPreguntando = True
    while seguirPreguntando:
        opcionIngresada = input(mensaje)
        if (condicion(opcionIngresada)):
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido')
    return opcionIngresada

def condicionInput(opcionIngresada):
    return opcionIngresada == '1' or opcionIngresada == '2' or \
           opcionIngresada == '3' or opcionIngresada == '0'

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
        cuadrada()
    elif (opcion == '2'):
       triangular()
    elif (opcion == '3'):
        sierra()

# ----------------------------------------------------------------------------------------
# end.
# ----------------------------------------------------------------------------------------
