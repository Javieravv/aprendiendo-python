from PIL import Image
import os
from PyPDF2 import PdfMerger

# Configuración
input_dir = os.getcwd()  # Carpeta donde se ejecuta el script
output_dir = os.path.join(input_dir, "comprimidas")  # Carpeta para imágenes comprimidas
pdf_filename = os.path.join(input_dir, "imagenes_comprimidas.pdf")  # Archivo PDF final
caratula_pdf = os.path.join(input_dir, "CARATULA.PDF")  # Archivo PDF de la carátula
calidad = 70  # Nivel de compresión (0-100)
tamaño_pagina = (3508, 2480)  # A4 horizontal en píxeles (297x210 mm a 300 DPI)
margen = 100  # Margen en píxeles alrededor de la imagen

# Crear directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Obtener lista de imágenes ordenadas por fecha de creación/modificación
imagenes = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg')) and os.path.isfile(f)]
imagenes.sort(key=lambda x: os.path.getctime(os.path.join(input_dir, x)))  # Ordenar por fecha de creación

# Lista para almacenar imágenes ajustadas para el PDF
imagenes_para_pdf = []

# Procesar imágenes en orden de fecha
for filename in imagenes:
    img_path = os.path.join(input_dir, filename)
    img = Image.open(img_path).convert("RGB")  # Convertir a RGB para PDF
    
    # Comprimir y guardar la imagen
    output_path = os.path.join(output_dir, filename)
    img.save(output_path, "JPEG", quality=calidad, optimize=True)

    # Redimensionar manteniendo la relación de aspecto
    img.thumbnail((tamaño_pagina[0] - 2 * margen, tamaño_pagina[1] - 2 * margen))

    # Crear una página en blanco (A4 horizontal) y centrar la imagen
    hoja = Image.new("RGB", tamaño_pagina, "white")  # Página blanca
    pos_x = (tamaño_pagina[0] - img.width) // 2
    pos_y = (tamaño_pagina[1] - img.height) // 2
    hoja.paste(img, (pos_x, pos_y))

    # Guardar la imagen ajustada en la lista para PDF
    imagenes_para_pdf.append(hoja)
    print(f"Imagen procesada: {filename} (ordenada por fecha)")

# Guardar imágenes como PDF temporal con tamaño A4 horizontal
imagenes_pdf_temp = os.path.join(output_dir, "imagenes_temp.pdf")
if imagenes_para_pdf:
    imagenes_para_pdf[0].save(imagenes_pdf_temp, save_all=True, append_images=imagenes_para_pdf[1:])
    print(f"📄 Imágenes convertidas a PDF: {imagenes_pdf_temp}")

# Unir CARÁTULA.PDF + imágenes en el PDF final
merger = PdfMerger()

if os.path.exists(caratula_pdf):
    merger.append(caratula_pdf)  # Agregar la carátula primero
    print(f"✅ CARÁTULA.PDF agregada sin modificaciones.")

if os.path.exists(imagenes_pdf_temp):
    merger.append(imagenes_pdf_temp)  # Agregar imágenes después

merger.write(pdf_filename)
merger.close()

print(f"📄 PDF final creado con éxito: {pdf_filename}")
