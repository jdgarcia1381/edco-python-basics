from datetime import datetime

from database import conexion


def listar_clientes():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes_list = cursor.fetchall()
    for cliente in clientes_list:
        print(cliente)


def listar_productos():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos_list = cursor.fetchall()
    for producto in productos_list:
        print(producto)


def listar_ventas():
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT v.id, c.nombre, p.nombre, v.cantidad, v.fecha_venta FROM ventas v JOIN clientes c ON v.cliente_id = c.id JOIN productos p ON v.producto_id = p.id"
    )
    ventas_list = cursor.fetchall()
    for venta in ventas_list:
        print(venta)


def agregar_cliente(nombre, correo):
    cursor = conexion.cursor()
    cursor.execute(
        """
        INSERT INTO clientes (nombre, correo)
        VALUES (%s, %s)
        """,
        (nombre, correo),
    )
    conexion.commit()
    print("Se ha creado exitosamente el registro")


def agregar_producto(nombre, precio, stock=0):
    cursor = conexion.cursor()
    cursor.execute(
        """
        INSERT INTO productos (nombre, precio, stock)
        VALUES (%s, %s, %s)
        """,
        (nombre, precio, stock),
    )
    conexion.commit()
    print("Se ha creado exitosamente el registro")


def registrar_venta(cliente_id, producto_id, cantidad):
    cursor = conexion.cursor()
    cursor.execute(
        """
        INSERT INTO ventas (cliente_id, producto_id, cantidad, fecha_venta)
        VALUES (%s, %s, %s, %s)
        """,
        (cliente_id, producto_id, cantidad, datetime.today().strftime("%Y-%m-%d")),
    )
    cursor.execute(
        """
        UPDATE productos
        SET stock = stock - %s
        WHERE id = %s
        """,
        (cantidad, producto_id),
    )
    conexion.commit()
    print("Se ha creado exitosamente el registro")


def actualizar_cliente(correo_actual, nuevo_nombre, nuevo_correo):
    cursor = conexion.cursor()
    cursor.execute(
        """
        UPDATE clientes
        SET nombre = %s, correo = %s
        WHERE correo = %s
        """,
        (nuevo_nombre, nuevo_correo, correo_actual),
    )
    conexion.commit()
    print("Se ha actualizado exitosamente el registro")


def actualizar_producto(producto_id, nombre, precio, stock):
    cursor = conexion.cursor()
    cursor.execute(
        """
        UPDATE productos
        SET nombre = %s, precio = %s, stock = %s
        WHERE id = %s
        """,
        (nombre, precio, stock, producto_id),
    )
    conexion.commit()
    print("Se ha actualizado exitosamente el registro")


def eliminar_venta(venta_id):
    cursor = conexion.cursor()
    cursor.execute(
        """
        DELETE FROM ventas
        WHERE id = %s
        """,
        (venta_id,),
    )
    filas_eliminadas = cursor.rowcount
    print(f"Filas eliminadas: {filas_eliminadas}")
    conexion.commit()
