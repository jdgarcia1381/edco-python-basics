import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",  # o dirección IP
    user="root",
    password="Asd!1234",  # POR SEGURIDAD, NO QUEMAR PASSWORD
    database="prueba_python",
)
cursor = conexion.cursor()

# Actualizar un solo registro
cursor.execute(
    """
UPDATE usuarios
SET email = %s, edad = %s
WHERE id = %s
""",
    ("juan.nuevo@ejemplo.co", 60, 2),
)

# Verificar cuántas filas se modificaron
filas_modificadas = cursor.rowcount
print(f"Filas modificadas: {filas_modificadas}")

conexion.commit()
conexion.close()
