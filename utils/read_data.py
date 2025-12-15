import csv
import os

def leer_datos_login():
    datos = []
    ruta_csv = os.path.join(os.getcwd(), "data", "login.csv")

    with open(ruta_csv, newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # salta header

        for fila in lector:
            if not fila or len(fila) < 3:
                continue  # ignora filas vacías o mal formadas

            usuario, password, resultado = fila
            datos.append((usuario, password, resultado))

    return datos

