from database import conexion

# Crear cursor
cursor = conexion.cursor()

# Ejecutar consulta
cursor.execute(
    """
CREATE TABLE `clientes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`));
"""
)

# Guardar y cerrar
conexion.commit()
conexion.close()
