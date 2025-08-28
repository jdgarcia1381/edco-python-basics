import math
import os
from datetime import datetime, timedelta

import requests
from calculadora import PI

resultado = math.sqrt(16)  # 4.0
print(resultado)

# from math import cos, pi, sqrt

# resultado = sqrt(16)  # 4.0
# resultado = pi(16)  # 4.0
# resultado = cos(16)  # 4.0

# from math import * # No recomendado
# resultado = sqrt(16) # 4.0

# import math as m
# resultado = m.sqrt(16) # 4.0

# Fecha y hora actual
ahora = datetime.now()
print(ahora)  # 2023-10-25 15:30:45.123456
# Operaciones con fechas
mañana = ahora + timedelta(days=1)
print(mañana)
# Formateo de fechas
print(ahora.strftime("%d/%m/%Y %H:%M"))


print(os.getcwd())  # Directorio actual
# os.mkdir("nueva_carpeta")

print(PI)


def main():
    print("Hello World")


if __name__ == "__main__":
    main()


response = requests.get("https://echo.free.beeceptor.com")
print(response.status_code)
print(response.json())
