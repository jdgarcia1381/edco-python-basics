import logging

logger = logging.getLogger(__name__)

# Exceptions
# if x = 5: # SyntaxError
# print(x)

# if x == 5:  # NameError
# print(x)

# resultado = "texto" + 5  # TypeError
# print(resultado)

# resultado = 10 / 0  # ZeroDivisionError


try:
    # Código que podría generar un error
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
    print(f"El resultado es: {resultado}")
except ValueError:
    # Se ejecuta si ocurre un ValueError
    print("Error: Debe ingresar un número válido")
except ZeroDivisionError:
    # Se ejecuta si ocurre un ZeroDivisionError
    print("Error: No se puede dividir por cero")
except Exception as e:
    # Captura cualquier otra excepción
    print(f"Ocurrió un error inesperado: {e}")
else:
    # Se ejecuta si NO ocurre ninguna excepción
    print("Operación realizada con éxito")
finally:
    print("Gracias por usar el programa")
# continua ejecución


class EdadInvalidaError(Exception):
    """Excepción lanzada cuando la edad está fuera del rango permitido"""

    def __init__(self, edad, mensaje="Edad fuera del rango permitido (0-120)"):
        self.edad = edad
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def verificar_edad(edad):
    if not 0 <= edad <= 120:
        raise EdadInvalidaError(edad)
    return f"Edad válida: {edad} años"


try:
    print(verificar_edad(150))
except EdadInvalidaError as e:
    print(f"Error: {e.mensaje}. Valor recibido: {e.edad}")
    logger.error(f"Error: {e.mensaje}. Valor recibido: {e.edad}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
else:
    # Se ejecuta si NO ocurre ninguna excepción
    print(f"Contenido leído: {len(contenido)} caracteres")
finally:
    # Se ejecuta SIEMPRE, haya error o no
    if "archivo" in locals():
        archivo.close()
    print("Proceso completado")
