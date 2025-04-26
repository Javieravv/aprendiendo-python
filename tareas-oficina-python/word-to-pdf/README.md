# Convertir archivos de Word a PDF.

Este script se emplea para convertir los archivos en formato Word existentes en un directorio determinado a PDF.

Para convertir el script en un archivo ```.exe``` de Windows, se ejecuta este comando:

``` pyinstaller --onefile --console word-to-pdf.py```

Para convertir el script en archivo ```.exe``` de Windows, que permita ser ejecutado desde el explorador de winndows y no desde la termina, entonces ejecutar este comando:
```
pyinstaller --onefile convert-to-mp3.py

```
O también ejecutar: ```pyinstaller --onefile --windowed --clean word-to-pdf.py```, caso en el cual no se abrirá la consola.
