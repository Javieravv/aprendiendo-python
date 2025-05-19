# Script para convertir imágenes a PDF, agregar una carátula si existe,
# y comprimir el resultado final (requiere Ghostscript instalado).
# Versión optimizada para mantener calidad de texto y ser compatible con macOS.
# Verión terminada en May-18-2-25

from PIL import Image
from fpdf import FPDF
from PyPDF2 import PdfMerger
import os
import subprocess
import time

def comprimir_imagen(ruta_entrada, calidad=90):
    """Comprime una imagen JPG o PNG sin redimensionar ni perder calidad legible."""
    carpeta_comprimidas = os.path.join(os.getcwd(), "comprimidas")
    os.makedirs(carpeta_comprimidas, exist_ok=True)

    with Image.open(ruta_entrada) as img:
        img = img.convert("RGB")  # Asegura que sea compatible con FPDF (sin transparencias ni metadatos)

        nombre_base = os.path.splitext(os.path.basename(ruta_entrada))[0]
        ruta_salida_jpg = os.path.join(carpeta_comprimidas, f"{nombre_base}_compressed.jpg")

        img.save(ruta_salida_jpg, format="JPEG", optimize=True, quality=calidad)

    return ruta_salida_jpg

def convertir_a_pdf(imagenes, nombre_pdf):
    """Convierte imágenes a un solo PDF A4 horizontal con márgenes de 1 cm."""
    pdf = FPDF(orientation='L', unit='cm', format='A4')
    ancho_pagina, alto_pagina = 29.7, 21.0
    margen = 1
    ancho_disponible, alto_disponible = ancho_pagina - 2*margen, alto_pagina - 2*margen

    for imagen in imagenes:
        with Image.open(imagen) as img:
            img_ancho, img_alto = img.size
            escala = min(ancho_disponible / img_ancho, alto_disponible / img_alto)
            nuevo_ancho, nuevo_alto = img_ancho * escala, img_alto * escala

            x_pos = (ancho_pagina - nuevo_ancho) / 2
            y_pos = (alto_pagina - nuevo_alto) / 2

            pdf.add_page()
            pdf.image(imagen, x=x_pos, y=y_pos, w=nuevo_ancho, h=nuevo_alto)

    pdf.output(nombre_pdf)

def unir_pdfs(pdf_caratula, pdf_imagenes, pdf_final):
    """Une la carátula y el PDF generado con imágenes en un solo archivo."""
    merger = PdfMerger()
    if os.path.exists(pdf_caratula):
        merger.append(pdf_caratula)
    merger.append(pdf_imagenes)
    merger.write(pdf_final)
    merger.close()

def comprimir_pdf(pdf_entrada, pdf_salida):
    """Comprime el PDF usando Ghostscript (asegúrate de tenerlo instalado en macOS)."""
    gs_command = [
        "gs",  # En macOS basta con "gs" si instalaste con Homebrew
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/ebook", #ajusta la calidad del PDF. Si se usa screen se reduce más
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={pdf_salida}",
        pdf_entrada
    ]
    subprocess.run(gs_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    os.system("clear")
    print(
    """
    **************************************************************************************
    📄 Convertir imágenes a PDF, unirlas con una carátula si existe, y comprimir el PDF final
    **************************************************************************************
    """)

    carpeta_actual = os.getcwd()

    imagenes = [f for f in os.listdir(carpeta_actual) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

    if not imagenes:
        print("❌ No se encontraron imágenes en la carpeta actual.")
        return

    print("🔄 Comprimiendo imágenes con calidad alta...")
    imagenes_comprimidas = [
        comprimir_imagen(os.path.join(carpeta_actual, img), calidad=95)
        for img in imagenes
    ]

    pdf_imagenes = os.path.join(carpeta_actual, "temp_imagenes.pdf")
    convertir_a_pdf(imagenes_comprimidas, pdf_imagenes)

    pdf_caratula = os.path.join(carpeta_actual, "CARATULA.PDF")
    pdf_final = os.path.join(carpeta_actual, "resultado.pdf")

    if os.path.exists(pdf_caratula):
        print("📎 Se encontró CARATULA.PDF, será añadida al inicio.")
        unir_pdfs(pdf_caratula, pdf_imagenes, pdf_final)
        os.remove(pdf_imagenes)
    else:
        print("⚠️ No se encontró CARATULA.PDF, se usará solo el PDF de imágenes.")
        os.rename(pdf_imagenes, pdf_final)

    print(f"✅ PDF generado: {pdf_final}")

    # Comprimir PDF si Ghostscript está disponible
    pdf_comprimido = os.path.join(carpeta_actual, "resultado_comprimido.pdf")
    print("🔄 Comprimiendo PDF final con Ghostscript...")
    try:
        comprimir_pdf(pdf_final, pdf_comprimido)
        os.remove(pdf_final)
        os.rename(pdf_comprimido, pdf_final)
        print(f"✅ PDF comprimido generado: {pdf_final}")
    except Exception as e:
        print(f"⚠️ No se pudo comprimir el PDF. Verifica si Ghostscript está instalado. Error: {e}")

    print("🎉 Proceso completado.")
    time.sleep(3)

if __name__ == "__main__":
    main()
