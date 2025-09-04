import sqlite3

try:
    # Intentar conectar a la base de datos
    conexion = sqlite3.connect("clase11/data/mi_base_datos.db")
    cursor = conexion.cursor()

    # Operaciones con la base de datos...
    cursor.execute("SELECT * FROM tabla_que_no_existe")

except sqlite3.OperationalError as e:
    print(f"Error de operación: {e}")

except sqlite3.DatabaseError as e:
    print(f"Error de base de datos: {e}")

finally:
    # Este bloque siempre se ejecuta
    if "conexion" in locals():
        conexion.close()
        print("Conexión cerrada")
