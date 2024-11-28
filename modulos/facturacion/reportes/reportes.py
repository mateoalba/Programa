# reportes.py
def generar_reporte(facturas):
    print("\nReporte de ventas:")
    for factura in facturas:
        factura.mostrar()
