#!/usr/bin/env python3
"""
Análisis de documentos PDF sobre sistemas silvopastoriles
Extrae datos cuantitativos específicos para el macroproyecto Yucatán
"""

import PyPDF2
import re
import os

# Ruta base
BASE_PATH = "/Users/smunozam/Library/CloudStorage/GoogleDrive-smunoz.sader@gmail.com/My Drive/2025. 1.0 JEFATURA PROGRAMA/DOCS REFERENCIA"

# Lista de PDFs a analizar
PDF_FILES = [
    "Sistemas silvopastoriles enriquecidos na propuesta para integrar la conservación en la producción ganadera en comunidades rurales de Los Tuxtlas, México.pdf",
    "RITER INFOGRAFIA.pdf",
    "Modelo_de_innovacion_en_ganaderia_sostenible TNC-UADY-RITER_compressed.pdf",
    "guia metodologica para la incorporacion de escuelas de campo de sistemas silvopastoriles (colombia).pdf",
    "MASIFICAR SISTEMAS SILVOPASTORILES, LARGO Y SINUOSO CAMINO.PDF",
    "especies nativas con potencial forrajero.pdf",
    "escuelas de campo silvopastoriles JALISCO.pdf"
]

def extract_text_from_pdf(pdf_path, max_pages=None):
    """Extrae texto de un PDF"""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)
            pages_to_read = min(total_pages, max_pages) if max_pages else total_pages
            
            text = ""
            for page_num in range(pages_to_read):
                page = reader.pages[page_num]
                text += page.extract_text() + "\n"
            
            return text, total_pages
    except Exception as e:
        return f"ERROR: {str(e)}", 0

def buscar_datos_escuelas_campo(texto, filename):
    """Busca información específica sobre escuelas de campo"""
    resultados = []
    
    # Patrones de búsqueda
    patrones = {
        'sesiones': r'(\d+)\s*(sesiones|talleres|encuentros)',
        'participantes': r'(\d+)[-\s]*(\d+)?\s*(productores|participantes|ganaderos)',
        'duracion': r'(\d+)\s*(años|meses|año)',
        'costo': r'(\$|USD|MXN|pesos)\s*(\d+[,\d]*)',
        'adopcion': r'(\d+)%\s*(adopción|adoptaron|implementaron)',
        'hectareas': r'(\d+[,\d]*)\s*(ha|hectáreas)',
    }
    
    for categoria, patron in patrones.items():
        matches = re.finditer(patron, texto, re.IGNORECASE)
        for match in matches:
            contexto = texto[max(0, match.start()-100):min(len(texto), match.end()+100)]
            resultados.append({
                'archivo': filename,
                'categoria': categoria,
                'match': match.group(0),
                'contexto': contexto.replace('\n', ' ').strip()
            })
    
    return resultados

def buscar_especies_nativas(texto, filename):
    """Busca menciones de especies nativas"""
    resultados = []
    
    # Especies comunes en península Yucatán
    especies = [
        'Leucaena', 'Guazuma', 'Ramón', 'Brosimum', 'Piscidia', 
        'Lysiloma', 'Acacia', 'Gliricidia', 'Moringa', 'Inga',
        'Havardia', 'Sabal', 'Coccoloba', 'Erythrina'
    ]
    
    for especie in especies:
        pattern = rf'\b{especie}\b[^.]*(?:\.)'
        matches = re.finditer(pattern, texto, re.IGNORECASE)
        for match in matches:
            resultados.append({
                'archivo': filename,
                'especie': especie,
                'contexto': match.group(0).strip()
            })
    
    return resultados

def analizar_costos_inversiones(texto, filename):
    """Busca datos de costos e inversiones"""
    resultados = []
    
    # Patrones de costos
    patrones_costo = [
        r'inversión[^.]*(\$|USD|MXN)\s*(\d+[,\d]*)[^.]*(?:ha|hectárea)',
        r'costo[^.]*(\$|USD|MXN)\s*(\d+[,\d]*)',
        r'subsidio[^.]*(\d+)%',
        r'(\d+)\s*jornales[^.]*ha',
    ]
    
    for patron in patrones_costo:
        matches = re.finditer(patron, texto, re.IGNORECASE)
        for match in matches:
            contexto = texto[max(0, match.start()-150):min(len(texto), match.end()+150)]
            resultados.append({
                'archivo': filename,
                'tipo': 'costo_inversion',
                'match': match.group(0),
                'contexto': contexto.replace('\n', ' ').strip()
            })
    
    return resultados

def buscar_datos_riter(texto, filename):
    """Busca datos específicos del proyecto RITER"""
    resultados = []
    
    keywords_riter = [
        'RITER', 'TNC', 'UADY', 'Yucatán', 'carga animal', 
        'ganancia de peso', 'carbono', 'UPP', 'productor'
    ]
    
    for keyword in keywords_riter:
        pattern = rf'[^.]*{keyword}[^.]*(?:\.)'
        matches = list(re.finditer(pattern, texto, re.IGNORECASE))
        for match in matches[:5]:  # Limitar a 5 matches por keyword
            resultados.append({
                'archivo': filename,
                'keyword': keyword,
                'contexto': match.group(0).strip()
            })
    
    return resultados

# MAIN ANALYSIS
print("=" * 80)
print("ANÁLISIS DE DOCUMENTOS SISTEMAS SILVOPASTORILES")
print("Macroproyecto Renacimiento Ganadero Maya - Yucatán 2026-2030")
print("=" * 80)
print()

all_results = {
    'escuelas_campo': [],
    'especies_nativas': [],
    'costos': [],
    'riter': []
}

for pdf_file in PDF_FILES:
    pdf_path = os.path.join(BASE_PATH, pdf_file)
    
    if not os.path.exists(pdf_path):
        print(f"❌ NO ENCONTRADO: {pdf_file}")
        continue
    
    print(f"\n{'='*80}")
    print(f"📄 PROCESANDO: {pdf_file}")
    print(f"{'='*80}")
    
    # Extraer texto (limitado a primeras 50 páginas para eficiencia)
    texto, total_pages = extract_text_from_pdf(pdf_path, max_pages=50)
    
    if texto.startswith("ERROR"):
        print(f"❌ Error al procesar: {texto}")
        continue
    
    print(f"✅ Páginas totales: {total_pages} | Páginas procesadas: {min(50, total_pages)}")
    print(f"   Caracteres extraídos: {len(texto):,}")
    
    # Análisis específico por documento
    if 'escuelas de campo' in pdf_file.lower() or 'colombia' in pdf_file.lower() or 'jalisco' in pdf_file.lower():
        resultados_ec = buscar_datos_escuelas_campo(texto, pdf_file)
        all_results['escuelas_campo'].extend(resultados_ec)
        print(f"   → Datos escuelas de campo: {len(resultados_ec)} matches")
    
    if 'especies nativas' in pdf_file.lower():
        resultados_esp = buscar_especies_nativas(texto, pdf_file)
        all_results['especies_nativas'].extend(resultados_esp)
        print(f"   → Especies nativas: {len(resultados_esp)} matches")
    
    if 'RITER' in pdf_file or 'Modelo' in pdf_file:
        resultados_riter = buscar_datos_riter(texto, pdf_file)
        all_results['riter'].extend(resultados_riter)
        print(f"   → Datos RITER: {len(resultados_riter)} matches")
    
    # Buscar costos en todos los documentos
    resultados_costos = analizar_costos_inversiones(texto, pdf_file)
    all_results['costos'].extend(resultados_costos)
    print(f"   → Datos costos/inversión: {len(resultados_costos)} matches")

# REPORTE CONSOLIDADO
print("\n\n" + "="*80)
print("REPORTE CONSOLIDADO DE HALLAZGOS")
print("="*80)

print("\n\n📊 A) ESCUELAS DE CAMPO - METODOLOGÍA")
print("-" * 80)
ec_por_archivo = {}
for item in all_results['escuelas_campo']:
    archivo = item['archivo']
    if archivo not in ec_por_archivo:
        ec_por_archivo[archivo] = []
    ec_por_archivo[archivo].append(item)

for archivo, items in ec_por_archivo.items():
    print(f"\n📄 {archivo}:")
    categorias = {}
    for item in items:
        cat = item['categoria']
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append(f"  • {item['match']} - [{item['contexto'][:200]}...]")
    
    for cat, matches in categorias.items():
        print(f"\n  {cat.upper()}:")
        for match in matches[:3]:  # Top 3 por categoría
            print(match)

print("\n\n🌳 D) ESPECIES NATIVAS FORRAJERAS")
print("-" * 80)
especies_count = {}
for item in all_results['especies_nativas']:
    esp = item['especie']
    especies_count[esp] = especies_count.get(esp, 0) + 1

print("\nEspecies mencionadas (frecuencia):")
for especie, count in sorted(especies_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  • {especie}: {count} menciones")

# Mostrar contextos relevantes
print("\nContextos relevantes:")
for item in all_results['especies_nativas'][:15]:
    print(f"\n  [{item['especie']}] {item['contexto'][:250]}...")

print("\n\n💰 E) COSTOS Y TIEMPOS REALISTAS")
print("-" * 80)
for item in all_results['costos'][:20]:
    print(f"\n📄 {item['archivo']}:")
    print(f"  Match: {item['match']}")
    print(f"  Contexto: {item['contexto'][:300]}...")

print("\n\n🏢 C) EXPERIENCIA RITER-UADY-TNC YUCATÁN")
print("-" * 80)
riter_por_keyword = {}
for item in all_results['riter']:
    kw = item['keyword']
    if kw not in riter_por_keyword:
        riter_por_keyword[kw] = []
    riter_por_keyword[kw].append(item['contexto'])

for keyword, contextos in riter_por_keyword.items():
    print(f"\n{keyword}:")
    for ctx in contextos[:3]:
        print(f"  • {ctx[:250]}...")

print("\n\n" + "="*80)
print("ANÁLISIS COMPLETADO")
print(f"Total hallazgos: {sum(len(v) for v in all_results.values())}")
print("="*80)
