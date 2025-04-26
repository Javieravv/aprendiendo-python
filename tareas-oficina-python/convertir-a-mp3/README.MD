# Convertir archivos en formato .AAC ó .M4A a formato MP3

Convierte todos los archivos que estén en el directorio donde se ejecute el script o el archivo .exe a formato .mp3.

## Pasos importantes.

1. Instalar *FFMpeg* en esta página: https://ffmpeg.org/download.html

Para istalarlo en Windows 11 se deben seguir estos pasos:


2. Instalar en python ```pydub``` con ```pip install pydub```

2.1. Ir a la página oficial: https://ffmpeg.org/download.html

2.2. En la sección Get packages & executable files, hacer clic en Windows.

2.3. Descargar la versión "ffmpeg-master-latest-win64-gpl.zip" desde https://www.gyan.dev/ffmpeg/builds/.

2.4. Extraer  el archivo .zip en una ubicación fácil de acceder, como ```C:\ffmpeg```

Asegurarse  de que la ruta contenga la carpeta bin dentro: ```C:\ffmpeg\bin\ffmpeg```exe

2.5. Agregar al path de windows la ruta donde está el ejecutable de ffmpeg.

Esto no podrá hacerse si el computador tiene restriccione adoptadas por la organización.


3. Convertir el secript a archivo ejecutable de Windows.
   
Para convertir a .exe ejecutar 

```
pyinstaller --onefile --windowed --clean convert-to-mp3.py
```
