# Script crear carpetas.

Este es un script que ayuda a una tarea repetitiva empleada en la oficina:

Crear una carpeta que contendrá las providencias de un estado determinado.

Esa carpeta tiene un nombre que se estructura así:

```
<NUMERO ESTADO>-<AÑO>
```

Ejemplo:

```
E001-2025
```

Recibirá dos parámetros:
- Número del Estado
- Año al que corresponde

Creará la carpeta uniendo esos dos parámetros. Y dentro de ella creará dos subcarpetas, que tendrán esta estructura:

```
<NUMERO ESTADO>-Pdf
<NUMERO ESTADO>-Word
```

Para el ejemplo se crearán dos subcarpetas llamadas ```E001-Pdf``` y ```E001-Word```

Es muy básico, pero ayuda mucho.