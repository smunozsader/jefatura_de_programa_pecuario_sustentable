# Metadatos - Análisis de Pareto Ganadería Yucatán
## Macroproyecto Renacimiento Ganadero Maya 2026-2030

### Información General
- **Autor**: MVZ Sergio Muñoz de Alba Medrano, Consultor Independiente
- **Comisionado por**: SEDER - Gobierno del Estado de Yucatán  
- **Fecha**: Diciembre 2025
- **Fuente de datos**: Padrón Ganadero Nacional 2025 (SINIIGA-SENASICA)

### Estadísticas del Análisis de Pareto
- **Municipios Pareto (Nivel 1)**: 11 (10.4% del total estatal)
- **Concentración superficie ganadera**: 79.1%
- **Concentración UPP**: 76.0%
- **Concentración vientres**: 87.9%
- **Municipio líder**: Tizimín (35.2% concentración individual)

### Archivos Generados
1. `pareto_ganadero_yucatan.csv` - Datos principales del análisis
2. `indicadores_territoriales_pareto.csv` - Indicadores suplementarios
3. `centros_estrategicos_macroproyecto.csv` - Ubicaciones estratégicas
4. `estilo_pareto_ganadero.qml` - Estilo QGIS oficial

### Uso en QGIS
1. Cargar shapefile municipal de INEGI (31mun.shp)
2. Unir por campo 'CVEGEO' con 'cve_muni' del CSV
3. Aplicar estilo QML generado
4. Agregar capas de puntos para centros estratégicos

### Colores Oficiales SADER
- Nivel 1 Pareto: RGB(0,102,51) - Verde SADER
- Nivel 2 Complementario: RGB(204,153,0) - Dorado SADER  
- Otros municipios: RGB(200,200,200) - Gris neutro

### Notas Técnicas
- Principio de Pareto validado: 10.4% municipios = 80.3% actividad
- Regionalización oficial: UGROY (7 mun. Pareto) + UGRY (4 mun. Pareto)
- Sistema de referencia: EPSG:4326 (WGS84)
