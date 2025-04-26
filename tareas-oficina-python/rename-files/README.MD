# Renombrar achivos.

Este script se emplea para renombrar archivos existentes en un directorio determinado cuyos nombres cumplen las siguientes características:

```DDP 7225. AP474-2025. RAD 66849..docx```

- Empiezan por DDP + espacio + número de 4 cifras + espacio
- Algunos terminan en ., antes de la extensión.

El script deja el nombre del archivo así:

```AP474-2025. RAD 66849.docx```

Para convertir el script en un archivo ```.exe``` de Windows, se ejecuta este comando:

``` pyinstaller --onefile --console rename-files.py```

Para convertir el script en archivo ```.exe``` de Windows, que permita ser ejecutado desde el explorador de winndows y no desde la termina, entonces ejecutar este comando:

```pyinstaller --onefile --windowed --clean rename-files.py``` 

