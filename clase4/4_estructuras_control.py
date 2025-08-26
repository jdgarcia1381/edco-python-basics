def main():
    print("Hello World")


if __name__ == "__main__":
    main()


condicion = True
otra_condicion = True

# Estructura básica
if condicion:
    # Código si la condición es True
    print("condicion es True")
elif otra_condicion:
    # Código si otra_condicion es True
    print("otra_condicion es True")
else:
    # Código si ninguna condición es True
    print("Ninguna condición es True")

# Ejemplo
edad = 16
if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Acabas de cumplir la mayoría de edad")
else:
    print("Eres mayor de edad")


nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")


# Operadores lógicos
edad = 15
tiene_carnet = True
if edad >= 18 and tiene_carnet:
    print("Puede conducir")
else:
    print("No puede conducir")


# Condicionales anidados
edad = 20
es_estudiante = True
if edad >= 18:
    print("Eres mayor de edad")
    if es_estudiante:
        print("Tienes descuento de estudiante")
    else:
        print("No tienes descuento")
else:
    print("Eres menor de edad")
    print("Tienes descuento de menor")


# Operador ternario
condicion = True
resultado = 10 if condicion else 5

resultado = 0
if condicion:
    resultado = 10
else:
    resultado = 5

# Sintaxis
# resultado = valor_si_verdadero if condicion else valor_si_falso
# Ejemplos
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)  # Mayor de edad
# Equivalente a:
if edad >= 18:
    mensaje = "Mayor de edad"
else:
    mensaje = "Menor de edad"


# Bucles for
# Iterar sobre una secuencia (lista, tupla, cadena, etc.)
frutas = ["manzana", "fresa"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")
# Me gusta la manzana
# Me gusta la fresa

# Iterar sobre un rango de números
lista_numeros = [0, 1, 2, 3, 4]  # es equivalente a range(5)
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)
for i in range(2, 5):  # 2, 3, 4
    print(i)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Iterar sobre diccionarios
estudiante = {"nombre": "Laura", "edad": 22}
for clave in estudiante:
    print(f"{clave}: {estudiante[clave]}")
# O mejor:
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")


termino_busqueda = "fresa"
frutas = [
    {"nombre": "manzana"},
    {"nombre": "piña"},
    {"nombre": "fresa"},
    {"nombre": "kiwi"},
    {"nombre": "mango"},
]
print(len(frutas))
for fruta in frutas:
    if fruta["nombre"] == termino_busqueda:
        print("Encontré la fresa")
        # TODO: hacer algo con la fresa
        break
else:
    print("No encontré la fresa")

for i in range(5):
    if i == 2:
        continue
    print(i)  # 0, 1, 3, 4
else:
    print("Bucle terminado")


condicion = True
# Bucles while
# Estructura básica
# while condicion:
#     # Código a repetir
#     # ...
#     pass

# Ejemplo: contar hasta 5
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1  # o contador += 1
# continuo acá

# Ejemplo: validación de entrada
respuesta = ""
while respuesta != "si":
    respuesta = input("¿Terminaste? (si/no): ")


# Ejercicio práctico:
estudiantes_list = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Carlos", "nota": 92},
    {"nombre": "Elena", "nota": 78},
    {"nombre": "David", "nota": 65},
    {"nombre": "Laura", "nota": 90},
]

for estudiante_obj in estudiantes_list:
    if estudiante_obj["nota"] >= 70:
        print(estudiante_obj["nombre"])


# Solución recomendada:
def filtrar_aprobados(lista, nota_minima=70):
    aprobados = []
    for estudiante in lista:
        if estudiante["nota"] >= nota_minima:
            aprobados.append(estudiante)
    return aprobados


# Llamar a la función
aprobados = filtrar_aprobados(estudiantes_list)

for e in aprobados:
    print(f"{e['nombre']}: {e['nota']}")
# Resultado:
# Ana: 85
# Carlos: 92
# Elena: 78
# Laura: 90
