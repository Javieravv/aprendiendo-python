# Convierte archivos .aac  a Mp3

import ffmpeg

def convertir_aac_a_mp3(archivo_aac, archivo_mp3):
    ffmpeg.input(archivo_aac).output(archivo_mp3, format='mp3').run()
    print(f"Archivo convertido: {archivo_mp3}")


print("""
============================================================
Convertir archivos .AAC a .MP3

      """)

archivoaac = "13 oct. 10.21 a. m.​ PVA 2022-042"

convertir_aac_a_mp3(f"{archivoaac}.aac", f"{archivoaac}.mp3")