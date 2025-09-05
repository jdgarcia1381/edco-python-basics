import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",  # o dirección IP
    user="root",
    password="Asd!1234",  # POR SEGURIDAD, NO QUEMAR PASSWORD
    database="prueba_python",
)
cursor = conexion.cursor()

# Consulta básica - seleccionar todo
cursor.execute("SELECT * FROM usuarios ORDER BY email DESC LIMIT 10 ")

# Recuperar todos los resultados
todos_usuarios = cursor.fetchall()
for usuario in todos_usuarios:
    print(usuario)  # Tupla con los datos

# Consulta con condiciones
cursor.execute("SELECT nombre, email FROM usuarios")

# Recuperar un solo resultado
primer_usuario = cursor.fetchone()
print("Primer usuario: ", primer_usuario)

conexion.close()
