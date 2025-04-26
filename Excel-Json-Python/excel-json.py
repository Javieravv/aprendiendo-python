# Ejercicio para pasar datos de excel a json
import pandas as pd
import json

print("Vamos a pasar datos de excel a json")

# ============================================
# Función para convertir archivos excel a JSON
# ============================================

def excel_to_json (file_path, sheet_name, ouput_file):
    # Leer la hoja de excel
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    # Convertir el dataframe a una lista de diccionario
    data = df.to_dict(orient='records')
    # Guardar datos en un archivo JSON
    with open(ouput_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
        
    print(f"Datos convertidos y guardados en {ouput_file}")
    

# Ejecutar la función
file_path = 'ListaTurnos2025.xlsx'
sheet_name = 'Tunja'
output_file = 'TurnosTunja2025.json'
excel_to_json(file_path, sheet_name, output_file)

