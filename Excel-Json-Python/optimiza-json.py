import json
print ("VAMOS A OPTIMIZAR ESTE ARCHIVO JSON...")

def process_json(input_file: str, output_file: str):
    print("Iniciando...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    processed_data = []
    
    for entry in data:
        filtered_dates = {key: value for key, value in entry.items() if key not in ["DESPACHO", "UNID JUD"] and value != ""}
        processed_entry = {
            "DESPACHO": entry["DESPACHO"],
            "UNID JUD": entry["UNID JUD"],
            "FECHAS": filtered_dates
        }
        processed_data.append(processed_entry)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, indent=4, ensure_ascii=False)
    
    print(f"Processed JSON saved to {output_file}")
    
def process_json_1(input_file: str, output_file: str):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    processed_data = []
    
    for entry in data:
        filtered_dates = [key for key, value in entry.items() if key not in ["DESPACHO", "UNID JUD"] and value != ""]
        processed_entry = {
            "DESPACHO": entry["DESPACHO"],
            "UNID JUD": entry["UNID JUD"],
            "FECHAS": filtered_dates
        }
        processed_data.append(processed_entry)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(processed_data, f, indent=4, ensure_ascii=False)
    
    print(f"Processed JSON saved to {output_file}")
    

# process_json("TurnosTunja2025.json", "TurnosTunja2025Opt.json")
process_json_1("TurnosTunja2025.json", "TurnosTunja2025Opt1.json")
    