def main():
    print("Hello, world!")


if __name__ == "__main__":
    edad = 30
    print(type(edad))
    main()


# Variables y tipos de datos
nombre_completo = "Juan García"
edad = 30
altura = 1.75
altura_pedro = 1.80
altura_str = "1.75"
altura_pedro_str = "1.80"
es_estudiante = False


# Operaciones básicas
valor_inicial = 10
multiplicador = 0.5
resultado = valor_inicial + multiplicador

# Operaciones de comparación
resultado_comparacion_igual = resultado == valor_inicial
resultado_comparacion_diferente = resultado != valor_inicial
resultado_comparacion_menor_igual = resultado <= valor_inicial

resultado = resultado_comparacion_igual and resultado_comparacion_menor_igual
if resultado:
    print("Las 2 comparaciones son True")
resultado_negado = not resultado


es_estudiante = True

if not es_estudiante:
    print("No envío correo promocional")
else:
    print("Envío correo promocional")
