import math 
def calcular_potencia (base, exponente): 
    r = math.pow(base, exponente)
    return r

def calcular_suma (a,b): 
    suma = a + b
    return suma

def calcular_resta (a,b): 
    resta = a - b
    return resta

def calcular_multiplicacion (a,b): 
    multiplicacion = a * b
    return multiplicacion

def calcular_division (a,b):
    if b == 0:
        division = 0
    else:
        division = a / b
    return division