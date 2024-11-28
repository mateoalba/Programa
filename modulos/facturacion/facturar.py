# facturar.py
def crear_factura(cliente, productos):
    total = sum(productos.values())
    print(f"Factura para {cliente.nombre}:")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio}")
    print(f"Total: ${total}")
    return total

