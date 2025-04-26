# Este script de python cambia el nombre de archivos que hay en el directorio
# donde se ejecuta, así:
#     Ejemplo de nombre: DDP 7225. AP474-2025. RAD 66849..docx
#     - Elimina el DDP 7225. 
#     - Elimina el . que hay al final del nombre

import os
import re

def rename_files():
    pattern = re.compile(r'^DDP \d{4}\. (.+?)(?=\.)\.?')
    directory = os.getcwd()  # Obtiene el directorio actual
    
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            new_name = match.group(1) + os.path.splitext(filename)[1]  # Mantiene la extensión
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            
            try:
                if os.path.exists(new_path):
                    print(f'Error: No se pudo renombrar "{filename}" porque "{new_name}" ya existe.')
                else:
                    os.rename(old_path, new_path)
                    print(f'Renombrado: "{filename}" → "{new_name}"')
            except Exception as e:
                print(f'Error al renombrar "{filename}": {e}. Ese archivo ya existe.')
    print("ARCHIVOS RENOMBRADOS.")

os.system("cls" if os.name == "nt" else "clear")
print("""
=====================================================================
RENOMBRAR ARCHIVOS ESPECÍFICOS
=====================================================================      
      """)
rename_files()
