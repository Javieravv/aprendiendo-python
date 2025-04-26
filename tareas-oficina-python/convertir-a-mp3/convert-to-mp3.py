# Script para convertir archivos .aac y .m4a a 
# formato mp3

import os
import ffmpeg

def convertir_archivos_en_carpeta(carpeta):
    formatos = (".aac", ".m4a")  # Formatos de entrada permitidos
    archivos = [f for f in os.listdir(carpeta) if f.lower().endswith(formatos)]

    if not archivos:
        print("No se encontraron archivos .aac o .m4a en la carpeta.")
        return

    for archivo in archivos:
        ruta_completa = os.path.join(carpeta, archivo)
        nombre_base, _ = os.path.splitext(archivo)
        archivo_mp3 = os.path.join(carpeta, f"{nombre_base}.mp3")

        try:
            print(f"Convirtiendo {archivo} a {nombre_base}.mp3 ...")
            ffmpeg.input(ruta_completa).output(archivo_mp3, format='mp3').run(quiet=True, overwrite_output=True)
            print(f"Convertido: {archivo} → {nombre_base}.mp3")
        except Exception as e:
            print(f"Error al convertir {archivo}: {e}")

# Usar el directorio desde donde se ejecuta el script
os.system("cls" if os.name == "nt" else "clear") #limpiamos pantalla

print("""
====================================================================================
Convertir archivo .AAC y .M4A a .MP3

Convierte los archivos con formato .AAC y .M4A a formato .MP3
====================================================================================

""")

carpeta_audio = os.getcwd()
# Mostramos esos archivos
print("Lista de archivos encontrados en la carpeta, candidatos a ser convertidos:")
for archivo in os.listdir(carpeta_audio):
    print(f" - {archivo}")
convertir_archivos_en_carpeta(carpeta_audio)
