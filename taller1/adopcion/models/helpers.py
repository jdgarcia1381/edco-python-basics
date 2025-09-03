def buscar_mascota(nombre, lista_mascotas):
    for mascota in lista_mascotas:
        if mascota.nombre == nombre:
            return mascota
    return None
