import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",  # o dirección IP
    user="root",
    password="Asd!1234",  # POR SEGURIDAD, NO QUEMAR PASSWORD
    database="prueba_python",
)
cursor = conexion.cursor()

# Eliminar un registro específico
cursor.execute(
    """
DELETE FROM usuarios
WHERE id = %s
""",
    (9,),
)

# Eliminar múltiples registros
cursor.execute(
    """
DELETE FROM usuarios
WHERE edad > %s
""",
    (50,),
)

# Verificar cuántas filas se eliminaron
filas_eliminadas = cursor.rowcount
print(f"Filas eliminadas: {filas_eliminadas}")

conexion.commit()
conexion.close()
