import whisper
import os
import sys

def print_usage():
    print("Uso: python convertir-mp3-a-texto.py <archivo_audio> [modelo] [idioma]")
    print("Ejemplo: python convertir-mp3-a-texto.py audio.mp3 base es")
    sys.exit(1)

if len(sys.argv) < 2:
    print_usage()

audio_path = sys.argv[1]
model_size = sys.argv[2] if len(sys.argv) > 2 else "medium"
idioma = sys.argv[3] if len(sys.argv) > 3 else "es"

if not os.path.isfile(audio_path):
    print(f"Error: el archivo '{audio_path}' no existe.")
    sys.exit(1)

try:
    model = whisper.load_model(model_size)
except Exception as e:
    print(f"Error al cargar el modelo '{model_size}': {e}")
    sys.exit(1)

try:
    result = model.transcribe(audio_path, language=idioma, task="transcribe", verbose=False)
except Exception as e:
    print(f"Error al transcribir el audio: {e}")
    sys.exit(1)

parrafos = []
parrafo_actual = ""
ultimo_fin = 0

for segment in result.get("segments", []):
    inicio = segment["start"]
    texto = segment["text"].strip()
    if inicio - ultimo_fin > 2 and parrafo_actual:
        parrafos.append(parrafo_actual.strip())
        parrafo_actual = texto
    else:
        parrafo_actual += " " + texto
    ultimo_fin = segment["end"]

if parrafo_actual:
    parrafos.append(parrafo_actual.strip())

base_name = os.path.splitext(os.path.basename(audio_path))[0]
output_path = os.path.join(os.path.dirname(audio_path), f"{base_name}_transcripcion.txt")

if os.path.exists(output_path):
    print(f"Advertencia: el archivo '{output_path}' ya existe y será sobrescrito.")

try:
    with open(output_path, "w", encoding="utf-8") as f:
        for p in parrafos:
            f.write(p + "\n\n")
    print(f"Transcripción guardada con párrafos en: {output_path}")
except Exception as e:
    print(f"Error al guardar la transcripción: {e}")
