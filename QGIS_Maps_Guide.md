# QGIS Maps Integration Guide for Macroproyecto

## 🗺️ **Maps Needed for the Document:**

### 1. **Mapa de Regionalización Ganadera Yucatán**
- **Data**: Municipal cattle inventory (SIAP 2023)
- **Visualization**: Choropleth map showing cattle density by municipality
- **Focus**: Highlight the 11 priority municipalities (80.3% concentration)
- **Output**: `mapa_regionalizacion_ganadera.png` (300 DPI, 15cm width)

### 2. **Mapa de Cobertura SSPi (Sistemas Silvopastoriles)**
- **Data**: Planned 6,000 hectares distribution
- **Visualization**: Point/polygon map showing UPP locations
- **Focus**: 120 UPP across priority regions
- **Output**: `mapa_cobertura_sspi.png` (300 DPI, 15cm width)

### 3. **Mapa de Distribución Meliponicultura**
- **Data**: 50 UPP across 7 regions, 38 municipalities
- **Visualization**: Graduated symbols by number of beneficiaries
- **Focus**: Gender distribution (350 women, 115 youth)
- **Output**: `mapa_meliponicultura.png` (300 DPI, 15cm width)

### 4. **Mapa Integrado del Macroproyecto**
- **Data**: All 6 components combined
- **Visualization**: Multi-layer comprehensive view
- **Focus**: Complete territorial coverage
- **Output**: `mapa_macroproyecto_integral.png` (300 DPI, 20cm width)

## 📋 **QGIS Data Preparation Steps:**

### A. **Data Sources**
1. **Municipal boundaries**: INEGI Marco Geoestadístico
2. **SIAP cattle data**: Link with municipal codes
3. **UPP locations**: GPS coordinates or approximate centroids
4. **Regional divisions**: Custom regions (Poniente, Noreste, etc.)

### B. **QGIS Project Setup**
```
Project Structure:
├── Data/
│   ├── municipios_yucatan.shp (INEGI boundaries)
│   ├── inventario_bovino_siap.csv (cattle data)
│   ├── upp_sspi_locations.csv (SSPi locations)
│   └── upp_meliponicultura.csv (beekeeping locations)
├── Styles/
│   ├── sader_colors.qml (official SADER styling)
│   └── symbol_library.xml (custom symbols)
└── Outputs/
    └── maps_300dpi/ (final PNG exports)
```

### C. **Styling Guidelines**
- **Colors**: Use SADER official palette
  - Green: RGB(34,139,34) for agricultural areas
  - Blue: RGB(0,51,102) for water/infrastructure
  - Gold: RGB(255,215,0) for priority areas
- **Fonts**: Arial or similar sans-serif, minimum 10pt
- **Legend**: Clear, bilingual (Spanish primary)
- **Scale bar**: Metric units (km)
- **North arrow**: Simple, unobtrusive

## 🔧 **QGIS Export Settings:**

### **For LaTeX Integration:**
```
Export Format: PNG
Resolution: 300 DPI
Width: 15-20 cm (for A4 layout)
Color Mode: RGB
Transparency: Background transparent
Compression: PNG (lossless)
```

## 📝 **LaTeX Integration Code:**

Add this to your document preamble:
```latex
\usepackage{graphicx}
\usepackage{subcaption} % for multiple maps
\graphicspath{{./maps/}} % set maps directory
```

### **Single Map Example:**
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{mapa_regionalizacion_ganadera.png}
\caption{Regionalización del Inventario Ganadero de Yucatán (SIAP 2023)}
\label{fig:mapa_regional}
\end{figure}
```

### **Multiple Maps (2x2 grid):**
```latex
\begin{figure}[h]
\centering
\begin{subfigure}[b]{0.48\textwidth}
    \includegraphics[width=\textwidth]{mapa_regionalizacion_ganadera.png}
    \caption{Regionalización Ganadera}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.48\textwidth}
    \includegraphics[width=\textwidth]{mapa_cobertura_sspi.png}
    \caption{Cobertura SSPi}
\end{subfigure}

\begin{subfigure}[b]{0.48\textwidth}
    \includegraphics[width=\textwidth]{mapa_meliponicultura.png}
    \caption{Distribución Meliponicultura}
\end{subfigure}
\hfill
\begin{subfigure}[b]{0.48\textwidth}
    \includegraphics[width=\textwidth]{mapa_macroproyecto_integral.png}
    \caption{Macroproyecto Integral}
\end{subfigure}
\caption{Mapas Territoriales del Macroproyecto Renacimiento Ganadero Maya}
\label{fig:mapas_territoriales}
\end{figure}
```

## 🎯 **Quick Start Workflow:**

### **1. Download Data (5 min)**
- Get Yucatán municipal boundaries from INEGI
- Prepare CSV with municipality names and cattle numbers

### **2. Create Basic Map (15 min)**
- Load municipal shapefile in QGIS
- Join cattle data by municipality code
- Apply graduated color styling

### **3. Style and Export (10 min)**
- Apply SADER color scheme
- Add legend, scale, north arrow
- Export as PNG at 300 DPI

### **4. Integrate in LaTeX (5 min)**
- Copy PNG to `maps/` folder
- Add figure code to document
- Compile and verify placement

## 💡 **Pro Tips:**
1. **Batch Export**: Use QGIS Atlas for multiple similar maps
2. **Consistent Styling**: Save QGIS project template with SADER styling
3. **Vector vs Raster**: Keep QGIS projects (.qgz) for future edits
4. **File Management**: Use descriptive filenames with prefixes (e.g., `fig01_`, `map_`)
5. **Quality Check**: Always preview in LaTeX before final compilation

## 🔄 **Update Workflow:**
When data changes:
1. Update CSV data files
2. Refresh QGIS layers (F5)
3. Re-export PNG maps
4. Recompile LaTeX document