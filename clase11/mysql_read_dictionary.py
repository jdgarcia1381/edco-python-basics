import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",  # o dirección IP
    user="root",
    password="Asd!1234",  # POR SEGURIDAD, NO QUEMAR PASSWORD
    database="prueba_python",
)

# Configurar para que devuelva diccionarios
cursor = conexion.cursor(dictionary=True)

# Ejecutar consulta
cursor.execute(
    """
SELECT id, nombre, email
FROM usuarios
"""
)

# Procesar resultados como diccionarios
for fila in cursor.fetchall():
    # Acceso por nombre de columna
    print(f"ID: {fila['id']}")
    print(f"Nombre: {fila['nombre']}")
    print(f"Email: {fila['email']}")
    print("-------------------")

conexion.close()
