# Script para extraer páginas de un archivo pdf. Dividirlo y extraer las páginas.

import PyPDF2

def extract_pages(input_pdf, output_prefix, page_ranges):
    """
    Extrae páginas específicas de un PDF y las guarda en archivos separados.

    Parámetros:
    - input_pdf: Ruta del archivo PDF de entrada.
    - output_prefix: Prefijo del nombre de los archivos de salida.
    - page_ranges: Lista de números de página o tuplas con rangos (basados en índice 1).

    Ejemplo de uso:
    extract_pages("documento.pdf", "parte_extraida", [5, (8, 10), 12, (15, 18)])
    """
    with open(input_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)

        extracted_files = []
        part_number = 1

        for item in page_ranges:
            writer = PyPDF2.PdfWriter()
            
            if isinstance(item, int):  # Página única
                if 1 <= item <= total_pages:
                    writer.add_page(reader.pages[item - 1])
                else:
                    print(f"⚠️ Página {item} fuera de rango. Se omite.")

            elif isinstance(item, tuple) and len(item) == 2:  # Rango de páginas
                start, end = item
                if 1 <= start <= end <= total_pages:
                    for i in range(start - 1, end):
                        writer.add_page(reader.pages[i])
                else:
                    print(f"⚠️ Rango {start}-{end} fuera de rango. Se omite.")

            if writer.pages:
                output_filename = f"{output_prefix}_part_{part_number}.pdf"
                with open(output_filename, "wb") as output_file:
                    writer.write(output_file)
                extracted_files.append(output_filename)
                part_number += 1

        print("✅ Páginas extraídas con éxito en los archivos:", extracted_files)

# Ejemplo de uso:
doc_pdf = "Coautoría - Jurisprudencia Relevante AÑO 2024.pdf"

# extract_pages(doc_pdf, "par_ext", [(1, 87), (88, 129), (130, 282), (283, 309)])
extract_pages(doc_pdf, "pag_ext", [1, 88, 130, 283])


