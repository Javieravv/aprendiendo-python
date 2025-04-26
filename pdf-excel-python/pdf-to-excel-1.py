import camelot
import pandas as pd

def pdf_tables_to_excel(pdf_path, excel_path):
    try:
        # Extraer tablas del PDF
        tables = camelot.read_pdf(pdf_path, pages="all", flavor="stream")
        
        # Verificar si se encontraron tablas
        if not tables:
            print("No se encontraron tablas en el PDF.")
            return
        
        print(f"Se encontraron {tables.n} tablas en el PDF.")
        
        # Combinar todas las tablas en un solo DataFrame
        combined_df = pd.concat([table.df for table in tables], ignore_index=True)
        
        # Guardar el DataFrame combinado en una hoja de Excel
        combined_df.to_excel(excel_path, index=False)
        
        print(f"Las tablas se han guardado en: {excel_path}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


# Ruta del archivo PDF de entrada
pdf_path = "VacantesFebrero2025.pdf"  # Asegúrate de que el archivo esté en el mismo directorio que el script

# Ruta del archivo Excel de salida
excel_path = "VacantesFebrero2025-1.xlsx"

pdf_tables_to_excel(pdf_path, excel_path)
