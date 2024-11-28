# clientes.py
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print(f"Cliente: {self.nombre}")

