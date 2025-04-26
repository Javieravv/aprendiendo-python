# Script hecho en Python para comprimir imágenes, pasarlas a PDF y unirlas en un solo archivo.

Este script de Python toma las imágenes que hay en el directorio donde se ejecuta, las comprime, las convierte a PDF y luego las une en un solo archivo PDF.

También coloca en la primera página del archivo resultante una carátulas, que deberá ser un archivo llamado ```CARATULA.PDF``` que deberá estar en el directorio donde se ejecuta el script.

Para que el script funcione en Windows 11 se deben instalar estas bibliotecas de Python:

1. Pillow
2. FPDF
3. PyDF

```
pip install pillow fpdf pypdf

```

También se deberá instalar en Windows 11 la aplicación ```Ghostcript``` que se encuentra en esta dirección web: https://ghostscript.com/releases/gsdnld.html

Luego de instalada se deberá agregar al Path de windows el directorio donde quedó instalada.

Una vez hecho esto se puede verificar en Windows que todo esté instalado:

```
python -c "import PIL, fpdf, pypdf; print('Librerías OK')"

gswin64c -v  # En Windows (debe mostrar la versión de Ghostscript)

```

## Ejecutar el script desde cualquier directorio.

Para poder ejecutar el script desde cualquier directorio, se debe hacer lo siguiente:

1. Copiar ese script y otros que se quieran en un directorio concreto. Por ejemplo ```C:\Juzgado\Scripts```

2. Crear un archivo llamado ```jpgcompresspdf.bat``` o algo así, con el siguiente código:

```
@echo off
python "D:\Usuarios\Javier\Proyectos-Dev\Python - Aprendiendo\jpg-compress-pdf\jpg-to-pdf-2.py" %*

```

Puede cambiarse ```jpg-to-pdf-2.py``` por cualquier otro nombre que el sctipt tenga.

3. Hecho esto, agrega un valor al Path de variables de entorno de Windows con el directorio donde están los scripts. Para el ejemplo sería ```C:\Juzgado\Scripts```

4. Convertir el script de python en un ejecutable ```.exe``` de Windows.

Ejecutar este comando: ```pyinstaller --onefile jpg-to-pdf.py```



