def main():
    print("Hello World")


if __name__ == "__main__":
    main()


# Definición básica de una clase
class NombreDeLaClase:
    # Atributos de clase (compartidos por todas las instancias)
    atributo_clase = 10

    # Método inicializador
    def __init__(self, parametro1, parametro2):
        # Atributos de instancia (específicos de cada objeto)
        self.atributo1 = parametro1
        self.atributo2 = parametro2

    # Métodos de la clase
    def metodo(self, parametros):
        # Código que implementa el comportamiento
        return resultado


class Automovil:
    atributo_clase = "Vehículo"

    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        return f"{self.anio} {self.marca} {self.modelo}"


auto_toyota = Automovil("Toyota", "Corolla", 2022)
print(auto_toyota.atributo_clase)
print(auto_toyota.descripcion())
print(auto_toyota.marca)
auto_mazda = Automovil("Mazda", "3", 2021)


class Estudiante:
    # Atributo de clase
    universidad = "Universidad de los Andes"

    # Método inicializador con atributos de instancia
    def __init__(self, nombre, codigo, semestre):
        self.nombre = nombre
        self.codigo = codigo
        self.semestre = semestre
        self.materias = []  # Lista vacía por defecto

    # Método para matricular una materia
    def matricular_materia(self, materia):
        self.materias.append(materia)
        print(f"{self.nombre} ha matriculado {materia}")

    # Método para mostrar información del estudiante
    def mostrar_info(self):
        return f"Estudiante: {self.nombre}, Código: {self.codigo}, Semestre: {self.semestre}"

    def __str__(self):
        return f"Estudiante: {self.nombre}, Código: {self.codigo}, Semestre: {self.semestre}, Materias: {self.materias}"

    def __eq__(self, otro):
        return self.codigo == otro.codigo and self.nombre == otro.nombre


# Creando objetos (instancias) de la clase Estudiante
estudiante1 = Estudiante("Ana García", "20211034567", 3)
estudiante2 = Estudiante("Carlos López", "20221045678", 1)
print(estudiante2.materias)

# Accediendo a los atributos
print(estudiante1.nombre)  # Ana García
print(estudiante1.universidad)  # Universidad de los Andes
print(estudiante2.semestre)  # 1

estudiante1.matricular_materia("Matemáticas")
print(estudiante1.materias)  # ['Matemáticas']
print(estudiante2.materias)
print(type(estudiante1))  # <class '__main__.Estudiante'>


# nuevo_objeto = Estudiante()  # Error: faltan argumentos
# nuevo_objeto = Estudiante()  # Error: faltan argumentos
print(estudiante1)

if estudiante1 == estudiante2:
    print("Son el mismo estudiante")


# Ejercicio práctico:
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"'{self.titulo}' ha sido prestado.")
        else:
            print(f"'{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        if self.disponible:
            print(f"'{self.titulo}' ya está en la biblioteca.")
        else:
            self.disponible = True
            print(f"'{self.titulo}' ha sido devuelto.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")
        print(f"Estado: {estado}")

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.anio_publicacion})"


# Crear instancias de la clase Libro
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
print("--- Información inicial de los libros ---")
libro1.mostrar_info()
libro2.mostrar_info()
print("\n--- Prestando libros ---")
libro1.prestar()
libro2.prestar()
libro2.prestar()  # Intentar prestar un libro no disponible
print("\n--- Información de los libros después de prestar ---")
libro1.mostrar_info()
libro2.mostrar_info()
print("\n--- Devolviendo libros ---")
libro1.devolver()
libro3.devolver()  # Intentar devolver un libro ya disponible
print("\n--- Información final de los libros ---")
libro1.mostrar_info()
libro3.mostrar_info()


# Herencia
class ClaseBase:
    # Atributos y métodos de la clase base
    pass


class ClaseDerivada(ClaseBase):
    # La clase derivada hereda todo de ClaseBase
    # Y puede añadir nuevos atributos y métodos
    # O modificar los existentes
    pass


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."


class Estudiante(Persona):
    def __init__(self, nombre, edad, codigo, carrera):
        # Llamamos al inicializador de la clase padre
        super().__init__(nombre, edad)
        # Añadimos atributos específicos de Estudiante
        self.codigo = codigo
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."


estudiante = Estudiante("Laura Gómez", 20, "2023102030", "Ingeniería de Sistemas")
# Método heredado de Persona
print(estudiante.presentarse())
# Salida: Hola, me llamo Laura Gómez
# y tengo 20 años.
# Método propio de Estudiante
print(estudiante.estudiar())
# Salida: Laura Gómez está estudiando
# Ingeniería de Sistemas.

persona = Persona("Carlos Pérez", 30)
persona.presentarse()
# persona.estudiar()  # Error: Persona no tiene el método estudiar


class EmpleadoTiempoCompleto:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario base: {self.salario_base}"


class EmpleadoConComision(EmpleadoTiempoCompleto):
    def __init__(self, nombre, salario_base, comisiones):
        super().__init__(nombre, salario_base)  # Llama al __init__ del padre
        self.comisiones = comisiones

    def calcular_salario(self):
        # Usa el método del padre y le añade las comisiones
        return super().calcular_salario() + self.comisiones


empleado_tiempo_completo = EmpleadoTiempoCompleto("Ana", 3000)
print(empleado_tiempo_completo.calcular_salario())  # 3000
print(empleado_tiempo_completo)

empleado_con_comision = EmpleadoConComision("Luis", 2000, 500)
print(empleado_con_comision.calcular_salario())  # 2500
print(empleado_con_comision)
