import sqlite3

# Crear conexión (si la BD no existe, se crea)
conexion = sqlite3.connect("clase11/data/mi_base_datos.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS usuarios (
 id INTEGER PRIMARY KEY,
 nombre TEXT NOT NULL,
 email TEXT UNIQUE,
 edad INTEGER
)
"""
)

# Guardar cambios y cerrar
conexion.commit()
conexion.close()
