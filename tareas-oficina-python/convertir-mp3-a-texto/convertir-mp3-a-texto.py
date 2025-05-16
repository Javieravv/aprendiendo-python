import whisper
import os
import sys

# Verificar que se haya pasado un archivo por parámetro
if len(sys.argv) < 2:
    print("Uso: python transcribir.py archivo.mp3")
    sys.exit(1)

audio_path = sys.argv[1]

if not os.path.isfile(audio_path):
    print(f"Error: el archivo '{audio_path}' no existe.")
    sys.exit(1)

# Cargar el modelo
model = whisper.load_model("medium")

# Transcripción con idioma español forzado
result = model.transcribe(audio_path, language="es", task="transcribe", verbose=False)

# Construir párrafos a partir de segmentos
parrafos = []
parrafo_actual = ""
ultimo_fin = 0

for segment in result["segments"]:
    inicio = segment["start"]
    texto = segment["text"].strip()

    # Si hay una pausa mayor a 2 segundos, comienza un nuevo párrafo
    if inicio - ultimo_fin > 2 and parrafo_actual:
        parrafos.append(parrafo_actual.strip())
        parrafo_actual = texto
    else:
        parrafo_actual += " " + texto

    ultimo_fin = segment["end"]

# Agrega el último párrafo
if parrafo_actual:
    parrafos.append(parrafo_actual.strip())

# Guardar transcripción con saltos entre párrafos
base_name = os.path.splitext(os.path.basename(audio_path))[0]
output_path = os.path.join(os.path.dirname(audio_path), f"{base_name}_transcripcion.txt")

with open(output_path, "w", encoding="utf-8") as f:
    for p in parrafos:
        f.write(p + "\n\n")

print(f"Transcripción guardada con párrafos en: {output_path}")
