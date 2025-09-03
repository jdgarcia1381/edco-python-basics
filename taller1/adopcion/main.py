from models.mascota import Mascota
from models.persona import Adoptante
from models.refugio import Refugio


def main():
    refugio = Refugio()

    mascota1 = Mascota("Firulais", "Perro", 3)
    mascota2 = Mascota("Michi", "Gato", 2)
    mascota3 = Mascota("Nemo", "Pez", 1)

    adoptante1 = Adoptante("Juan", 30)

    refugio.registrar_mascota(mascota1)
    refugio.registrar_mascota(mascota2)
    refugio.registrar_mascota(mascota3)

    # Opción 1: while
    procesar_input_usuario_while(refugio, adoptante1)

    # Opción 2: función recursiva
    # procesar_input_usuario_recursion(refugio, adoptante1)


def procesar_input_usuario_while(refugio, adoptante1):
    while True:
        input_usuario = input(
            "\nIngrese el número de la acción:\n1. Listar mascotas disponibles.\n2. Adoptar una mascota por nombre.\n3. Ver las mascotas adoptadas.\n4. Salir.\n"
        )

        try:
            input_usuario_entero = int(input_usuario)
        except ValueError:
            print("Por favor, ingrese un número válido.")

        if input_usuario_entero == 1:
            refugio.listar_disponibles()
        elif input_usuario_entero == 2:
            input_nombre_mascota = input(
                "Ingrese el nombre de la mascota que desea adoptar:\n"
            )
            refugio.asignar_adopcion(input_nombre_mascota, adoptante1)
        elif input_usuario_entero == 3:
            refugio.listar_adoptadas()
        else:
            print("Gracias por usar el sistema de adopción.")
            break


def procesar_input_usuario_recursion(refugio, adoptante1):
    input_usuario = input(
        "\nIngrese el número de la acción:\n1. Listar mascotas disponibles.\n2. Adoptar una mascota por nombre.\n3. Ver las mascotas adoptadas.\n4. Salir.\n"
    )

    try:
        input_usuario_entero = int(input_usuario)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        procesar_input_usuario_recursion(refugio, adoptante1)
        return

    if input_usuario_entero == 1:
        refugio.listar_disponibles()
    elif input_usuario_entero == 2:
        input_nombre_mascota = input(
            "Ingrese el nombre de la mascota que desea adoptar:\n"
        )
        refugio.asignar_adopcion(input_nombre_mascota, adoptante1)
    elif input_usuario_entero == 3:
        refugio.listar_adoptadas()

    if input_usuario_entero == 4:
        print("Gracias por usar el sistema de adopción.")
    else:
        procesar_input_usuario_recursion(refugio, adoptante1)


if __name__ == "__main__":
    main()
