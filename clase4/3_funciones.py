def funcion_prueba(parametro1, parametro2):
    variable1 = 10
    if variable1 > 5:
        print("Variable1 es mayor que 5")


def sumar(a, b):
    return a + b


def funcion_con_valores_por_defecto(a, b=2, c=3):
    return a + b + c


funcion_prueba(parametro2=10, parametro1=5)
print(funcion_con_valores_por_defecto(c=5, a=5, b=3))


# *args: Número variable de argumentos posicionales
def sumar_todos(*numeros):
    return sum(numeros)


print(sumar_todos(1, 2, 3, 4, 5, 123, 54, 6))  # 10


# **kwargs: Número variable de argumentos con nombre
def info_persona(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")


info_persona(nombre="Ana", edad=25, ciudad="Cali")
# nombre: Ana
# edad: 25
# ciudad: Cali


# Retornar un valor
def calcular_iva(precio):
    return precio * 0.19


precio_con_iva = calcular_iva(100)
total = precio_con_iva + 100
print(total)


# Retornar múltiples valores
def dividir(a, b):
    cociente = a // b
    resto = a % b
    return cociente, resto


resultado_cociente, resultado_resto = dividir(10, 3)
print("Cociente:", resultado_cociente)  # Cociente: 3
print("Resto:", resultado_resto)  # Resto: 1


# Sin retorno explícito
def saludar(nombre):
    print(f"Hola {nombre}")


resultado_saludar = saludar("Carlos")  # Hola Carlos
print(resultado_saludar)  # None
