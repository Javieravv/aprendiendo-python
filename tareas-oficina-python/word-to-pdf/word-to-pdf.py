import os
import comtypes.client

print("Pasar archivo word a pdf en equipos con SO Widows y con Word Instalado")

def convert_word_to_pdf (docx_file, pdf_file):
    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = False
    doc = None # para evitar UnboundLocalError
    try:
        doc = word.Documents.Open(docx_file)
        doc.SaveAs(pdf_file, FileFormat = 17)
        print(f"Archivo convertido de manera exitosa_ {pdf_file}")
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")
    finally:
        if doc:
            doc.Close()
        word.Quit()
        

# Obtener el directorio actual
directory = os.getcwd()

# filtrar archijvos word
docx_files = [f for f in os.listdir(directory) if f.endswith(".docx")]

if not docx_files:
    print("No se encontraron archivos word en el directorio actual.")
else:
    for docx_file in docx_files:
        docx_path = os.path.join(directory, docx_file)
        pdf_path = os.path.join(directory, os.path.splitext(docx_file)[0])
        convert_word_to_pdf(docx_path, pdf_path)
