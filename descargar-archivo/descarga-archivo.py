# Intentamos descargar un archivo almacenado en una nube
# De este enlace: https://onedrive.live.com/?authkey=%21ADH1nniCVUZfdmM&id=9ACBA858AE40D6BD%21161056&cid=9ACBA858AE40D6BD&parId=root&parQt=sharedby&o=OneUp

import requests
import os

url = "https://onedrive.live.com/?authkey=%21ADH1nniCVUZfdmM&id=9ACBA858AE40D6BD%21161056&cid=9ACBA858AE40D6BD&parId=root&parQt=sharedby&o=OneUp"  # Usa el enlace directo obtenido
response = requests.get(url, allow_redirects=True)

if response.status_code == 200:
    with open("archivo_descargado.docx", "wb") as file:
        file.write(response.content)
    print("Archivo descargado exitosamente.")
else:
    print("Error al descargar el archivo:", response.status_code)
    
file_path = "archivo_descargado.docx"
print(f"Tamaño del archivo descargado: {os.path.getsize(file_path)} bytes")

with open("archivo_descargado.docx", "rb") as file:
    print(file.read(500))  # Imprime los primeros 500 bytes

