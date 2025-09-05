import mysql.connector

# Establecer la conexión con la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",  # o dirección IP
    user="root",
    password="Asd!1234",  # POR SEGURIDAD, NO QUEMAR PASSWORD
    database="prueba_python",
)
cursor = conexion.cursor()

# Insertar un solo registro
cursor.execute(
    """
INSERT INTO usuarios (nombre, email, edad)
VALUES (%s, %s, %s)
""",
    ("Juan Pérez", "juan3@ejemplo.co", 20),
)

# Insertar múltiples registros
usuarios = [
    ("María López", "maria3@ejemplo.co", 25),
    ("Carlos Gómez", "carlos3@ejemplo.co", 30),
    ("Ana Torres", "ana3@ejemplo.co", 35),
]
cursor.executemany(
    """
INSERT INTO usuarios (nombre, email, edad)
VALUES (%s, %s, %s)
""",
    usuarios,
)

conexion.commit()

print(f"ID generado: {cursor.lastrowid}")

conexion.close()
