# Este escript convierte imagenes JPG a formato PDF.
# Luego toma las imágenes comprimidas y las une en un solo archivo pdf.
# Si hay un archivo llamado CARATULA.PDF en la misma carpeta, lo coloca al comienzo 

from PIL import Image
import os
from fpdf import FPDF
from PyPDF2 import PdfMerger

# --- Configuración ---
CARPETA_ENTRADA = os.getcwd()
CARPETA_SALIDA = os.path.join(CARPETA_ENTRADA, "comprimidas")
ARCHIVO_FINAL = os.path.join(CARPETA_ENTRADA, "resultado.pdf")
CARATULA_PDF = os.path.join(CARPETA_ENTRADA, "CARATULA.PDF")

# Modo texto: mejor calidad para imágenes con texto
# MODO_TEXTO = True
# CALIDAD = 95 if MODO_TEXTO else 85
CALIDAD = 95

# Crear la carpeta de salida si no existe
os.makedirs(CARPETA_SALIDA, exist_ok=True)

def comprimir_imagen(ruta_entrada, ruta_salida, calidad=95):
    """Comprime una imagen sin cambiar su tamaño y elimina transparencias."""
    with Image.open(ruta_entrada) as img:
        img = img.convert("RGB")  # Asegura compatibilidad y elimina transparencia
        img.save(ruta_salida, optimize=True, quality=calidad)

def convertir_a_pdf(lista_imagenes, archivo_salida):
    """Convierte imágenes a un solo PDF en formato A4 horizontal con márgenes de 1 cm."""
    pdf = FPDF(orientation="L", unit="cm", format="A4")

    for imagen in lista_imagenes:
        with Image.open(imagen) as img:
            ancho_img, alto_img = img.size
            ancho_pagina, alto_pagina = 29.7, 21  # Tamaño A4 horizontal en cm
            margen = 1  # Márgenes de 1 cm
            ancho_disponible = ancho_pagina - (2 * margen)
            alto_disponible = alto_pagina - (2 * margen)

            proporcion = min(ancho_disponible / ancho_img, alto_disponible / alto_img)
            nuevo_ancho = ancho_img * proporcion
            nuevo_alto = alto_img * proporcion

            x_pos = margen + (ancho_disponible - nuevo_ancho) / 2
            y_pos = margen + (alto_disponible - nuevo_alto) / 2

            pdf.add_page()
            pdf.image(imagen, x=x_pos, y=y_pos, w=nuevo_ancho, h=nuevo_alto)

    pdf.output(archivo_salida)

def unir_pdfs(lista_pdfs, archivo_salida):
    """Une varios archivos PDF en uno solo."""
    merger = PdfMerger()
    
    for pdf in lista_pdfs:
        if os.path.exists(pdf):
            merger.append(pdf)

    merger.write(archivo_salida)
    merger.close()

def main():
    """Función principal que procesa las imágenes y genera el PDF final con la carátula."""
    imagenes_comprimidas = []

    for archivo in os.listdir(CARPETA_ENTRADA):
        if archivo.lower().endswith((".jpg", ".jpeg", ".png")) and archivo not in ["resultado.pdf", "CARATULA.PDF"]:
            ruta_original = os.path.join(CARPETA_ENTRADA, archivo)
            ruta_comprimida = os.path.join(CARPETA_SALIDA, archivo)

            comprimir_imagen(ruta_original, ruta_comprimida, calidad=CALIDAD)
            imagenes_comprimidas.append(ruta_comprimida)

    pdf_imagenes = os.path.join(CARPETA_SALIDA, "imagenes.pdf")
    
    if imagenes_comprimidas:
        convertir_a_pdf(imagenes_comprimidas, pdf_imagenes)

        lista_pdfs = [CARATULA_PDF, pdf_imagenes] if os.path.exists(CARATULA_PDF) else [pdf_imagenes]
        unir_pdfs(lista_pdfs, ARCHIVO_FINAL)
        
        print(f"✅ PDF generado exitosamente: {ARCHIVO_FINAL}")
    else:
        print("⚠️ No se encontraron imágenes para procesar.")

if __name__ == "__main__":
    main()
