# Script para convertir imágenes a PDF, unirlas 
# Colocar al comienzo una carátula, siempre y cuando esté el archivo CARATULA.PDF

from PIL import Image
from fpdf import FPDF
import os
import subprocess
import time

def comprimir_imagen(ruta_entrada, calidad=70, usar_webp=False):
    # Comprime una imagen sin cambiar su tamaño, eliminando metadatos y optimizando calidad.
    # Siempre devuelve un archivo JPG compatible con FPDF.
    carpeta_comprimidas = os.path.join(os.getcwd(), "comprimidas")
    os.makedirs(carpeta_comprimidas, exist_ok=True)
    
    with Image.open(ruta_entrada) as img:
        img = img.convert("RGB")  # Elimina transparencias y metadatos
        
        nombre_base = os.path.splitext(os.path.basename(ruta_entrada))[0]
        ruta_salida_webp = os.path.join(carpeta_comprimidas, f"{nombre_base}.webp")
        ruta_salida_jpg = os.path.join(carpeta_comprimidas, f"{nombre_base}_compressed.jpg")
        
        # Si usamos WebP, primero guardamos la imagen en WebP
        if usar_webp:
            img.save(ruta_salida_webp, format="WEBP", optimize=True, quality=calidad)
            img = Image.open(ruta_salida_webp)  # Volvemos a abrirla
        
        # Guardamos en JPG
        img.save(ruta_salida_jpg, format="JPEG", optimize=True, quality=calidad)
    
    return ruta_salida_jpg  # Siempre devolverá un JPG

def convertir_a_pdf(imagenes, nombre_pdf):
    # Convierte imágenes a un solo archivo PDF en formato A4 horizontal con márgenes de 1 cm.
    pdf = FPDF(orientation='L', unit='cm', format='A4')
    ancho_pagina, alto_pagina = 29.7, 21.0  # A4 horizontal
    margen = 1  # Márgenes de 1 cm
    ancho_disponible, alto_disponible = ancho_pagina - 2*margen, alto_pagina - 2*margen
    
    for imagen in imagenes:
        with Image.open(imagen) as img:
            img_ancho, img_alto = img.size
            escala = min(ancho_disponible / img_ancho, alto_disponible / img_alto)
            nuevo_ancho, nuevo_alto = img_ancho * escala, img_alto * escala
            
            x_pos = (ancho_pagina - nuevo_ancho) / 2  # Centrar horizontalmente
            y_pos = (alto_pagina - nuevo_alto) / 2  # Centrar verticalmente
            
            pdf.add_page()
            pdf.image(imagen, x=x_pos, y=y_pos, w=nuevo_ancho, h=nuevo_alto)
    
    pdf.output(nombre_pdf)

def unir_pdfs(pdf_caratula, pdf_imagenes, pdf_final):
    # Une el archivo CARATULA.PDF con el PDF generado a partir de imágenes.
    from PyPDF2 import PdfMerger
    merger = PdfMerger()
    merger.append(pdf_caratula)
    merger.append(pdf_imagenes)
    merger.write(pdf_final)
    merger.close()

def comprimir_pdf(pdf_entrada, pdf_salida):
    # Comprime un archivo PDF usando Ghostscript.
    gs_command = [
        "gswin64c" if os.name == "nt" else "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/screen",
        "-dNOPAUSE",
        "-dBATCH",
        "-sOutputFile=" + pdf_salida,
        pdf_entrada
    ]
    subprocess.run(gs_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(
    """
    **************************************************************************************
    Convertir imágenes a formato PDF, unirlas junto con un archivo que será la portada
    **************************************************************************************
    """)

    carpeta_actual = os.getcwd()
    
    imagenes = [f for f in os.listdir(carpeta_actual) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    
    if not imagenes:
        print("❌ No se encontraron imágenes en la carpeta actual.")
        return
    
    print("🔄 Comprimiendo imágenes...")
    
    imagenes_comprimidas = [comprimir_imagen(os.path.join(carpeta_actual, img), calidad=60, usar_webp=True) for img in imagenes]
    
    pdf_imagenes = os.path.join(carpeta_actual, "temp_imagenes.pdf")
    
    convertir_a_pdf(imagenes_comprimidas, pdf_imagenes)
    
    pdf_caratula = os.path.join(carpeta_actual, "CARATULA.PDF")
    
    if not os.path.exists(pdf_caratula):
        print("⚠️ No se encontró CARATULA.PDF, se generará solo el PDF con imágenes.")
        pdf_final = os.path.join(carpeta_actual, "resultado.pdf")
        os.rename(pdf_imagenes, pdf_final)
    else:
        pdf_final = os.path.join(carpeta_actual, "resultado.pdf")
        unir_pdfs(pdf_caratula, pdf_imagenes, pdf_final)
        os.remove(pdf_imagenes)  # Eliminar el temporal
    
    print(f"✅ PDF generado exitosamente: {pdf_final}")
    
    pdf_comprimido = os.path.join(carpeta_actual, "resultado_comprimido.pdf")
    print("🔄 Comprimiendo PDF final...")
    comprimir_pdf(pdf_final, pdf_comprimido)
    print(f"✅ PDF comprimido generado: {pdf_comprimido}")
    os.remove(pdf_final)  # Eliminar el PDF sin comprimir
    os.rename(pdf_comprimido, pdf_final)  # Renombrar el comprimido como resultado final
    print("🎉 Proceso completado...")

if __name__ == "__main__":
    main()
    time.sleep(3)
