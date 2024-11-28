from calculadora import operaciones as oper
from area import area
from conversiones import conver
from perimetro import perimetro as pri

a = area.area_circulo(5)

print(f'El area del circulo con radio 5 es: {a}')
    
    
a = oper.calcular_multiplicacion(25, 3)
print(f"El valor de la multiplicaciòn: {a}")

pesos = 3500

a = conver.convertir_pesos_dolares(pesos)
print(f"{pesos} pesos equivale a {a} dolares")

r = 5
valor3 = pri.calcular_circulo_perimetro(r)
print(f"{valor3} es el area del circulo de radio {r}")
