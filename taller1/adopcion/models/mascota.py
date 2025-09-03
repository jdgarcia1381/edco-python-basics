class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.adoptado = False

    def __str__(self):
        texto_adpotado = "Sí" if self.adoptado else "No"
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Adoptado: {texto_adpotado}"
