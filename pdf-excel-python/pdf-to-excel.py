# Pasar archivo pdf a excel

import fitz
import pandas as pd

def pdf_to_excel (pdf_path, excel_path):
    try:
        pdf_document = fitz.open(pdf_path)
        text_lines = []
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text = page.get_text("text")
            text_lines.extend(text.splitlines())
            
        df = pd.DataFrame(text_lines, columns=["Text"])
        df.to_excel(excel_path, index = False)
        print (f"El archivo excel se ha guardado en {excel_path}")
    except FileNotFoundError:
        print (f"No se encontró el archivo {pdf_path}")
    except Exception as e:
        print(f"Error: no se pudo hallar el archivo pdf en {pdf_path}")


pdf_path = r"D:\Usuarios\Javier\Proyectos-Dev\Python - Aprendiendo\pdf-excel-python\VacantesFebrero2025.pdf"
excel_path = "VacantesFebrero2025.xlsx"

pdf_to_excel(pdf_path, excel_path)