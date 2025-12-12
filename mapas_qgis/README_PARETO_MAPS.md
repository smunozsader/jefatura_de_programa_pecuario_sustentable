# 🗺️ QGIS Maps - Análisis Pareto Ganadero Yucatán

## 📊 Análisis de Concentración Ganadera por Superficie (Hectáreas)

**Fuente de datos**: Padrón Ganadero Nacional 2025 - Análisis oficial SEDER Yucatán  
**Métrica principal**: **Superficie ganadera en hectáreas** (no número de cabezas)  
**Umbral Pareto**: 11 municipios concentran **80.3%** de la superficie ganadera estatal

---

## 📁 Archivos Incluidos

### 1. Datos Base
- **`pareto_ganadero_yucatan_FINAL.csv`**: Top 20 municipios con datos validados
  - Campos: CVEGEO, municipio, superficie_ha, organizacion, pareto_grupo, porcentaje_acumulado

### 2. Estilos QGIS (.qml)
- **`estilo_analisis_pareto.qml`**: Estilo categórico (Pareto vs Nivel2 vs Resto)
- **`estilo_graduado_ganado.qml`**: Graduado por intensidad de superficie (6 clases)
- **`estilo_organizaciones.qml`**: Por organización ganadera (UGROY/UGRY)

### 3. Documentación
- **`README_PARETO_MAPS.md`**: Este archivo
- **`guia_completa_qgis.md`**: Tutorial detallado de uso

---

## 🎯 Top 11 Municipios Pareto (80.3% Concentración)

| Rank | Municipio | Superficie (ha) | Organización | % Acumulado | Grupo |
|------|-----------|-----------------|--------------|-------------|-------|
| 1 | **Tizimín** | 260,595 | UGROY | 35.2% | Pareto |
| 2 | **Panabá** | 100,026 | UGROY | 48.1% | Pareto |
| 3 | **Tekax de Álvaro Obregón** | 78,245 | UGRY | 54.3% | Pareto |
| 4 | **Buctzotz** | 74,793 | UGROY | 59.6% | Pareto |
| 5 | **Dzilam González** | 55,102 | UGROY | 63.5% | Pareto |
| 6 | **Tzucacab** | 50,688 | UGRY | 67.0% | Pareto |
| 7 | **Cenotillo** | 43,279 | UGROY | 70.0% | Pareto |
| 8 | **Peto** | 41,168 | UGRY | 72.8% | Pareto |
| 9 | **Sucilá** | 39,712 | UGROY | 75.6% | Pareto |
| 10 | **Izamal** | 33,903 | UGRY | 78.0% | Pareto |
| 11 | **San Felipe** | 33,203 | UGROY | **80.3%** | Pareto |

**🔴 Interpretación**: Estos 11 municipios representan el **10.4% del territorio** estatal pero concentran **80.3%** de la superficie ganadera, validando el principio de Pareto (80/20).

---

## 📈 Municipios Nivel 2 (hasta 94.8% acumulado)

| Rank | Municipio | Superficie (ha) | Organización | % Acumulado | Grupo |
|------|-----------|-----------------|--------------|-------------|-------|
| 12 | Temozón | 27,754 | UGROY | 82.3% | Nivel2 |
| 13 | Tunkás | 27,262 | UGRY | 84.2% | Nivel2 |
| 14 | Yaxcabá | 25,045 | UGRY | 85.9% | Nivel2 |
| 15 | Kinchil | 25,378 | UGRY | 87.6% | Nivel2 |
| 16 | Valladolid | 23,992 | UGROY | 89.2% | Nivel2 |
| 17 | Maxcanú | 23,180 | UGRY | 90.7% | Nivel2 |
| 18 | Sotuta | 21,142 | UGRY | 92.1% | Nivel2 |
| 19 | Calotmul | 20,638 | UGROY | 93.5% | Nivel2 |
| 20 | Espita | 19,442 | UGROY | 94.8% | Nivel2 |

---

## 🛠️ Cómo Usar en QGIS

### Paso 1: Cargar Capa Base (Marco Geoestadístico INEGI)
```
1. Abrir QGIS 3.16+
2. Capa → Añadir Capa → Añadir Capa Vectorial
3. Seleccionar: ../marco_geoestadistico_inegi/31mun.shp
```

### Paso 2: Unir Datos Pareto
```
1. Click derecho en capa "31mun" → Propiedades → Uniones
2. Añadir nueva unión:
   - Capa de unión: pareto_ganadero_yucatan_FINAL.csv
   - Campo de unión: CVEGEO
   - Campo objetivo: CVEGEO
3. Aceptar
```

### Paso 3: Aplicar Estilo

#### Opción A: Estilo Categórico (Pareto vs Resto)
```
1. Click derecho en capa → Propiedades → Simbología
2. Cargar Estilo → estilo_analisis_pareto.qml
3. Resultado: 11 municipios en ROJO intenso, 9 municipios Nivel2 en NARANJA, resto en gris claro
```

#### Opción B: Estilo Graduado (Intensidad)
```
1. Click derecho en capa → Propiedades → Simbología
2. Cargar Estilo → estilo_graduado_ganado.qml
3. Resultado: Gradiente rojo (260K ha Tizimín) → rosa claro (resto)
```

---

## 🎨 Paleta de Colores

### Estilo Categórico
- **Grupo Pareto (80.3%)**: 🔴 Rojo intenso #B22222
- **Grupo Nivel2 (hasta 94.8%)**: 🟠 Naranja #FF8C00
- **Resto (5.2%)**: ⚪ Gris claro #E0E0E0

### Estilo Graduado (por superficie)
1. **Muy Alto** (100,000+ ha): 🔴 #B22222 - Tizimín, Panabá
2. **Alto** (50,000-99,999 ha): 🔴 #CD5C5C - Tekax, Buctzotz, Dzilam González, Tzucacab
3. **Medio-Alto** (30,000-49,999 ha): 🔴 #DC143C - Cenotillo, Peto, Sucilá, Izamal, San Felipe
4. **Medio** (20,000-29,999 ha): 🟥 #F08080 - Temozón, Tunkás, Yaxcabá, Kinchil, Valladolid, Maxcanú, Sotuta, Calotmul
5. **Bajo** (10,000-19,999 ha): 🌸 #FFA0A0 - Espita
6. **Muy Bajo** (1-9,999 ha): 🌸 #FFE4E1 - Resto

---

## 📐 Exportar para LaTeX

### Configuración Recomendada
```
Proyecto → Importar/Exportar → Exportar Mapa a Imagen
- Formato: PNG
- Resolución: 300 DPI
- Ancho: 15-20 cm (para documento A4)
- Escala: 1:1,500,000 (mapa estatal completo)
- Fondo transparente: SÍ
```

### Integración en LaTeX
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.85\textwidth]{mapa_pareto_ganadero_yucatan.png}
\caption{Análisis de Pareto: Concentración Ganadera en Yucatán por Superficie (2025). 
Los 11 municipios en rojo (Pareto) concentran el 80.3\% de la superficie ganadera estatal, 
validando la focalización territorial del Macroproyecto Renacimiento Ganadero Maya.}
\label{fig:pareto_ganadero}
\end{figure}
```

---

## ⚠️ NOTAS IMPORTANTES

### ❌ Municipios NO incluidos en Top 20
**Mérida, Progreso, Hunucmá, Umán, Motul, Kanasín, Oxkutzcab** NO aparecen en el análisis oficial de Pareto porque:
- El análisis se basa en **superficie ganadera en hectáreas**, no en número de cabezas
- Estos municipios tienen alta densidad poblacional humana, reduciendo superficie disponible para ganadería
- La fuente oficial es el **Padrón Ganadero Nacional 2025** (SEDER Yucatán), no SIAP

### ✅ Validación de Datos
- **Fuente primaria**: Analisis Pareto Ganadero Yucatan.tex (documento LaTeX oficial)
- **Líneas de referencia**: 95-129 (tabla de concentración acumulada)
- **Verificación**: Top 11 = 80.3% acumulado exacto

### 📊 Distribución por Organización
- **UGROY (Unión Ganadera Regional de Oriente de Yucatán)**: 7 municipios Pareto (63.6% del grupo)
- **UGRY (Unión Ganadera Regional del Centro)**: 4 municipios Pareto (36.4% del grupo)
- **Implicación estratégica**: UGROY lidera concentración territorial, justificando enfoque en municipios orientales

---

## 🔄 Actualización de Datos

Si necesitas actualizar con nuevos datos del Padrón Ganadero:

1. **Editar CSV**:
   ```
   nano pareto_ganadero_yucatan_FINAL.csv
   ```

2. **Mantener estructura**:
   ```csv
   CVEGEO,municipio,superficie_ha,organizacion,pareto_grupo,porcentaje_acumulado
   31096,Tizimín,260595,UGROY,Pareto,35.2
   ```

3. **Recalcular estilos** si cambian rangos de superficie

4. **Validar** contra documento LaTeX oficial

---

## 📞 Soporte Técnico

**Contacto**: MVZ Sergio Muñoz de Alba Medrano  
**Proyecto**: Macroproyecto Renacimiento Ganadero Maya  
**Institución**: SEDER Yucatán  
**Versión**: 2025.01 (datos validados enero 2025)

---

**Última actualización**: 2025-01-XX (corrección de datos - uso de superficie en hectáreas en lugar de número de cabezas)
