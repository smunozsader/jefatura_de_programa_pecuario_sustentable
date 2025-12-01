#!/usr/bin/env python3
"""
Extracción DETALLADA de datos cuantitativos específicos
para Macroproyecto Yucatán SSPi
"""

import PyPDF2
import re
import os

BASE_PATH = "/Users/smunozam/Library/CloudStorage/GoogleDrive-smunoz.sader@gmail.com/My Drive/2025. 1.0 JEFATURA PROGRAMA/DOCS REFERENCIA"

def extract_full_text(pdf_path):
    """Extrae TODO el texto de un PDF"""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
            return text
    except Exception as e:
        return f"ERROR: {str(e)}"

def analizar_colombia_eca():
    """Análisis detallado guía Colombia"""
    print("\n" + "="*80)
    print("📚 GUÍA METODOLÓGICA COLOMBIA - ANÁLISIS DETALLADO")
    print("="*80)
    
    pdf_path = os.path.join(BASE_PATH, "guia metodologica para la incorporacion de escuelas de campo de sistemas silvopastoriles (colombia).pdf")
    text = extract_full_text(pdf_path)
    
    if text.startswith("ERROR"):
        print(f"Error: {text}")
        return
    
    print(f"\nTexto completo extraído: {len(text):,} caracteres")
    
    # Búsquedas específicas
    print("\n--- ESTRUCTURA OPERATIVA ---")
    
    # Sesiones
    sesiones = re.findall(r'(\d+)\s*sesiones', text, re.IGNORECASE)
    if sesiones:
        print(f"Sesiones mencionadas: {set(sesiones)}")
    
    # Participantes
    part = re.findall(r'(\d+)\s*(?:productores|participantes|ganaderos)', text, re.IGNORECASE)
    if part:
        print(f"Número participantes mencionados: {set(part)}")
    
    # Duración
    dur = re.findall(r'duración[^.]*?(\d+)\s*(meses|años)', text, re.IGNORECASE)
    if dur:
        print(f"Duración: {dur}")
    
    # Buscar secciones sobre costos
    print("\n--- COSTOS Y PRESUPUESTO ---")
    costos_section = re.findall(r'(?:costo|presupuesto|inversión)[^.]{0,200}', text, re.IGNORECASE)
    for i, costo in enumerate(costos_section[:10], 1):
        print(f"{i}. {costo.strip()}")
    
    # Buscar metodología
    print("\n--- METODOLOGÍA ---")
    metod = re.findall(r'metodología[^.]{0,250}', text, re.IGNORECASE)
    for i, m in enumerate(metod[:5], 1):
        print(f"{i}. {m.strip()}")
    
    # Resultados/indicadores
    print("\n--- RESULTADOS/INDICADORES ---")
    result = re.findall(r'(?:resultado|indicador|adopción|impacto)[^.]{0,200}', text, re.IGNORECASE)
    for i, r in enumerate(result[:10], 1):
        print(f"{i}. {r.strip()}")

def analizar_masificar():
    """Análisis documento MASIFICAR (barreras adopción)"""
    print("\n" + "="*80)
    print("🚧 MASIFICAR SISTEMAS SILVOPASTORILES - BARRERAS Y FACTORES CRÍTICOS")
    print("="*80)
    
    pdf_path = os.path.join(BASE_PATH, "MASIFICAR SISTEMAS SILVOPASTORILES, LARGO Y SINUOSO CAMINO.PDF")
    text = extract_full_text(pdf_path)
    
    if text.startswith("ERROR"):
        print(f"Error: {text}")
        return
    
    print(f"\nTexto completo extraído: {len(text):,} caracteres")
    
    # Barreras
    print("\n--- BARRERAS IDENTIFICADAS ---")
    barreras = re.findall(r'(?:barrera|obstáculo|limitante|problema|dificultad)[^.]{0,250}\.', text, re.IGNORECASE)
    for i, b in enumerate(barreras[:15], 1):
        print(f"{i}. {b.strip()}")
    
    # Tiempo
    print("\n--- TIEMPOS Y PLAZOS ---")
    tiempos = re.findall(r'(?:\d+)\s*(?:años|meses|año)[^.]{0,150}', text, re.IGNORECASE)
    for i, t in enumerate(tiempos[:10], 1):
        print(f"{i}. {t.strip()}")
    
    # Subsidios
    print("\n--- SUBSIDIOS Y APOYO ---")
    subsidios = re.findall(r'(?:subsidio|apoyo|financiamiento|incentivo)[^.]{0,200}', text, re.IGNORECASE)
    for i, s in enumerate(subsidios[:10], 1):
        print(f"{i}. {s.strip()}")
    
    # Recomendaciones
    print("\n--- RECOMENDACIONES ---")
    recom = re.findall(r'(?:recomendar|recomendación|debe|necesario)[^.]{0,200}', text, re.IGNORECASE)
    for i, r in enumerate(recom[:10], 1):
        print(f"{i}. {r.strip()}")

def analizar_riter_modelo():
    """Análisis Modelo TNC-UADY-RITER"""
    print("\n" + "="*80)
    print("🏢 MODELO TNC-UADY-RITER - DATOS CUANTITATIVOS")
    print("="*80)
    
    pdf_path = os.path.join(BASE_PATH, "Modelo_de_innovacion_en_ganaderia_sostenible TNC-UADY-RITER_compressed.pdf")
    text = extract_full_text(pdf_path)
    
    if text.startswith("ERROR"):
        print(f"Error: {text}")
        return
    
    print(f"\nTexto completo extraído: {len(text):,} caracteres")
    
    # Hectáreas
    print("\n--- HECTÁREAS Y SUPERFICIE ---")
    ha = re.findall(r'(\d+[,\d]*)\s*(?:ha|hectáreas)[^.]{0,150}', text, re.IGNORECASE)
    for i, h in enumerate(ha[:15], 1):
        print(f"{i}. {h.strip()}")
    
    # UPP/Productores
    print("\n--- UPP Y PRODUCTORES ---")
    upp = re.findall(r'(?:UPP|productores|ganaderos)[^.]{0,200}', text, re.IGNORECASE)
    for i, u in enumerate(upp[:15], 1):
        print(f"{i}. {u.strip()}")
    
    # Carga animal
    print("\n--- CARGA ANIMAL ---")
    carga = re.findall(r'carga\s*animal[^.]{0,250}', text, re.IGNORECASE)
    for i, c in enumerate(carga[:10], 1):
        print(f"{i}. {c.strip()}")
    
    # Ganancia peso
    print("\n--- GANANCIA DE PESO ---")
    ganancia = re.findall(r'ganancia[^.]{0,200}', text, re.IGNORECASE)
    for i, g in enumerate(ganancia[:10], 1):
        print(f"{i}. {g.strip()}")
    
    # Producción
    print("\n--- PRODUCCIÓN LECHE/CARNE ---")
    prod = re.findall(r'producción[^.]{0,200}(?:leche|carne|kg)', text, re.IGNORECASE)
    for i, p in enumerate(prod[:10], 1):
        print(f"{i}. {p.strip()}")
    
    # Carbono
    print("\n--- CAPTURA CARBONO ---")
    carbono = re.findall(r'carbono[^.]{0,200}', text, re.IGNORECASE)
    for i, c in enumerate(carbono[:10], 1):
        print(f"{i}. {c.strip()}")

def analizar_especies_nativas():
    """Análisis especies nativas (ahora con PyCryptodome)"""
    print("\n" + "="*80)
    print("🌳 ESPECIES NATIVAS CON POTENCIAL FORRAJERO")
    print("="*80)
    
    pdf_path = os.path.join(BASE_PATH, "especies nativas con potencial forrajero.pdf")
    text = extract_full_text(pdf_path)
    
    if text.startswith("ERROR"):
        print(f"Error: {text}")
        return
    
    print(f"\nTexto completo extraído: {len(text):,} caracteres")
    
    # Especies mencionadas
    print("\n--- ESPECIES IDENTIFICADAS ---")
    especies_keywords = [
        'Leucaena', 'Guazuma', 'Ramón', 'Brosimum', 'Piscidia',
        'Lysiloma', 'Acacia', 'Gliricidia', 'Inga', 'Havardia',
        'Sabal', 'Coccoloba', 'Erythrina', 'Caesalpinia'
    ]
    
    for especie in especies_keywords:
        matches = re.findall(rf'{especie}[^.]*\.', text, re.IGNORECASE)
        if matches:
            print(f"\n{especie.upper()}:")
            for m in matches[:3]:
                print(f"  • {m.strip()}")
    
    # Densidad/establecimiento
    print("\n--- DENSIDAD Y ESTABLECIMIENTO ---")
    densidad = re.findall(r'(?:densidad|plantas|árboles)[^.]{0,200}(?:/ha|por hectárea)', text, re.IGNORECASE)
    for i, d in enumerate(densidad[:10], 1):
        print(f"{i}. {d.strip()}")
    
    # Costos
    print("\n--- COSTOS ESTABLECIMIENTO ---")
    costos = re.findall(r'costo[^.]{0,200}', text, re.IGNORECASE)
    for i, c in enumerate(costos[:10], 1):
        print(f"{i}. {c.strip()}")

def analizar_jalisco_eca():
    """Análisis Jalisco ECA"""
    print("\n" + "="*80)
    print("📚 ESCUELAS DE CAMPO JALISCO")
    print("="*80)
    
    pdf_path = os.path.join(BASE_PATH, "escuelas de campo silvopastoriles JALISCO.pdf")
    text = extract_full_text(pdf_path)
    
    if text.startswith("ERROR"):
        print(f"Error: {text}")
        return
    
    print(f"\nTexto completo extraído: {len(text):,} caracteres")
    
    # Buscar estructura
    print("\n--- ESTRUCTURA Y METODOLOGÍA ---")
    metod = re.findall(r'(?:sesiones|talleres|módulos)[^.]{0,200}', text, re.IGNORECASE)
    for i, m in enumerate(metod[:10], 1):
        print(f"{i}. {m.strip()}")
    
    # Participantes
    print("\n--- PARTICIPANTES Y REQUISITOS ---")
    part = re.findall(r'(?:participantes|productores|requisitos)[^.]{0,200}', text, re.IGNORECASE)
    for i, p in enumerate(part[:10], 1):
        print(f"{i}. {p.strip()}")

# EJECUCIÓN PRINCIPAL
print("\n" + "="*80)
print("EXTRACCIÓN DETALLADA DATOS CUANTITATIVOS SSPi")
print("Macroproyecto Renacimiento Ganadero Maya - Yucatán 2026-2030")
print("="*80)

# Ejecutar análisis por documento
analizar_colombia_eca()
analizar_masificar()
analizar_riter_modelo()
analizar_especies_nativas()
analizar_jalisco_eca()

print("\n" + "="*80)
print("EXTRACCIÓN COMPLETADA")
print("="*80)
