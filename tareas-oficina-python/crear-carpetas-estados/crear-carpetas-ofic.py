# Este script crea una carpeta basada en los parámetro que se le envíen.
# El nombre de la carpeta será un parámetro y el año será otro. 
# Ejemplo: 
#     Nombre: 'E026'
#     Ano: '2025'
# Creará una carpeta llamada 'E026-2025' y dentro de ella dos subcarpetas: 'E026-Word' y 'E026-Pdf'.

import sys
import os

def crear_carpetas(nombre_base, anio):
    carpeta_principal = f"{nombre_base}-{anio}"
    subcarpeta_word = os.path.join(carpeta_principal, f"{nombre_base}-Word")
    subcarpeta_pdf = os.path.join(carpeta_principal, f"{nombre_base}-Pdf")

    try:
        os.makedirs(subcarpeta_word)
        os.makedirs(subcarpeta_pdf)
        print(f"Se creó la carpeta principal '{carpeta_principal}' con las subcarpetas.")
    except FileExistsError:
        print(f"La carpeta '{carpeta_principal}' ya existe.")
    except Exception as e:
        print(f"Error al crear las carpetas: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python crear_carpetas.py <nombre_base> <anio>")
        sys.exit(1)

    nombre_base = sys.argv[1]
    anio = sys.argv[2]

    crear_carpetas(nombre_base, anio)
