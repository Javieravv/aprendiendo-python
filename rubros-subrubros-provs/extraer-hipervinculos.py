import pdfplumber
import fitz  # PyMuPDF
import re
import pandas as pd

def extraer_providencias_y_enlaces(pdf_path):
    data = []

    # Extraer texto y enlaces
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                matches = re.findall(r'(SP\d{3,4}-\d{4}\(\d+\)|AP\d{3,4}-\d{4}\(\d+\))', text)
                
                # Buscar enlaces en la misma página
                doc = fitz.open(pdf_path)
                for link in doc[page_num].get_links():
                    if "uri" in link:
                        url = link["uri"]
                        for match in matches:
                            if match in url:
                                data.append([match, url])

    # Crear DataFrame
    df = pd.DataFrame(data, columns=["Providencia", "Enlace"]).drop_duplicates()

    return df

# Uso
pdf_file = "Boletin Jurisprudencial 2025-02-07"  # Cambia esto con el archivo real
df_resultado = extraer_providencias_y_enlaces(pdf_file)
print(df_resultado)

# Guardar en CSV
df_resultado.to_csv("providencias_enlaces.csv", index=False)
