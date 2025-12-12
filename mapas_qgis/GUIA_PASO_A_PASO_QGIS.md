# 🗺️ Guía Paso a Paso: Mapa Pareto Ganadero Yucatán en QGIS

## ⚠️ PROBLEMA IDENTIFICADO Y SOLUCIONADO

**Error anterior**: El CSV tenía códigos CVEGEO incorrectos y municipios equivocados (Mérida, Hunucmá, Umán, etc.)

**Solución aplicada**: CSV regenerado con códigos CVEGEO oficiales de INEGI y municipios correctos del análisis LaTeX

---

## 📋 PASO 1: Preparar QGIS

### 1.1 Cerrar proyecto actual (si está abierto)
```
Proyecto → Cerrar
```

### 1.2 Crear nuevo proyecto
```
Proyecto → Nuevo
```

### 1.3 Guardar proyecto
```
Proyecto → Guardar como...
Nombre: analisis_pareto_ganadero_yucatan.qgz
Ubicación: H:\My Drive\2025. 1.0 JEFATURA PROGRAMA\mapas_qgis\
```

---

## 📋 PASO 2: Cargar Shapefile INEGI

### 2.1 Añadir capa vectorial
```
Menú: Capa → Añadir Capa → Añadir Capa Vectorial
O: Ctrl + Shift + V
```

### 2.2 Seleccionar archivo
```
Fuente: H:\My Drive\2025. 1.0 JEFATURA PROGRAMA\marco_geoestadistico_inegi\conjunto_de_datos\31mun.shp
Codificación: UTF-8
Añadir → Cerrar
```

**✅ Verificar**: Debes ver el mapa de Yucatán con 106 municipios en gris

---

## 📋 PASO 3: Unir Datos CSV de Pareto

### 3.1 Añadir capa delimitada (CSV)
```
Menú: Capa → Añadir Capa → Añadir Capa de Texto Delimitado
```

### 3.2 Configurar importación CSV
```
Nombre de archivo: H:\My Drive\2025. 1.0 JEFATURA PROGRAMA\mapas_qgis\pareto_ganadero_yucatan_FINAL.csv

Formato de archivo:
  ☑ CSV (valores separados por coma)
  
Opciones de registro:
  Primera fila de datos: 2 (la fila 1 es el encabezado)
  ☑ Primera línea como nombre de campo
  
Definición de geometría:
  ⦿ Sin geometría (únicamente tabla de atributos)
  
Añadir → Cerrar
```

**✅ Verificar**: En el panel Capas debe aparecer `pareto_ganadero_yucatan_FINAL` (sin ícono de mapa, solo tabla)

### 3.3 Crear unión entre shapefile y CSV

```
1. Click derecho en capa "31mun" → Propiedades
2. En el menú lateral izquierdo: Uniones
3. Click en botón verde "+" (Añadir nueva unión)
4. Configurar:
   
   Capa de unión: pareto_ganadero_yucatan_FINAL
   Campo de unión: CVEGEO
   Campo objetivo: CVEGEO
   
   ☐ Almacenar campos de unión en memoria (dejar SIN marcar)
   ☐ Crear índice de atributos en el campo de unión (opcional)
   
   Prefijo de nombre de campo personalizado: [DEJAR EN BLANCO]
   
5. Aceptar (cerrar ventana de unión)
6. Aceptar (cerrar ventana de Propiedades)
```

**✅ Verificar**: 
```
1. Click derecho en capa "31mun" → Abrir tabla de atributos
2. Scroll horizontal hacia la derecha
3. Debes ver columnas nuevas: municipio, superficie_ha, organizacion, pareto_grupo, porcentaje_acumulado
4. Verificar que Tizimín (fila con CVEGEO = 31096) tenga:
   - municipio: Tizimín
   - superficie_ha: 260595
   - pareto_grupo: Pareto
```

**⚠️ SI NO VES LAS COLUMNAS**: La unión falló. Revisar:
- Que el CSV se cargó correctamente
- Que ambas capas tienen campo "CVEGEO"
- Que no haya espacios extra en los valores

---

## 📋 PASO 4: Aplicar Estilo Categórico (Pareto vs Nivel2 vs Resto)

### 4.1 Cargar archivo QML
```
1. Click derecho en capa "31mun" → Propiedades
2. En menú lateral izquierdo: Simbología
3. En la parte inferior: Estilo → Cargar estilo...
4. Seleccionar archivo: H:\My Drive\2025. 1.0 JEFATURA PROGRAMA\mapas_qgis\estilo_analisis_pareto.qml
5. Cargar estilo
6. Aceptar
```

**✅ RESULTADO ESPERADO**:
- 11 municipios en ROJO intenso (Pareto): Tizimín, Panabá, Tekax, Buctzotz, Dzilam González, Tzucacab, Cenotillo, Peto, Sucilá, Izamal, San Felipe
- 9 municipios en NARANJA (Nivel2): Temozón, Tunkás, Yaxcabá, Kinchil, Valladolid, Maxcanú, Sotuta, Calotmul, Espita
- 86 municipios en GRIS CLARO (Resto): todos los demás

**❌ SI VES MUNICIPIOS INCORRECTOS EN ROJO** (Mérida, Hunucmá, Umán, Ticul):
- La unión NO se aplicó correctamente
- Volver al PASO 3.3 y verificar la unión

---

## 📋 PASO 5: (OPCIONAL) Aplicar Estilo Graduado por Superficie

### 5.1 Cambiar a estilo graduado
```
1. Click derecho en capa "31mun" → Propiedades → Simbología
2. Estilo → Cargar estilo...
3. Seleccionar: H:\My Drive\2025. 1.0 JEFATURA PROGRAMA\mapas_qgis\estilo_graduado_ganado.qml
4. Cargar estilo
5. Aceptar
```

**✅ RESULTADO ESPERADO**:
- Gradiente de rojo a rosa claro
- Tizimín (260K ha) en rojo más intenso
- Panabá (100K ha) en rojo medio
- Municipios pequeños en rosa claro

---

## 📋 PASO 6: Añadir Elementos Cartográficos

### 6.1 Añadir escala
```
Vista → Decoraciones → Barra de escala
☑ Habilitar barra de escala
Unidades: Kilómetros
Aceptar
```

### 6.2 Añadir flecha norte
```
Vista → Decoraciones → Flecha de Norte
☑ Habilitar flecha de Norte
Aceptar
```

### 6.3 Añadir título
```
Vista → Decoraciones → Etiqueta de Título
☑ Habilitar etiqueta de título
Texto: Análisis de Pareto: Concentración Ganadera en Yucatán
Fuente: Arial 16pt Bold
Aceptar
```

---

## 📋 PASO 7: Exportar Mapa para LaTeX

### 7.1 Ajustar encuadre
```
1. Zoom para que todo Yucatán sea visible con márgenes
2. Vista → Zoom a Capa (si es necesario)
```

### 7.2 Exportar imagen
```
Proyecto → Importar/Exportar → Exportar Mapa a Imagen

Archivo de salida: H:\My Drive\2025. 1.0 JEFATURA PROGRAMA\mapas_qgis\mapa_pareto_ganadero_yucatan.png

Extensión del mapa: [Usar encuadre actual del lienzo]

Resolución de salida: 300 dpi

Anchura / Altura (píxeles): 
  - Ancho: 5000 px (aprox. 42 cm a 300 dpi)
  - Alto: se calcula automáticamente

☑ Dibujar decoraciones activas
☐ Añadir georreferenciación (únicamente archivos de imagen TIFF y GeoTIFF)

Guardar
```

**✅ Archivo generado**: `mapa_pareto_ganadero_yucatan.png` listo para incluir en LaTeX

---

## 📋 PASO 8: Guardar Proyecto QGIS

```
Proyecto → Guardar
```

**✅ Proyecto guardado**: `analisis_pareto_ganadero_yucatan.qgz` con todas las configuraciones

---

## 🔍 VERIFICACIÓN FINAL

### Checklist de municipios CORRECTOS en ROJO (Pareto):

- [ ] **Tizimín** - Municipio más grande, noreste
- [ ] **Panabá** - Norte, cerca de costa
- [ ] **Tekax de Álvaro Obregón** - Sur
- [ ] **Buctzotz** - Norte
- [ ] **Dzilam González** - Norte, costa
- [ ] **Tzucacab** - Sur
- [ ] **Cenotillo** - Centro-norte
- [ ] **Peto** - Sur
- [ ] **Sucilá** - Norte
- [ ] **Izamal** - Centro
- [ ] **San Felipe** - Norte, costa

### Checklist de municipios que NO deben estar en ROJO:

- [ ] ❌ Mérida (capital) - debe estar GRIS
- [ ] ❌ Hunucmá (cerca de Mérida) - debe estar GRIS
- [ ] ❌ Umán (cerca de Mérida) - debe estar GRIS
- [ ] ❌ Progreso (puerto) - debe estar GRIS
- [ ] ❌ Motul - debe estar GRIS
- [ ] ❌ Kanasín - debe estar GRIS
- [ ] ❌ Oxkutzcab - debe estar GRIS
- [ ] ❌ Ticul - debe estar GRIS

---

## ⚠️ SOLUCIÓN DE PROBLEMAS

### Problema 1: Municipios incorrectos en rojo

**Causa**: La unión entre shapefile y CSV no se aplicó correctamente

**Solución**:
1. Eliminar unión: Click derecho en "31mun" → Propiedades → Uniones → Seleccionar unión → Botón "-" (eliminar)
2. Eliminar CSV: Click derecho en "pareto_ganadero_yucatan_FINAL" → Quitar capa
3. Volver a PASO 3 y repetir cuidadosamente

### Problema 2: Columnas del CSV no aparecen en tabla de atributos

**Causa**: Campo de unión no coincide

**Solución**:
1. Verificar que CSV tiene columna "CVEGEO" (con mayúsculas)
2. Verificar que shapefile tiene campo "CVEGEO" (Ver tabla de atributos de 31mun)
3. Recrear CSV ejecutando: `python "ANALISIS Y SCRIPTS\generar_csv_pareto_correcto.py"`

### Problema 3: Estilo QML no carga correctamente

**Causa**: Nombres de campos en QML no coinciden con datos unidos

**Solución**:
1. Los archivos QML ya fueron corregidos para usar nombres sin prefijo
2. Si aún falla, aplicar estilo manualmente:
   - Simbología → Categorizado
   - Columna: pareto_grupo
   - Clasificar
   - Asignar colores: Pareto = #B22222 (rojo), Nivel2 = #FF8C00 (naranja), resto = #E0E0E0 (gris)

### Problema 4: Nombres de municipios con caracteres raros

**Causa**: Codificación UTF-8 no reconocida

**Solución**:
1. Al cargar CSV: Verificar que Codificación sea "UTF-8"
2. Al cargar shapefile: Verificar que Codificación sea "UTF-8"
3. Preferencias → Fuentes de Datos → Codificación de archivo de texto: UTF-8

---

## 📊 DATOS TÉCNICOS

### Códigos CVEGEO correctos (Top 11 Pareto):

| CVEGEO | Municipio | Superficie (ha) | Org | % Acum |
|--------|-----------|-----------------|-----|--------|
| 31096 | Tizimín | 260,595 | UGROY | 35.2% |
| 31057 | Panabá | 100,026 | UGROY | 48.1% |
| 31079 | Tekax de Álvaro Obregón | 78,245 | UGRY | 54.3% |
| 31006 | Buctzotz | 74,793 | UGROY | 59.6% |
| 31029 | Dzilam González | 55,102 | UGROY | 63.5% |
| 31098 | Tzucacab | 50,688 | UGRY | 67.0% |
| 31012 | Cenotillo | 43,279 | UGROY | 70.0% |
| 31058 | Peto | 41,168 | UGRY | 72.8% |
| 31070 | Sucilá | 39,712 | UGROY | 75.6% |
| 31040 | Izamal | 33,903 | UGRY | 78.0% |
| 31065 | San Felipe | 33,203 | UGROY | 80.3% |

### Códigos CVEGEO municipios Nivel 2 (12-20):

| CVEGEO | Municipio | Superficie (ha) | % Acum |
|--------|-----------|-----------------|--------|
| 31085 | Temozón | 27,754 | 82.3% |
| 31097 | Tunkás | 27,262 | 84.2% |
| 31104 | Yaxcabá | 25,045 | 85.9% |
| 31044 | Kinchil | 25,378 | 87.6% |
| 31102 | Valladolid | 23,992 | 89.2% |
| 31048 | Maxcanú | 23,180 | 90.7% |
| 31069 | Sotuta | 21,142 | 92.1% |
| 31008 | Calotmul | 20,638 | 93.5% |
| 31032 | Espita | 19,442 | 94.8% |

---

## 📝 NOTAS FINALES

- **Fuente oficial**: Padrón Ganadero Nacional 2025 (Analisis Pareto Ganadero Yucatan.tex)
- **Métrica**: Superficie ganadera en hectáreas (NO número de cabezas)
- **Validación**: 11 municipios = 80.3% concentración (Principio de Pareto)
- **Fecha**: Diciembre 2025
- **Autor**: MVZ Sergio Muñoz de Alba Medrano
- **Institución**: SEDER Yucatán
