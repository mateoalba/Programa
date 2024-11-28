# productos.py
class Producto:
    def _iniventario_(self, nombre, valor, desc, cant):
        self.nombre = nombre
        self.valor = valor
        self.desc = desc
        self.cant = cant

a = int(input("¿Cuantos productos desea ingresar?:"))
productos = []

for i in range (a):
    print("Numero de productos: ", i+1)
    n = input("Nombre del producto: ")
    val = int(input("Valor del producto: "))
    desc = input("Descripcion del producto: ")
    cant = int(input("Cantidad del producto: "))
    p = Producto = n,val,desc,cant
    productos.append (p)

print("------LISTADO DE PRODUCTOS--------")
for j in range(len(productos)):
    print("Nombre: ", productos[j])
    print("Valor: ", productos[j])
    print("Descripcion: ", productos[j])
    print("Cantidad: ", productos[j])
    print("=================================")

