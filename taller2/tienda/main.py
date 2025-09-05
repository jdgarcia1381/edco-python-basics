from crud import (
    actualizar_cliente,
    actualizar_producto,
    agregar_cliente,
    agregar_producto,
    eliminar_venta,
    listar_clientes,
    listar_productos,
    listar_ventas,
    registrar_venta,
)
from database import conexion


def main():
    procesar_input_usuario_while()


def procesar_input_usuario_while():
    while True:
        input_usuario = input(
            "\nIngrese el número de la acción:\n1. Listar clientes.\n2. Listar productos.\n3. Listar ventas.\n4. Agregar cliente.\n5. Agregar producto.\n6. Registrar venta.\n7. Actualizar datos cliente.\n8. Actualizar datos producto.\n9. Eliminar venta.\n10. Salir.\n"
        )

        try:
            input_usuario_entero = int(input_usuario)
        except ValueError:
            print("Por favor, ingrese un número válido.")

        try:
            if input_usuario_entero == 1:
                listar_clientes()
            elif input_usuario_entero == 2:
                listar_productos()
            elif input_usuario_entero == 3:
                listar_ventas()
            elif input_usuario_entero == 4:
                input_nombre = input("Ingrese el nombre del cliente:")
                input_email = input("Ingrese el correo del cliente:")
                agregar_cliente(input_nombre, input_email)
            elif input_usuario_entero == 5:
                input_nombre = input("Ingrese el nombre del producto:")
                input_precio = input("Ingrese el precio del producto:")
                input_stock = input("Ingrese el stock del producto:")
                agregar_producto(input_nombre, input_precio, input_stock)
            elif input_usuario_entero == 6:
                input_cliente_id = input("Ingrese el ID del cliente:")
                input_producto_id = input("Ingrese el ID del producto:")
                input_cantidad = input("Ingrese la cantidad vendida del producto:")
                registrar_venta(input_cliente_id, input_producto_id, input_cantidad)
            elif input_usuario_entero == 7:
                input_current_email = input(
                    "Ingrese el correo actual del cliente a actualizar:"
                )
                input_new_nombre = input("Ingrese el nuevo nombre del cliente:")
                input_new_email = input("Ingrese el nuevo correo del cliente:")
                actualizar_cliente(
                    input_current_email, input_new_nombre, input_new_email
                )
            elif input_usuario_entero == 8:
                input_producto_id = input("Ingrese el ID del producto a actualizar:")
                input_new_nombre = input("Ingrese el nuevo nombre del producto:")
                input_new_precio = input("Ingrese el nuevo precio del producto:")
                input_new_stock = input("Ingrese el nuevo stock del producto:")
                actualizar_producto(
                    input_producto_id,
                    input_new_nombre,
                    input_new_precio,
                    input_new_stock,
                )
            elif input_usuario_entero == 9:
                input_venta_id = input("Ingrese el ID de la venta a eliminar:")
                eliminar_venta(input_venta_id)
            else:
                print("Gracias por usar el sistema.")
                break
        except Exception as e:
            print("Hubo un error al ejecutar la operación: {}".format(e))
        finally:
            conexion.close()


if __name__ == "__main__":
    main()
