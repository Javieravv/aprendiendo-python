# Script para extraer páginas de un archivo pdf. Dividirlo y extraer las páginas.
# Este pedirá el nombre del archivo origen y el rango de páginas.
# Preguntará si quiere los archivos extraídos unidos o en archivos individuales.

import PyPDF2
import os
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main_message():
    clear_screen()
    print("""
        ====================================================================================
        Extraer páginas individuales o grupos de páginas de un archivo PDF

        Extrae una o varias páginas, individuales o un grupo de páginas de un archivo .pdf y 
        los muestra en un único archivo o en archivos individuales.
        ====================================================================================
        """
        )

def parse_page_ranges(input_str):
    """
    Convierte una cadena como '5, 8-9, 15, 25-30'
    en una lista de enteros y tuplas [(5), (8,9), (15), (25,30)].
    """
    page_ranges = []
    for part in input_str.split(","):
        part = part.strip()
        if "-" in part:
            try:
                start, end = map(int, part.split("-"))
                if start <= end:
                    page_ranges.append((start, end))
                else:
                    print(f"⚠️ Rango inválido: {part}. Se omite.")
            except ValueError:
                print(f"⚠️ Formato incorrecto en: {part}. Se omite.")
        else:
            try:
                page_ranges.append(int(part))
            except ValueError:
                print(f"⚠️ Número inválido: {part}. Se omite.")
    return page_ranges

def extract_pages(input_pdf, page_ranges, merge=False):
    """
    Extrae páginas específicas de un PDF y las guarda en archivos separados o en un único archivo.
    
    Parámetros:
    - input_pdf: Nombre del archivo PDF de origen.
    - page_ranges: Lista de números de página o tuplas con rangos.
    - merge: Si es True, fusiona todas las páginas extraídas en un solo archivo.
    """
    if not os.path.exists(input_pdf):
        print(f"❌ Error: El archivo '{input_pdf}' no existe.")
        return
    
    with open(input_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)

        extracted_files = []
        all_pages = PyPDF2.PdfWriter()
        part_number = 1

        for item in page_ranges:
            writer = PyPDF2.PdfWriter()
            
            if isinstance(item, int):  # Página única
                if 1 <= item <= total_pages:
                    writer.add_page(reader.pages[item - 1])
                    all_pages.add_page(reader.pages[item - 1])
                else:
                    print(f"⚠️ Página {item} fuera de rango. Se omite.")

            elif isinstance(item, tuple) and len(item) == 2:  # Rango de páginas
                start, end = item
                if 1 <= start <= end <= total_pages:
                    for i in range(start - 1, end):
                        writer.add_page(reader.pages[i])
                        all_pages.add_page(reader.pages[i])
                else:
                    print(f"⚠️ Rango {start}-{end} fuera de rango. Se omite.")

            if writer.pages and not merge:  # Guarda archivos individuales si no se unen
                output_filename = f"{os.path.splitext(input_pdf)[0]}_part_{part_number}.pdf"
                with open(output_filename, "wb") as output_file:
                    writer.write(output_file)
                extracted_files.append(output_filename)
                part_number += 1

        if merge:  # Guarda todas las páginas extraídas en un solo archivo
            merged_filename = f"{os.path.splitext(input_pdf)[0]}_unido.pdf"
            with open(merged_filename, "wb") as merged_file:
                all_pages.write(merged_file)
            print(f"✅ Páginas extraídas y combinadas en: {merged_filename}")
        else:
            print("✅ Páginas extraídas en archivos separados:", extracted_files)

# 🚀 Programa principal
if __name__ == "__main__":
    main_message()
    print("Dividir archivo PDF")
    input_pdf = input("Ingrese el nombre del archivo PDF: ").strip()
    if not input_pdf.lower().endswith(".pdf"):
        input_pdf += ".pdf"

    page_input = input("Ingrese las páginas o rangos a extraer (ejemplo: 5, 8-9, 15, 25-30): ").strip()
    page_ranges = parse_page_ranges(page_input)

    if not page_ranges:
        print("❌ No se ingresaron páginas válidas. Saliendo...")
    else:
        merge_choice = input("¿Quieres unir las páginas extraídas en un solo archivo? (S/N): ").strip().lower()
        merge = merge_choice == "s"
        extract_pages(input_pdf, page_ranges, merge)
    
    print("He terminado....")
    time.sleep(2)
