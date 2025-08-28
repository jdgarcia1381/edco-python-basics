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


# Poliformismo
class Animal:
    def hacer_sonido(self):
        pass  # Método base que será sobrescrito


class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"


class Vaca(Animal):
    def hacer_sonido(self):
        return "¡Muuu!"


class Loro(Animal):
    def hacer_sonido(self):
        return "¡Muuu!"


# Lista de animales de diferentes clases
animales = [Perro(), Gato(), Vaca(), Loro()]
# Polimorfismo en acción
for animal in animales:
    print(animal.hacer_sonido())  # Cada animal hace su sonido específico


# Encapsulamiento
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular  # Público - accesible para todos
        self._saldo = saldo_inicial  # Protegido - solo para uso interno
        self.__pin = "0000"  # Privado - muy restringido

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad, pin):
        if pin == self.__pin and cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False

    def obtener_saldo(self):
        return self._saldo

    def cambiar_pin(self, pin_actual, pin_nuevo):
        if pin_actual == self.__pin:
            self.__pin = pin_nuevo
            return True
        return


cuenta_bancaria = CuentaBancaria("Juan Pérez", 1000)
cuenta_bancaria.depositar(500)
cuenta_bancaria.retirar(200, "0000")

cuenta = CuentaBancaria("Ana López", 1000000)
# Acceso a atributo público
print(cuenta.titular)  # Ana López
# Interfaz pública para interactuar con la cuenta
cuenta.depositar(500000)
print(cuenta.obtener_saldo())  # 1500000
exito = cuenta.retirar(200000, "0000")
if exito:
    print("Retiro exitoso")
else:
    print("Retiro fallido")
# Intento de acceso directo (no recomendado)
print(cuenta._saldo)  # Funciona, pero viola encapsulamiento
# Intento de acceso a atributo privado
# print(cuenta.__pin)  # Error!
# El nombre real es _CuentaBancaria__pin


# Properties
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0 and nueva_edad < 120:
            self._edad = nueva_edad
        else:
            raise ValueError("Edad inválida")

    @property
    def nombre(self):
        return self._nombre


# Uso
persona = Persona("Carlos", 25)
print(persona.edad)  # Usa el getter -> 25
persona.edad = 30  # Usa el setter
try:
    persona.edad = -5  # Lanza una excepción
except ValueError:
    print("Intento de asignar una edad inválida")
print(persona.edad)


# Caso práctico: Sistema de Biblioteca
class Libro:
    def __init__(self, titulo, autor, año_publicacion, isbn):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self._isbn = isbn  # Protegido
        self._disponible = True  # Protegido
        self._veces_prestado = 0  # Protegido

    @property
    def disponible(self):
        return self._disponible

    @property
    def isbn(self):
        return self._isbn

    def prestar(self):
        if self._disponible:
            self._disponible = False
            self._veces_prestado += 1
            return True
        return False

    def devolver(self):
        if not self._disponible:
            self._disponible = True
            return True
        return False

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

    def __eq__(self, otro):
        return isinstance(otro, Libro) and self._isbn == otro._isbn


variable_libro_2 = Libro("1984", "George Orwell", 1949, "123-456-7892")
variable_libro = Libro("1984", "George Orwell", 1949, "123-456-789")
if variable_libro_2 == variable_libro:
    print("Son iguales")
else:
    print("No son iguales")


class LibroFisico(Libro):
    def __init__(
        self, titulo, autor, año_publicacion, isbn, ubicacion, estado_fisico="Bueno"
    ):
        super().__init__(titulo, autor, año_publicacion, isbn)
        self.ubicacion = ubicacion  # Ej: "Estante A-3"
        self.estado_fisico = estado_fisico

    def mostrar_info(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"{self} - Ubicación: {self.ubicacion}, Estado: {estado}, Condición: {self.estado_fisico}"


class LibroDigital(Libro):
    def __init__(self, titulo, autor, año_publicacion, isbn, formato, tamaño_mb):
        super().__init__(titulo, autor, año_publicacion, isbn)
        self.formato = formato  # Ej: "PDF", "EPUB"
        self.tamaño_mb = tamaño_mb
        self._descargas_simultaneas = 0
        self._max_descargas = 3

    def prestar(self):
        if self._descargas_simultaneas < self._max_descargas:
            self._descargas_simultaneas += 1
            self._veces_prestado += 1
            return True
        return False

    def devolver(self):
        if self._descargas_simultaneas > 0:
            self._descargas_simultaneas -= 1
            return True
        return False

    def mostrar_info(self):
        return f"{self} - Formato: {self.formato}, Tamaño: {self.tamaño_mb}MB, Descargas: {self._descargas_simultaneas}/{self._max_descargas}"


# Crear diferentes tipos de libros
libro_fisico = LibroFisico(
    "Cien años de soledad",
    "Gabriel García Márquez",
    1967,
    "978-84-376-0494-7",
    "Estante A-3",
)
libro_digital = LibroDigital(
    "1984", "George Orwell", 1949, "978-0-452-28423-4", "PDF", 2.5
)

# Lista de libros (polimorfismo)
biblioteca = [libro_fisico, libro_digital]
# Procesar todos los libros de manera uniforme
for libro in biblioteca:
    print(libro.mostrar_info())

    # Prestar libro
    if libro.prestar():
        print(f"{libro} prestado exitosamente")
    else:
        print(f" No se pudo prestar {libro}")

# Comparar libros usando __eq__
libro_fisico2 = LibroFisico(
    "Otra edición", "Otro autor", 2000, "978-84-376-0494-7", "Estante B-1"
)
print(f"¿Son el mismo libro? {libro_fisico == libro_fisico2}")  # True (mismo ISBN)
