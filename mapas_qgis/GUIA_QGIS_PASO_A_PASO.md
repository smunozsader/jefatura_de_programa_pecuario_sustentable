# 🗺️ GUÍA PASO A PASO: Crear Mapa de Análisis de Pareto en QGIS

## 🎯 **OBJETIVO: MOSTRAR LOS 11 MUNICIPIOS PARETO**
Destacar visualmente los municipios que concentran **80.3% de la ganadería** en Yucatán (principio de Pareto 80/20).

## 📋 **ARCHIVOS LISTOS PARA USAR:**

✅ `pareto_ganadero_yucatan_FINAL.csv` - Datos corregidos con nombres INEGI exactos
✅ `estilo_analisis_pareto.qml` - Estilo QML para análisis Pareto (NUEVO)
✅ `estilo_pareto_ganadero.qml` - Estilo QML alternativo
✅ `31mun.shp` - Shapefile municipal oficial INEGI

---

## 🚀 **PASOS EN QGIS (Versión 3.16+):**

### **PASO 1: Cargar Shapefile Municipal**
1. Abrir QGIS
2. Capa → Añadir Capa → Añadir Capa Vectorial
3. Navegar a: `H:\My Drive\2025. 1.0 JEFATURA PROGRAMA\marco_geoestadistico_inegi\conjunto_de_datos\`
4. Seleccionar: **31mun.shp** (municipios de Yucatán)
5. ✅ **Cargar**

### **PASO 2: Cargar CSV de Datos Pareto**
⚠️ **IMPORTANTE**: Primero debes cargar el CSV como capa antes de poder hacer la unión

1. Capa → Añadir Capa → **Añadir Capa de Texto Delimitado**
2. Navegar a: `H:\My Drive\2025. 1.0 JEFATURA PROGRAMA\mapas_qgis\`
3. Seleccionar: **pareto_ganadero_yucatan_FINAL.csv**
4. Configurar:
   - ✅ **Formato de archivo**: CSV
   - ✅ **Geometría**: Sin geometría (solo atributos)
   - ✅ **Detectar tipos de campo**: Automáticamente
5. Click **"Añadir"**
6. ✅ Ahora deberías ver **"pareto_ganadero_yucatan"** en tu panel de capas

### **PASO 3: Unir Datos del CSV con Shapefile**
1. Click derecho en la capa **"31mun"** → **Propiedades**
2. Ir a pestaña **"Uniones"**
3. Click en **"+"** (añadir unión)
4. Configurar:
   - **Unir capa**: pareto_ganadero_yucatan_FINAL
   - **Campo de unión**: cvegeo
   - **Campo objetivo**: CVEGEO
   - ✅ **Campos a unir**: [seleccionar todos]
5. **Aceptar** → **Aceptar**

**🔍 VERIFICACIÓN CRÍTICA:**
1. Click derecho en "31mun" → **Abrir tabla de atributos**
2. ✅ **DEBE aparecer**: `pareto_ganadero_yucatan_FINAL_pareto_grupo` (campo clave)
3. ✅ **Si NO aparece**: Repetir la unión verificando que los campos coincidan
4. ✅ **Cerrar tabla de atributos**

### **PASO 4: Configurar Análisis PARETO (MANUAL - MÁS SEGURO)**
1. Click derecho en capa **"31mun"** → **Propiedades**
2. Ir a pestaña **"Simbología"**
3. Cambiar de **"Símbolo único"** a **"Categorizado"**
4. En **"Columna"**: seleccionar **"pareto_ganadero_yucatan_FINAL_pareto_grupo"**
5. Click **"Clasificar"** (botón abajo)
6. **Configurar colores para ANÁLISIS PARETO:**

   **Para "Pareto":**
   - Color: **RGB(178, 34, 34)** - Rojo intenso
   - Contorno: **Blanco, grosor 1.0mm**
   - Etiqueta: **"11 Municipios PARETO (80.3%)"**

   **Para "Resto":**
   - Color: **RGB(144, 238, 144)** - Verde claro
   - Transparencia: **40%**
   - Etiqueta: **"95 Municipios RESTO (19.7%)"**

   **Para valores vacíos/NULL:**
   - Color: **RGB(211, 211, 211)** - Gris claro
   - Transparencia: **70%**
   - Etiqueta: **"Sin datos"**

7. ✅ **Aplicar** → **Aceptar**

### **PASO 4B: Estilo GRADUADO por Cantidad de Ganado (NUEVO)** 
1. Click derecho en capa **"31mun"** → **Propiedades**
2. Ir a pestaña **"Simbología"**
3. Click en **"Estilo"** → **"Cargar Estilo"**
4. Seleccionar: **estilo_graduado_ganado.qml** (intensidad por cabezas de ganado)
5. ✅ **Cargar** → **Aceptar**

### **PASO 4C: Estilo QML PARETO Categórico** 
1. Click derecho en capa **"31mun"** → **Propiedades**
2. Ir a pestaña **"Simbología"**
3. Click en **"Estilo"** → **"Cargar Estilo"**
4. Seleccionar: **estilo_analisis_pareto.qml** (análisis Pareto categórico)
5. ✅ **Cargar** → **Aceptar**

**⚠️ Si el QML no funciona, usar PASO 4C (configuración manual):**

### **PASO 4D: Configuración Manual GRADUADA (Método Avanzado)**
Para crear estilo graduado manualmente:

1. Click derecho en **"31mun"** → **Propiedades** → **Simbología**
2. Cambiar de **"Símbolo único"** a **"Graduado"**
3. **Campo valor**: `pareto_ganadero_yucatan_FINAL_ganado_bovino`
4. **Método**: Jenks (cortes naturales)
5. **Clases**: 6
6. **Rampa de color**: Rojos (o personalizada)
7. Click **"Clasificar"**

### **PASO 4E: Configuración Manual CATEGÓRICA (BACKUP)**
Si prefieres el análisis Pareto simple:

1. Click derecho en **"31mun"** → **Propiedades** → **Simbología**
2. Cambiar de **"Símbolo único"** a **"Categorizado"**
3. **Campo valor**: `pareto_ganadero_yucatan_FINAL_pareto_grupo`
4. Click **"Clasificar"** (debe mostrar Pareto, Resto, valores NULL)
5. **Configurar colores manualmente**:

**Para Pareto**:
   - Doble click en símbolo → **Color**: RGB(178, 34, 34) - Rojo intenso
   - **Contorno**: Blanco, grosor 1.0mm
   - **Etiqueta**: "11 Municipios PARETO (80.3%)"

**Para Resto**:
   - Doble click en símbolo → **Color**: RGB(144, 238, 144) - Verde claro
   - **Transparencia**: 40%
   - **Etiqueta**: "95 Municipios RESTO (19.7%)"

**Para valores vacíos/NULL**:
   - Doble click en símbolo → **Color**: RGB(230, 230, 230) - Gris claro
   - **Transparencia**: 70%
   - **Etiqueta**: "Sin clasificar"

6. ✅ **Aplicar** → **Aceptar**

### **PASO 5: Agregar Centros Estratégicos**
1. Capa → Añadir Capa → **Añadir Capa de Texto Delimitado**
2. Seleccionar: **centros_estrategicos_macroproyecto.csv**
3. Configurar:
   - **Campo X**: lon
   - **Campo Y**: lat
   - **CRS**: EPSG:4326 (WGS 84)
4. ✅ **Añadir**

### **PASO 6: Configurar Etiquetas**
1. Click derecho en capa municipal → **Propiedades**
2. Ir a pestaña **"Etiquetas"**
3. Configurar:
   - **Etiquetas simples**
   - **Etiquetar con**: municipio (o pareto_ganadero_yucatan_municipio)
   - **Fuente**: Arial, 8pt
   - **Color**: Negro
   - **Buffer**: Blanco, 0.5mm
4. ✅ **Aceptar**

---

## 🎨 **LEYENDAS DISPONIBLES:**

### **🎯 ESTILO GRADUADO (Recomendado) - Intensidad por Cabezas de Ganado:**

**🔴 Rojo Intenso** - **Muy Alto: 80,000+ cabezas** 
- Tizimín (131,108), Valladolid (80,146) - Líderes absolutos

**🔴 Rojo Medio-Alto** - **Alto: 50,000-79,999 cabezas**
- Mérida (58,514), Maxcanú (51,362) - Concentración alta

**🔴 Rojo Medio** - **Medio-Alto: 35,000-49,999 cabezas**
- Ticul (47,377), Tekax (40,613), Hunucmá (38,686), Umán (37,734), Motul (37,243), Kanasín (36,649), Oxkutzcab (36,407)

**🔴 Rojo Claro** - **Medio: 20,000-34,999 cabezas**
- Municipios con concentración media-alta

**🌸 Rosa** - **Bajo: 10,000-19,999 cabezas**  
- Municipios con concentración moderada

**🌸 Rosa Claro** - **Muy Bajo: 1-9,999 cabezas**
- Municipios con menor concentración ganadera

### **🎯 ESTILO CATEGÓRICO (Alternativo) - Análisis Pareto Simple:**

**🔴 Rojo Intenso** - **11 MUNICIPIOS PARETO (80.3% concentración)**
- Todos los municipios que cumplen el principio 80/20

**🟢 Verde Claro** - **95 MUNICIPIOS RESTO (19.7% concentración)**  
- Municipios con menor concentración ganadera

---

## 📊 **DATOS CLAVE DEL ANÁLISIS:**

| **Indicador** | **11 Municipios Pareto** | **% Estatal** |
|---|---|---|
| Superficie ganadera | 810,713 ha | **80.3%** |
| UPP totales | 5,241 | 76.8% |
| Vientres | 188,512 | 81.2% |
| **Principio Pareto** | **10.4% municipios** | **= 80% actividad** |

### **Distribución por Organizaciones Ganaderas:**
- **🔵 UGROY (Oriente)**: 7 municipios Pareto = 65.5% concentración estatal
  - Municipios: Tizimín, Panabá, Buctzotz, Dzilam González, Cenotillo, Sucila, San Felipe
- **🟡 UGRY (Centro)**: 4 municipios Pareto = 14.8% concentración estatal
  - Municipios: Tekax, Tzucacab, Peto, Izamal

---

## 🚨 **SOLUCIÓN DE PROBLEMAS - COLORACIÓN**

### **Problema: "Todos los municipios aparecen grises"**

**✅ SOLUCIÓN PASO A PASO:**

1. **Verificar unión exitosa**:
   - Click derecho en capa "31mun" → **Abrir tabla de atributos**
   - ¿Ves columnas que empiecen con "pareto_ganadero_yucatan_FINAL_"?
   - Si NO: Repetir PASO 3 (unión de datos)

2. **Verificar campo correcto en simbología**:
   - Propiedades → Simbología → Campo valor
   - Debe ser: **"pareto_ganadero_yucatan_FINAL_organizacion"**
   - Si aparece otro nombre, usa ese nombre exacto

3. **Forzar clasificación manual**:
   - En simbología categorizada → **"Clasificar"**
   - Debe aparecer: UGROY, UGRY, y valores vacíos
   - Si no aparece nada: El campo está mal seleccionado

4. **Verificar datos en tabla**:
   - Abrir tabla de atributos
   - Buscar municipio "Tizimín" → debe mostrar "UGROY"
   - Buscar municipio "Tekax de Álvaro Obregón" → debe mostrar "UGRY"

### **Problema: "El archivo QML no carga"**

**✅ SOLUCIÓN:**
- Usar **estilo_pareto_simple.qml** en lugar de estilo_pareto_ganadero.qml
- Si persiste: Usar configuración manual (PASO 4C)

### **Problema: "Solo algunos municipios se colorean"**

**✅ CAUSA:** Nombres de municipios no coinciden exactamente
**✅ SOLUCIÓN:** Usar archivo `pareto_ganadero_yucatan_FINAL.csv` (nombres corregidos)

---

## 🎯 **TIPS PARA MEJORAR EL MAPA:**

### **Personalización Avanzada:**
1. **Graduado por superficie**: Usar "superficie_ha" con 5 clases
2. **Etiquetas inteligentes**: Mostrar solo municipios Pareto principales  
3. **Transparencia**: 80% para municipios no prioritarios
4. **Anotaciones**: Agregar texto "Principio de Pareto: 80/20 Validado"

### **Layout para Exportación:**
1. **Proyecto** → **Nuevo Diseñador de Impresión**
2. **Agregar mapa, leyenda, título, escala**
3. **Formato**: A4 horizontal, 300 DPI
4. **Título sugerido**: "Análisis de Pareto - Concentración Ganadera Yucatán 2025"
5. **Subtítulo**: "Macroproyecto Renacimiento Ganadero Maya 2026-2030"

---

## 🚨 **SOLUCIÓN DE PROBLEMAS COMUNES:**

### **❌ "Todos los municipios aparecen en gris"**
**CAUSA MÁS COMÚN**: La unión no funcionó o el campo no se llama como esperamos
- ✅ **VERIFICAR**: Abrir tabla de atributos y buscar `pareto_ganadero_yucatan_organizacion`
- ✅ **SOLUCIÓN**: Si no aparece, repetir PASO 3 (unión)
- ✅ **ALTERNATIVA**: Usar configuración manual del PASO 4

### **❌ "No puedo hacer la unión - No aparece el CSV"**
**CAUSA**: No cargaste el CSV como capa primero
- ✅ **SOLUCIÓN**: Cargar CSV usando "Añadir Capa de Texto Delimitado" ANTES de intentar la unión
- ✅ **VERIFICAR**: El CSV debe aparecer en el panel de capas antes de la unión

### **❌ "No se pueden unir los datos"**
**CAUSA**: Campos incompatibles entre shapefile y CSV
- ✅ Verificar que CVEGEO en shapefile sea texto (no número)
- ✅ Asegurar que cve_muni en CSV sea texto con 5 dígitos
- ✅ **Ejemplo correcto**: "31094" para Tizimín

### **❌ "El estilo QML no se aplica"**
**CAUSA**: La unión no funcionó o el nombre del campo cambió
- ✅ **SOLUCIÓN DEFINITIVA**: Usar configuración manual (PASO 4)
- ✅ Verificar que existe el campo "pareto_ganadero_yucatan_organizacion"
- ✅ Si el campo tiene otro nombre, usar ese nombre en la configuración

### **❌ "Solo aparecen algunos municipios coloreados"**
**CAUSA**: Los valores en el CSV no coinciden exactamente
- ✅ Verificar que los valores sean exactamente "UGROY" y "UGRY"
- ✅ Revisar que no haya espacios extra o caracteres especiales
- ✅ **SOLUCIÓN**: Usar el CSV proporcionado sin modificaciones

### **❌ "Los puntos no aparecen correctamente"**
**CAUSA**: Problemas de coordenadas o sistema de referencia
- ✅ Verificar CRS: debe ser EPSG:4326
- ✅ Coordenadas válidas: lat entre 19-22, lon entre -90 a -87
- ✅ Zoom al extent de la capa si están fuera de vista

---

## 📞 **SOPORTE TÉCNICO:**

**Datos oficiales validados según:**
- Padrón Ganadero Nacional 2025 (SINIIGA-SENASICA)
- Marco Geoestadístico INEGI 2025
- Análisis Pareto científicamente fundamentado

**Contacto del autor:**
MVZ Sergio Muñoz de Alba Medrano, Consultor Independiente
Comisionado por SEDER - Gobierno del Estado de Yucatán

---

## ✅ **VERIFICACIÓN FINAL - MAPA CORRECTO:**

Tu mapa está correcto si ves:
- **� 11 municipios en ROJO INTENSO** (Municipios PARETO - 80.3% concentración)
- **🟢 95 municipios en VERDE CLARO** (Municipios RESTO - 19.7% concentración) 
- **📍 Principio de Pareto validado**: 10.4% del territorio = 80.3% del ganado

### **Los 11 Municipios que DEBEN aparecer en ROJO (Pareto):**
1. **Tizimín** ⭐ (131,108 cabezas - líder absoluto)
2. **Valladolid** (80,146 cabezas)
3. **Mérida** (58,514 cabezas)
4. **Maxcanú** (51,362 cabezas)
5. **Ticul** (47,377 cabezas)
6. **Tekax de Álvaro Obregón** (40,613 cabezas)
7. **Hunucmá** (38,686 cabezas)
8. **Umán** (37,734 cabezas)
9. **Motul** (37,243 cabezas)
10. **Kanasín** (36,649 cabezas)
11. **Oxkutzcab** (36,407 cabezas)

### **Todos los demás municipios DEBEN aparecer en VERDE CLARO (Resto)**

**✅ Validación**: Si ves exactamente 11 municipios en rojo y el resto en verde claro, ¡el análisis Pareto está correcto!

**Si no ves estos colores exactos, revisa la sección de problemas comunes arriba.**

---

## 🔧 **CORRECCIÓN DE DATOS MUNICIPALES**

### **Problema Inicial: Codificación UTF-8**
Los nombres de municipios en el CSV original tenían problemas de codificación que impedían la unión correcta con el shapefile INEGI:
- Panabá aparecía como "PanabÃ¡"
- Sucilá aparecía como "SucilÃ¡"
- Otros municipios con acentos también tenían problemas

### **Solución Implementada**
1. **Extracción desde fuente oficial**: Se leyó el archivo Excel INEGI `AGEEML_2025102162256_UTF.xlsx`
2. **Script Python desarrollado**: `extraer_municipios_inegi.py` para obtener nombres con codificación correcta
3. **Archivo final**: `pareto_ganadero_yucatan_FINAL.csv` con nombres exactos según INEGI

### **Resultado**
✅ **Unión QGIS exitosa**: Los nombres coinciden exactamente con el shapefile oficial
✅ **Visualización correcta**: Todos los municipios Pareto se colorean según su organización
✅ **Datos oficiales**: Garantiza consistencia con el marco geoestadístico nacional

---

¡**Listo para crear mapas profesionales del análisis de Pareto!** 🎉