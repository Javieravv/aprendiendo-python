# Convertir archivos con formato MP3 a texto

Convierte a texto el contenido de un archivo .mp3.

Esto tiene que ver con una biblioteca de ChatGpt

## Pasos importantes.

1. Instalar *FFMpeg* en esta página: https://ffmpeg.org/download.html

2. Instalar whisper y torch
```
pip install git+https://github.com/openai/whisper.git
pip install torch
```

3. Instalar en python ```pydub``` con ```pip install pydub```

2.1. 

## Generar ejecutable, para sistema operativos Windows

  
Para convertir a .exe ejecutar 

```
pyinstaller --onefile --windowed --clean convertir-mp3-a-texto.py
```
