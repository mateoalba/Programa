from config import constantes as const
def perimetro_rectangulo (a, b):
    perimetro = 2 * (a + b)
    return perimetro 


def calcular_circulo_perimetro(radio):
    perimetro = 2 * const.PI * radio
    return perimetro