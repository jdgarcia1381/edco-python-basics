class Refugio:
    def __init__(self):
        self.__mascotas = []

    def registrar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def listar_disponibles(self):
        # Opción 1
        for mascota in self.__mascotas:
            if not mascota.adoptado:
                print(mascota)

        # Opción 2
        # mascotas_disponibles = []
        # for mascota in self.__mascotas:
        #     if not mascota.adoptado:
        #         mascotas_disponibles.append(mascota)
        # for mascota in mascotas_disponibles:
        #     print(mascota)
        # return mascotas_disponibles

    def listar_adoptadas(self):
        for mascota in self.__mascotas:
            if mascota.adoptado:
                print(mascota)

    def asignar_adopcion(self, nombre_mascota, adoptante):
        # Opción 1
        for mascota in self.__mascotas:
            if mascota.nombre == nombre_mascota:
                adoptante.adoptar(mascota)
                return
        print(f"No se encontró una mascota con el nombre {nombre_mascota}.")

        # Opción 2
        # mascota_encontrada = None
        # for mascota in self.__mascotas:
        #     if mascota.nombre == nombre_mascota:
        #         mascota_encontrada = mascota
        #         break
        # if mascota_encontrada:
        #     adoptante.adoptar(mascota)
        # else:
        #     print(f"No se encontró una mascota con el nombre {nombre_mascota}.")
