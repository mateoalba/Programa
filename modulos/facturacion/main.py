# main.py
import autenticacion
import arqueo_caja
import clientes
import facturar 
import reportes
import configurar

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
            productos.mostrar_productos()
            productos_seleccionados = {}
            
            while True:
                producto_nombre = input("Ingrese producto o 'fin' para terminar: ")
                if producto_nombre == 'fin':
                    break
                precio = productos.obtener_precio(producto_nombre)
                if precio:
                    productos_seleccionados[producto_nombre] = precio
                else:
                    print("Producto no disponible.")
            
            cliente_nombre = input("Ingrese el nombre del cliente: ")
            cliente = clientes.Cliente(cliente_nombre)
            total = facturar.crear_factura(cliente, productos_seleccionados)
            arqueo.agregar_ingreso(total)
            facturas.append(cliente)
        
        elif opcion == "2":
            # Mostrar saldo de caja
            arqueo.mostrar_saldo()
        
        elif opcion == "3":
            # Reportes
            reportes.generar_reporte(facturas)
        
        elif opcion == "4":
            # Configuración
            configurar.configurar_sistema()
        
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

