# 📄 Script: Conversor de Imágenes a PDF con Carátula y Compresión Final

Este script convierte imágenes (JPG, PNG, JPEG) en un único archivo PDF horizontal A4, les aplica compresión, y opcionalmente antepone una carátula si encuentra el archivo `CARATULA.PDF` en la misma carpeta.

---

## ✅ Requisitos

### Librerías de Python (instalar una vez)

Abre la terminal o consola y ejecuta:

```bash
pip install pillow fpdf PyPDF2
```

### Ghostscript

Ghostscript se usa para comprimir el PDF final. Debes instalarlo dependiendo del sistema operativo:

- **Windows**:  
  Descarga desde: https://www.ghostscript.com/download/gsdnld.html  
  Asegúrate de agregar `gswin64c.exe` (usualmente ubicado en `C:\Program Files\gs\...\bin`) al **PATH del sistema**.

- **macOS**:  
  Si tienes [Homebrew](https://brew.sh/) instalado, puedes hacer:

  ```bash
  brew install ghostscript
  ```

---

## 📂 Archivos esperados

Coloca este script en una carpeta junto con las imágenes a convertir. También puedes incluir un archivo llamado:

- `CARATULA.PDF` (opcional): Se usará como la primera página del PDF.

---

## 🚀 ¿Qué hace el script?

1. Comprime las imágenes sin perder demasiada calidad.
2. Convierte las imágenes comprimidas a un PDF horizontal con márgenes.
3. Si existe `CARATULA.PDF`, lo antepone al PDF generado.
4. Comprime el PDF final con Ghostscript.
5. El resultado final es un archivo llamado `resultado.pdf`.

---

## ⚠️ Notas importantes

### Windows

- El script ya detecta si estás en Windows (`os.name == "nt"`) y usa `gswin64c`.
- Asegúrate de que el nombre del archivo sea **exactamente** `CARATULA.PDF` (sin `.pdf.pdf`).
- No guardes ni ejecutes el script en carpetas protegidas como `C:\Archivos de programa`.

### macOS

- El script utiliza `gs` como comando para Ghostscript (funciona bien con Homebrew).
- Todas las rutas se manejan automáticamente con `os.path`.

---

## 📘 Ejecución

### Windows (doble clic o desde terminal)

```bash
python nombre_del_script.py
```

### macOS/Linux (desde Terminal)

```bash
python3 nombre_del_script.py
```

---

## 🧼 Limpieza automática

El script borra archivos temporales como:

- Imágenes WebP intermedias
- PDF sin comprimir (`temp_imagenes.pdf`)
- Copias temporales después de la compresión

---

## 📌 Créditos

Script creado y mejorado por Javier, usando Python para automatizar tareas jurídicas y administrativas de forma eficiente.  
Versión actual: **Mayo 2025**