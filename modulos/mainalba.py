import facturacion.autenticacion as autenticacion
import facturacion.arqueo_caja.arqueo_caja as arqueo_caja
import facturacion.clientes.clientes as clientes
import facturacion.facturacion as facturar
import facturacion.reportes.reportes as reportes
import facturacion.configurar.configurar as configurar
import facturacion.productos.productos as productos


def main():
    # Autenticación del usuario
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if not autenticacion.autenticar(usuario, contrasena):
        print("Autenticación fallida.")
        return

    # Inicializar componentes
    arqueo = arqueo_caja.ArqueoCaja()
    facturas = []
    productos_disponibles = productos.obtener_lista_productos()  # Función ficticia que devuelve productos disponibles

    while True:
        print("\nMenú de opciones:")
        print("1. Facturar")
        print("2. Arqueo de caja")
        print("3. Reportes")
        print("4. Configuración")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Facturar
            print("\nProductos disponibles:")
            for prod in productos_disponibles:
                print(f"- {prod['nombre']} (Precio: ${prod['precio']})")

            productos_seleccionados = []
            while True:
                producto_nombre = input("Ingrese producto o 'fin' para terminar: ")
                if producto_nombre.lower() == "fin":
                    break

                # Buscar el producto
                producto = next(
                    (p for p in productos_disponibles if p["nombre"] == producto_nombre), None
                )
                if producto:
                    cantidad = int(input(f"Ingrese cantidad para {producto_nombre}: "))
                    productos_seleccionados.append({"producto": producto, "cantidad": cantidad})
                else:
                    print("Producto no disponible.")

            cliente_nombre = input("Ingrese el nombre del cliente: ")
            total = facturar.crear_factura(cliente_nombre, productos_seleccionados)
            arqueo.agregar_ingreso(total)
            facturas.append({"cliente": cliente_nombre, "total": total})

        elif opcion == "2":
            # Mostrar saldo de caja
            arqueo.mostrar_saldo()

        elif opcion == "3":
            # Generar reportes
            tipo_reporte = input("Tipo de reporte (ventas, ingresos, etc.): ")
            reportes.generar_reporte(tipo_reporte, facturas)

        elif opcion == "4":
            # Configuración del sistema
            opcion_config = input("Ingrese la opción de configuración: ")
            valor_config = input("Ingrese el valor: ")
            configurar.cambiar_configuracion(opcion_config, valor_config)

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()