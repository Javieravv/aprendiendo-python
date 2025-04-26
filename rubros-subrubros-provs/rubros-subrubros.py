import re
import json

# Texto de entrada
texto = """
PRINCIPIO PRO INFANS - Genera exigencias reforzadas de diligencia en el proceso penal, cuando la víctima es menor de edad / 
PRINCIPIO PRO INFANS - Formas de garantizarlo cuando las víctimas son víctimas de delitos sexuales / 
ENFOQUE DE GÉNERO - Obligaciones de las autoridades judiciales: en el ámbito de juzgamiento, impone al fallador valorar la prueba eliminando estereotipos que tratan de universalizar como criterios de racionalidad prejuicios machistas / 
ACCESO CARNAL VIOLENTO - Configuración: no es exigible que la víctima despliegue una acción de resistencia frente al acto sexual no consentido. /
PRINCIPIO PRO INFANS - Genera exigencias reforzadas de diligencia en el proceso penal, cuando la víctima es menor de edad / 
PRINCIPIO PRO INFANS - Formas de garantizarlo cuando las víctimas son víctimas de delitos sexuales / 
ENFOQUE DE GÉNERO - Obligaciones de las autoridades judiciales: en el ámbito de juzgamiento, impone al fallador valorar la prueba eliminando estereotipos que tratan de universalizar como criterios de racionalidad prejuicios machistas. /
SISTEMA PENAL ACUSATORIO - Declaraciones rendidas antes del juicio: entrevista rendida ante psicólogo por menor víctima de delito sexual, es prueba de referencia sobre lo dicho por éste y prueba directa sobre las percepciones del profesional / 
SISTEMA PENAL ACUSATORIO - Declaraciones rendidas antes del juicio, entrevistas, menor víctima de delitos sexuales, incorporación como prueba de referencia para evitar su doble victimización / 
SISTEMA PENAL ACUSATORIO - Declaraciones rendidas antes del juicio: alcance, constituyen prueba de referencia dependiendo del ejercicio del derecho de confrontación. /
ACCESO CARNAL VIOLENTO - Configuración: no es exigible que la víctima despliegue una acción de resistencia frente al acto sexual no consentido. /
SP3240-2024(62446) de 22/11/2024
https://cortesuprema.gov.co/corte/wp-content/uploads/relatorias/pe/b1ene2025/SP3240-2024(62446).pdf
"""

# Expresiones regulares
patron_rubros = re.findall(r'([A-ZÁÉÍÓÚÑ ]+) - ([^/]+)', texto)
patron_providencia = re.search(r'(SP\d{4,}-\d{4}\(\d+\)) de (\d{2}/\d{2}/\d{4})', texto)
patron_enlace = re.search(r'https?://\S+', texto)

# print(patron_rubros[0])
# print(patron_providencia)
# print(patron_enlace)

# Procesar rubros y subrubros
rubros_dict = {}
for rubro, subrubro in patron_rubros:
    rubro = rubro.strip()
    print(rubro)
    subrubro = subrubro.strip()
    print(subrubro)
    if rubro not in rubros_dict:
        rubros_dict[rubro] = []
    if subrubro not in rubros_dict[rubro]:  # Evitar duplicados
        rubros_dict[rubro].append(subrubro)

# Extraer providencia y fecha
providencia = patron_providencia.group(1) if patron_providencia else "No encontrada"
fecha = patron_providencia.group(2) if patron_providencia else "No encontrada"

# Extraer enlace
enlace = patron_enlace.group(0) if patron_enlace else "No encontrado"

# Crear estructura JSON
resultado = {
    "providencia": {
        "numero": providencia,
        "fecha": fecha,
        "enlace": enlace
    },
    "rubros": [{"nombre": rubro, "subrubros": subrubros} for rubro, subrubros in rubros_dict.items()]
}

# Guardar en un archivo JSON
nombre_archivo = "jurisprudencia.json"
with open(nombre_archivo, "w", encoding="utf-8") as archivo_json:
    json.dump(resultado, archivo_json, indent=4, ensure_ascii=False)

print(f"✅ Archivo JSON guardado correctamente como '{nombre_archivo}'")
