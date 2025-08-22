def multiplicar(a, b):
    print(variable1)
    return a * b


variable1 = 5
variable2 = 10
mi_variable_con_cualquier_nombre = multiplicar(variable1, variable2)


def pruebas():
    pass


variable_global = 100


def funcion_nivel1():
    print(variable_global)
    variable_local_1 = 50

    def funcion_nivel2():
        print(variable_global)
        print(variable_local_1)
        variable_local_2 = 25

    print(variable_local_2)


print(variable_local_1)
