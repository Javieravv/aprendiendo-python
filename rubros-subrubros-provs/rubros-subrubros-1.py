import re
import json

def extraer_datos(textos):
    resultados = []
    
    for texto in textos:
        # Extraer la providencia y el enlace
        match_providencia = re.search(r'(SP\d{4}-\d{4}\(\d{5}\)) de (\d{2}/\d{2}/\d{4})', texto)
        match_enlace = re.search(r'(https?://\S+)', texto)
        
        if not match_providencia or not match_enlace:
            continue
        
        providencia = match_providencia.group(1)
        fecha = match_providencia.group(2)
        enlace = match_enlace.group(1)
        
        # Limpiar el texto removiendo la providencia y el enlace
        texto_limpio = texto[:match_providencia.start()].strip()
        
        # Extraer rubros y subrubros
        rubros_dict = {}
        patrones = re.findall(r'([A-ZÁÉÍÓÚÑ ]+?) - (.+?)(?: / |$)', texto_limpio)
        
        for rubro, subrubro in patrones:
            rubro = rubro.strip()
            subrubro = subrubro.strip()
            if rubro not in rubros_dict:
                rubros_dict[rubro] = []
            if subrubro not in rubros_dict[rubro]:  # Evitar duplicados
                rubros_dict[rubro].append(subrubro)
        
        resultados.append({
            "providencia": providencia,
            "fecha": fecha,
            "enlace": enlace,
            "rubros": rubros_dict
        })
    
    return resultados

# Lista de textos con providencias
textos = [
    """PRINCIPIO PRO INFANS - Genera exigencias reforzadas de diligencia en el proceso penal, cuando la víctima es menor de edad / PRINCIPIO PRO INFANS - Formas de garantizarlo cuando las víctimas son víctimas de delitos sexuales / ENFOQUE DE GÉNERO - Obligaciones de las autoridades judiciales: en el ámbito de juzgamiento, impone al fallador valorar la prueba eliminando estereotipos que tratan de universalizar como criterios de racionalidad prejuicios machistas / ACCESO CARNAL VIOLENTO - Configuración: no es exigible que la víctima despliegue una acción de resistencia frente al acto sexual no consentido. PRINCIPIO PRO INFANS - Genera exigencias reforzadas de diligencia en el proceso penal, cuando la víctima es menor de edad / PRINCIPIO PRO INFANS - Formas de garantizarlo cuando las víctimas son víctimas de delitos sexuales / ENFOQUE DE GÉNERO - Obligaciones de las autoridades judiciales: en el ámbito de juzgamiento, impone al fallador valorar la prueba eliminando estereotipos que tratan de universalizar como criterios de racionalidad prejuicios machistas. SISTEMA PENAL ACUSATORIO - Declaraciones rendidas antes del juicio: entrevista rendida ante psicólogo por menor víctima de delito sexual, es prueba de referencia sobre lo dicho por éste y prueba directa sobre las percepciones del profesional / SISTEMA PENAL ACUSATORIO - Declaraciones rendidas antes del juicio, entrevistas, menor víctima de delitos sexuales, incorporación como prueba de referencia para evitar su doble victimización / SISTEMA PENAL ACUSATORIO - Declaraciones rendidas antes del juicio: alcance, constituyen prueba de referencia dependiendo del ejercicio del derecho de confrontación. ACCESO CARNAL VIOLENTO - Configuración: no es exigible que la víctima despliegue una acción de resistencia frente al acto sexual no consentido /
    SP3240-2024(62446) de 22/11/2024
    https://cortesuprema.gov.co/corte/wp-content/uploads/relatorias/pe/b1ene2025/SP3240-2024(62446).pdf""",
    """CONFLICTO ARMADO INTERNO -Demostración: hecho notorio, el daño causado por motivo de las conductas cometidas con ocasión del conflicto, sí debe ser probado / LEY DE JUSTICIA Y PAZ - Reparación integral: indemnización de perjuicios, perjuicios morales, en los delitos de destrucción y apropiación debienes protegidos y actos de terrorismo no se presumen / LEY DE JUSTICIA Y PAZ - Reparación integral: incidente de reparación, sucesión procesal / LEY DE JUSTICIA Y PAZ - Reparación integral: incidente de reparación, transmisión del derecho por causa de muerte, solo compete determinar la procedencia de la indemnización, no definir quiénes ostentan la calidad de herederos / LEY DE JUSTICIA Y PAZ - Reparación integral: incidente de reparación, transmisión del derecho por causa de muerte, la condena en perjuicios, no se hace a favor de persona alguna, sino de la sucesión / LEY DE JUSTICIA Y PAZ - Víctimas indirectas: no pueden reportarse los hijos de crianza / LEY DE JUSTICIA Y PAZ - Víctimas: no se reconoce como víctima a los padres de crianza / LEY DE JUSTICIA Y PAZ - Víctimas: acreditación, unión marital de hecho, no es posible el reconocimiento de dos o más uniones maritales de hecho simultáneas. / PRUEBA - Hecho notorio: concepto / PRUEBA - Hecho notorio: conflicto armado interno / CONFLICTO ARMADO	INTERNO - Demostración: hecho notorio / LEY DE JUSTICIA Y PAZ - Reparación integral: indemnización de perjuicios, perjuicios morales, familiares del occiso, sus perjuicios no son un hecho notorio. / LEY DE JUSTICIA Y PAZ - Reparación integral: indemnización de perjuicios, demostración, al menos prueba sumaria / LEY DE JUSTICIA Y PAZ - Reparación integral: indemnización de perjuicios, demostración, principio de flexibilización de las reglas de apreciación probatoria, no equivale a la ausencia de prueba / LEY DE JUSTICIA Y PAZ - Reparación integral: presunción de legalidad del daño moral / LEY DE JUSTICIA Y PAZ - Reparación integral: tasación del daño moral en casos de desplazamiento forzado  /  DESPLAZAMIENTO  FORZADO  -Indemnización de perjuicios / PERJUICIOS - Los daños materiales deben ser probados. / CONFLICTO ARMADO INTERNO-Demostración: hecho notorio, el daño causado por motivo de las conductas cometidas con ocasión del conflicto, sí debe ser probado / DESTRUCCIÓN Y APROPIACIÓN DE BIENES PROTEGIDOS - Elementos: relación con la ventaja militar concreta prevista, explicación / DESTRUCCIÓN Y APROPIACIÓN DE BIENES PROTEGIDOS - Bienes protegidos: concepto / PERSONAS Y BIENES PROTEGIDOS POR EL DERECHO INTERNACIONAL HUMANITARIO -Daños incidentales / PERJUICIOS - Daño: siempre debe demostrarse, salvo en los casos en que la ley establece la presunción de su existencia. / ACTOS DE TERRORISMO - Concepto / ACTOS DE TERRORISMO - Finalidad: sembrar el miedo, el terror y la zozobra entre la población civil / ACTOS DE TERRORISMO - Daños morales: deben ser demostrados / PERJUICIOS - Daños morales: daño moral subjetivado, principio de arbitrio judicium / LEY DE JUSTICIA Y PAZ - Reparación integral: indemnización de perjuicios, perjuicios morales, en los delitos de destrucción y apropiación de bienes protegidos y actos de terrorismo no se presumen / INDEMNIZACIÓN  DE  PERJUICIOS  -  Lucro cesante: menor de edad, regulación	/INDEMNIZACIÓN  DE  PERJUICIOS  -  Lucro cesante: menor de edad, hasta los 18 años, salvo que se demuestre su dependencia económica hasta los 25 años / LEY DE JUSTICIA Y PAZ - Reparación integral: incidente de reparación, sucesión procesal / LEY DE JUSTICIA Y PAZ - Reparación integral: incidente de reparación, transmisión del derecho por causa de muerte / LEY DE JUSTICIA Y PAZ - Reparación integral: incidente de reparación, transmisión del derecho por causa de muerte, requisitos / LEY DE JUSTICIA Y PAZ - Reparación integral: incidente de reparación, transmisión del derecho por causa de muerte, solo compete determinar la procedencia de la indemnización, no definir quiénes ostentan la calidad de herederos / LEY DE JUSTICIA Y PAZ - Reparación integral: incidente de reparación, transmisión del derecho por causa de muerte, la condena en perjuicios, no se hace a favor de persona alguna, sino de la sucesión / FAMILIA - De crianza: requisitos para su existencia / FAMILIA - Hijos de crianza: elementos / LEY DE JUSTICIA Y PAZ - Víctimas: hijos de crianza, acreditación / LEY DE JUSTICIA Y PAZ - Víctimas indirectas: no pueden reportarse los hijos de crianza / LEY DE JUSTICIA Y PAZ - Víctimas: no se reconoce como víctima a los padres de crianza / LEY	DE JUSTICIA	Y	PAZ	-	Víctimas: acreditación, unión marital de hecho / LEY DE JUSTICIA Y PAZ - Víctimas: acreditación, unión marital de hecho, no es posible el reconocimiento de dos o más uniones maritales de hecho simultáneas / 
    SP2995-2024(58767) de 13/11/2024
    https://cortesuprema.gov.co/corte/wp-content/uploads/relatorias/pe/b1ene2025/SP2995-2024(58767).pdf"""
]

# Procesar textos
datos_extraidos = extraer_datos(textos)

# Guardar en un archivo JSON
with open("providencias.json", "w", encoding="utf-8") as f:
    json.dump(datos_extraidos, f, ensure_ascii=False, indent=4)

if datos_extraidos:  # Verifica que la lista no esté vacía
    primer_elemento = datos_extraidos[0]  # Obtiene el primer elemento
    rubros = primer_elemento["rubros"]  # Extrae los rubros
    print("Rubros del primer elemento:")
    for rubro in rubros:
        print(f"- {rubro}")
        
print("Archivo JSON generado: providencias.json")
