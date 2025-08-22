import os
import platform

# Obtener información del sistema
sistema = platform.system()
version = platform.version()
directorio = os.getcwd()

print(type(sistema))

# Mostrar información
print("¡Hola mundo desde Python!2")
print(f"Sistema operativo: {sistema}")
print(f"Versión: {version}")
print(f"Directorio actual: {directorio}")
