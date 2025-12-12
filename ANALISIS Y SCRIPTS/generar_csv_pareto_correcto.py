"""
Crear CSV correcto de Pareto con códigos CVEGEO de INEGI
Basado en la tabla oficial del documento LaTeX
"""

# Top 20 municipios del análisis oficial (líneas 52-71 del LaTeX)
top_20_oficial = [
    # Rank, Nombre LaTeX, Superficie ha, Org, % Acum, Grupo
    (1, 'Tizimín', 260595, 'UGROY', 35.2, 'Pareto'),
    (2, 'Panaba', 100026, 'UGROY', 48.1, 'Pareto'),  # Sin acento en LaTeX
    (3, 'Tekax', 78245, 'UGRY', 54.3, 'Pareto'),
    (4, 'Buctzotz', 74793, 'UGROY', 59.6, 'Pareto'),
    (5, 'Dzilam González', 55102, 'UGROY', 63.5, 'Pareto'),
    (6, 'Tzucacab', 50688, 'UGRY', 67.0, 'Pareto'),
    (7, 'Cenotillo', 43279, 'UGROY', 70.0, 'Pareto'),
    (8, 'Peto', 41168, 'UGRY', 72.8, 'Pareto'),
    (9, 'Sucila', 39712, 'UGROY', 75.6, 'Pareto'),  # Sin acento en LaTeX
    (10, 'Izamal', 33903, 'UGRY', 78.0, 'Pareto'),
    (11, 'San Felipe', 33203, 'UGROY', 80.3, 'Pareto'),
    (12, 'Temozon', 27754, 'UGROY', 82.3, 'Nivel2'),  # Sin acento en LaTeX
    (13, 'Tunkas', 27262, 'UGRY', 84.2, 'Nivel2'),  # Sin acento en LaTeX
    (14, 'Yaxcaba', 25045, 'UGRY', 85.9, 'Nivel2'),  # Sin acento en LaTeX
    (15, 'Kinchil', 25378, 'UGRY', 87.6, 'Nivel2'),
    (16, 'Valladolid', 23992, 'UGROY', 89.2, 'Nivel2'),
    (17, 'Maxcanú', 23180, 'UGRY', 90.7, 'Nivel2'),
    (18, 'Sotuta', 21142, 'UGRY', 92.1, 'Nivel2'),
    (19, 'Calotmul', 20638, 'UGROY', 93.5, 'Nivel2'),
    (20, 'Espita', 19442, 'UGROY', 94.8, 'Nivel2'),
]

# Mapeo de nombres LaTeX a códigos CVEGEO de INEGI
# Formato: 31 + código municipal de 3 dígitos
cvegeo_mapping = {
    'Tizimín': '31096',        # Tizimín
    'Panaba': '31057',         # Panabá
    'Tekax': '31079',          # Tekax de Álvaro Obregón
    'Buctzotz': '31006',       # Buctzotz
    'Dzilam González': '31029', # Dzilam González
    'Tzucacab': '31098',       # Tzucacab
    'Cenotillo': '31012',      # Cenotillo
    'Peto': '31058',           # Peto
    'Sucila': '31070',         # Sucilá
    'Izamal': '31040',         # Izamal
    'San Felipe': '31065',     # San Felipe
    'Temozon': '31085',        # Temozón
    'Tunkas': '31097',         # Tunkás
    'Yaxcaba': '31104',        # Yaxcabá
    'Kinchil': '31044',        # Kinchil
    'Valladolid': '31102',     # Valladolid
    'Maxcanú': '31048',        # Maxcanú
    'Sotuta': '31069',         # Sotuta
    'Calotmul': '31008',       # Calotmul
    'Espita': '31032',         # Espita
}

# Nombres oficiales COMPLETOS de INEGI (con acentos correctos)
nombre_inegi = {
    '31096': 'Tizimín',
    '31057': 'Panabá',
    '31079': 'Tekax de Álvaro Obregón',
    '31006': 'Buctzotz',
    '31029': 'Dzilam González',
    '31098': 'Tzucacab',
    '31012': 'Cenotillo',
    '31058': 'Peto',
    '31070': 'Sucilá',
    '31040': 'Izamal',
    '31065': 'San Felipe',
    '31085': 'Temozón',
    '31097': 'Tunkás',
    '31104': 'Yaxcabá',
    '31044': 'Kinchil',
    '31102': 'Valladolid',
    '31048': 'Maxcanú',
    '31069': 'Sotuta',
    '31008': 'Calotmul',
    '31032': 'Espita',
}

# Generar CSV
output_path = r'H:\My Drive\2025. 1.0 JEFATURA PROGRAMA\mapas_qgis\pareto_ganadero_yucatan_FINAL.csv'

with open(output_path, 'w', encoding='utf-8') as f:
    # Header
    f.write('CVEGEO,municipio,superficie_ha,organizacion,pareto_grupo,porcentaje_acumulado\n')
    
    # Datos
    for rank, nombre_latex, superficie, org, pct_acum, grupo in top_20_oficial:
        cvegeo = cvegeo_mapping[nombre_latex]
        nombre_oficial = nombre_inegi[cvegeo]
        
        f.write(f'{cvegeo},{nombre_oficial},{superficie},{org},{grupo},{pct_acum}\n')

print("=" * 80)
print("CSV GENERADO CORRECTAMENTE")
print("=" * 80)
print(f"\nArchivo: {output_path}")
print("\nContenido:")
print("-" * 80)

with open(output_path, 'r', encoding='utf-8') as f:
    print(f.read())

print("\n" + "=" * 80)
print("VERIFICACIÓN: Municipios que APARECEN en mapa pero NO deberían")
print("=" * 80)

municipios_incorrectos = {
    '31050': 'Mérida',
    '31059': 'Progreso',
    '31038': 'Hunucmá',
    '31101': 'Umán',
    '31052': 'Motul',
    '31041': 'Kanasín',
    '31056': 'Oxkutzcab',
    '31089': 'Ticul'
}

print("\nEstos municipios NO deben aparecer como Pareto ni Nivel2:")
for cvegeo, nombre in municipios_incorrectos.items():
    print(f"  {cvegeo} - {nombre}")

print("\n" + "=" * 80)
