import os

import mysql.connector

# Crear conexión
conexion = mysql.connector.connect(
    host="201.130.6.1",  # o dirección IP
    user="root",
    password=os.environ.get("MYSQL_PASSWORD"),  # POR SEGURIDAD, NO QUEMAR PASSWORD
    database="prueba_python",
)

# Crear cursor
cursor = conexion.cursor()

# Ejecutar consulta
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS usuarios (
 id INT AUTO_INCREMENT PRIMARY KEY,
 nombre VARCHAR(100) NOT NULL,
 email VARCHAR(100) UNIQUE,
 edad INT
)
"""
)

# Guardar y cerrar
conexion.commit()
conexion.close()
