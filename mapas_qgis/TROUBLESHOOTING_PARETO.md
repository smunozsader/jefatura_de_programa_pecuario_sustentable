# 🔍 TROUBLESHOOTING - Municipios Pareto no se muestran

## 🚨 **DIAGNÓSTICO PASO A PASO**

### **CHECK 1: ¿Está el CSV cargado como capa?**
1. Mira el **panel de capas** (izquierda de QGIS)
2. ¿Ves **"pareto_ganadero_yucatan"** listado?
   - ✅ **SÍ** → Continúa al Check 2
   - ❌ **NO** → **SOLUCIÓN**: Repetir PASO 2 de la guía

### **CHECK 2: ¿Funcionó la unión correctamente?**
1. Click derecho en **"31mun"** → **Abrir tabla de atributos**
2. Scroll hacia la derecha para ver TODAS las columnas
3. ¿Ves columnas que empiecen con **"pareto_ganadero_yucatan_"**?
   - Ejemplo: **"pareto_ganadero_yucatan_municipio"**
   - Ejemplo: **"pareto_ganadero_yucatan_nivel_prioridad"**

**RESULTADO:**
- ✅ **SÍ veo esas columnas** → La unión funcionó, continúa al Check 3
- ❌ **NO veo esas columnas** → **PROBLEMA**: La unión falló, ve a SOLUCIÓN A

### **CHECK 3: ¿Hay datos en las filas unidos?**
1. En la tabla de atributos abierta
2. Busca municipios como **Tizimín, Panabá, Tekax**
3. ¿Tienen valores en las columnas **"pareto_ganadero_yucatan_..."**?
   - ¿Dice **"Nivel_1_Pareto"** en la columna nivel_prioridad?

**RESULTADO:**
- ✅ **SÍ tienen datos** → Los datos están unidos correctamente, continúa al Check 4
- ❌ **NO tienen datos o dice NULL** → **PROBLEMA**: Códigos municipales no coinciden, ve a SOLUCIÓN B

### **CHECK 4: ¿Se aplicó el estilo correctamente?**
1. Click derecho en **"31mun"** → **Propiedades** → **Simbología**
2. ¿Qué tipo de simbología está seleccionada?
   - ¿Dice **"Categorizada"**?
   - ¿El campo es **"pareto_ganadero_yucatan_nivel_prioridad"**?
   - ¿Hay 3 categorías listadas?

**RESULTADO:**
- ✅ **SÍ está categorizada correctamente** → Ve a SOLUCIÓN C (refrescar)
- ❌ **NO está categorizada o campo incorrecto** → Ve a SOLUCIÓN D

---

## 🛠️ **SOLUCIONES**

### **SOLUCIÓN A: La unión falló**
**PROBLEMA**: El CSV no se cargó correctamente o la unión no funcionó

**PASOS:**
1. **Eliminar la unión actual**:
   - Propiedades de "31mun" → Uniones → Seleccionar unión → Click "-" → Aceptar

2. **Recargar el CSV correctamente**:
   - Capa → Añadir Capa → **Añadir Capa de Texto Delimitado**
   - Archivo: `pareto_ganadero_yucatan.csv`
   - **IMPORTANTE**: Geometría = **"Sin geometría"**
   - Añadir

3. **Repetir la unión**:
   - Propiedades "31mun" → Uniones → "+" 
   - Unir capa: **pareto_ganadero_yucatan**
   - Campo unión: **cve_muni**
   - Campo objetivo: **CVEGEO**

### **SOLUCIÓN B: Códigos municipales no coinciden**
**PROBLEMA**: Los códigos CVEGEO y cve_muni no son compatibles

**VERIFICAR CÓDIGOS:**
1. **En el shapefile** (tabla de atributos "31mun"):
   - ¿CVEGEO tiene formato "31001", "31094", etc.?

2. **En el CSV** (tabla de atributos "pareto_ganadero_yucatan"):
   - ¿cve_muni tiene el mismo formato?

**Si los códigos son diferentes:**
- Buscar campo alternativo en el shapefile (CVE_MUN, CVEMUN, etc.)
- Usar ese campo como "Campo objetivo" en la unión

### **SOLUCIÓN C: Refrescar el estilo**
**PROBLEMA**: El estilo está correcto pero no se muestra

**PASOS:**
1. Click derecho en "31mun" → **Zoom a la capa**
2. **F5** para refrescar el mapa
3. Click en **"Aplicar"** en las propiedades de simbología
4. Si no funciona, **cerrar y reabrir** las propiedades de la capa

### **SOLUCIÓN D: Aplicar estilo manualmente**
**PROBLEMA**: El QML no se cargó correctamente

**APLICAR ESTILO MANUAL:**
1. Propiedades "31mun" → **Simbología**
2. Cambiar de "Símbolo único" a **"Categorizada"**
3. **Campo**: Buscar **"pareto_ganadero_yucatan_nivel_prioridad"**
4. Click **"Clasificar"**
5. **Configurar colores manualmente**:
   - **Nivel_1_Pareto** → Verde RGB(0,102,51)
   - **Nivel_2_Complementario** → Dorado RGB(204,153,0)
   - **otros valores** → Gris RGB(200,200,200)

---

## 📞 **SI NADA FUNCIONA - DIAGNÓSTICO FINAL**

### **VERIFICACIÓN COMPLETA:**
1. **¿Qué versión de QGIS usas?** (Ayuda → Acerca de)
2. **¿Los archivos están en la ruta correcta?**
3. **¿Puedes abrir el CSV en Excel?** (verificar que tiene datos)

### **SOLUCIÓN DE EMERGENCIA - Manual:**
1. **Abrir ambos archivos por separado** (shapefile + CSV)
2. **Identificar manualmente** municipios Pareto en el shapefile
3. **Seleccionar municipios Pareto** (Ctrl+Click)
4. **Cambiar color** a verde solo para seleccionados
5. **Crear nueva capa** desde selección

---

## 🎯 **DIME QUÉ ENCONTRASTE:**

Ejecuta **CHECK 1, 2, 3, 4** y dime **exactamente** qué viste en cada paso. Con esa información te daré la solución precisa.