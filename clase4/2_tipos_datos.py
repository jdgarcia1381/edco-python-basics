"""LISTAS"""

# Creación de listas
lista_vacia = []
frutas = ["manzana", "banano", "naranja", "mora", "fresa"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", True, 3.14]

# Acceder a elementos (índice desde 0)
print(frutas[0])  # manzana
print(frutas[1])  # banano
print(frutas[-1])  # fresa (último elemento)
# Modificar elementos
frutas[1] = "piña"

# Agregar elemento al final
frutas.append("Kiwi")

# Agregar elemento en una posición específica
frutas.insert(2, "Papaya")

# Eliminar elementos
frutas.remove("mora")
ultima = frutas.pop()  # Elimina y retorna "Kiwi"

# Ordenar lista
frutas.sort()  # ["fresa", "manzana", "piña"]

print(frutas)  # ["manzana", "piña", "fresa"]
print(len(frutas))


"""TUPLAS"""
tupla_vacia = ()
coordenadas = (4.7110, -74.0721)  # Bogotá
dias = ("lunes", "martes", "miércoles", "jueves", "viernes")
tipos_documento = ("CC", "TI", "CE")
tipos_documento = ({"nombre": "CC"}, {}, {})
# Acceder a elementos (igual que listas)
print(coordenadas[0])  # 4.7110
print(dias[1:3])  # ("martes", "miércoles")


"""DICCIONARIOS"""
estudiante = {
    "nombre": "Laura",
    "edad": 22,
    "carrera": "Ingeniería",
    "activo": True,
}
# Acceder a valores
print(estudiante["nombre"])  # Laura
# Modificar valores
estudiante["edad"] = 23
print(estudiante["edad"])  # 23

# Añadir nuevos pares clave-valor
estudiante["ciudad"] = "Medellín"
print(estudiante)

# Eliminar pares
del estudiante["edad"]
print(estudiante)

if "carrera" in estudiante:
    print("La clave carrera existe")

# Obtener todas las claves y valores
print(estudiante.keys())  # dict_keys(['nombre', 'carrera', 'ciudad'])
print(estudiante.values())  # dict_values(['Laura', 'Ingeniería', 'Medellín'])
print(estudiante.items())  # dict_items([('nombre', 'Laura'), ...])


# Funciones
def ordenar_lista(lista_a_ordenar, parametro_prueba, tipo_ordenamiento):
    """Ordena una lista de números de menor a mayor."""
    print("Ordenando lista:", lista_a_ordenar)
    return []  # TODO: implementar ordenamiento


criterio_busqueda = "Juan"
for item in estudiante.items():
    if item["nombre"] == criterio_busqueda:
        print("Estudiante encontrado:", item)
        break

resultado_funcion = ordenar_lista(lista_vacia, criterio_busqueda, "ascendente")  # None
