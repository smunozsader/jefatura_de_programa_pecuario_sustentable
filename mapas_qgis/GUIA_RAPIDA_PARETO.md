# 🎯 GUÍA RÁPIDA: Mapa de Análisis PARETO en QGIS

## ⚡ **OBJETIVO CLARO**
Mostrar los **11 municipios que concentran el 80.3% de la ganadería** en Yucatán (principio de Pareto 80/20).

---

## 🚀 **PASOS RÁPIDOS:**

### **1. Cargar Datos**
```
1. Abrir QGIS
2. Cargar: 31mun.shp (shapefile municipal)
3. Cargar: pareto_ganadero_yucatan_FINAL.csv (como tabla)
4. Unir datos: CVE_MUN ↔ CVEGEO
```

### **2A. ESTILO GRADUADO - Intensidad por Ganado (RECOMENDADO)**
```
1. Click derecho en "31mun" → Propiedades → Simbología
2. Estilo → Cargar Estilo → estilo_graduado_ganado.qml
3. Cargar → Aceptar
✅ ¡Gradiente rojo perfecto!
```

### **2B. ESTILO CATEGÓRICO - Pareto Simple**
```
1. Click derecho en "31mun" → Propiedades → Simbología  
2. Estilo → Cargar Estilo → estilo_analisis_pareto.qml
3. Cargar → Aceptar
✅ ¡Clasificación binaria!
```

### **2B. MÉTODO MANUAL (si QML falla)**
```
1. Propiedades → Simbología → Categorizado
2. Campo: "pareto_ganadero_yucatan_FINAL_pareto_grupo"
3. Clasificar
4. Configurar colores:
   - Pareto → Rojo RGB(178,34,34)
   - Resto → Verde RGB(144,238,144) + 40% transparencia
```

---

## ✅ **RESULTADO ESPERADO:**

### 🔴 **11 Municipios en ROJO (Pareto 80.3%)**
1. **Tizimín** ⭐ - 131,108 cabezas (líder absoluto)
2. **Valladolid** - 80,146 cabezas  
3. **Mérida** - 58,514 cabezas
4. **Maxcanú** - 51,362 cabezas
5. **Ticul** - 47,377 cabezas
6. **Tekax de Álvaro Obregón** - 40,613 cabezas
7. **Hunucmá** - 38,686 cabezas
8. **Umán** - 37,734 cabezas
9. **Motul** - 37,243 cabezas
10. **Kanasín** - 36,649 cabezas
11. **Oxkutzcab** - 36,407 cabezas

### 🟢 **95 Municipios en VERDE (Resto 19.7%)**
- Todos los demás municipios de Yucatán
- Transparencia 40% para destacar los Pareto

---

## 🚨 **SOLUCIÓN RÁPIDA DE PROBLEMAS**

### **"Todos aparecen grises"**
```
✅ Verificar unión: ¿Aparece columna "pareto_ganadero_yucatan_FINAL_pareto_grupo"?
✅ Si NO: Rehacer unión CVE_MUN ↔ CVEGEO
```

### **"Solo algunos se colorean"**
```
✅ Usar archivo pareto_ganadero_yucatan_FINAL.csv (nombres corregidos)
✅ NO usar archivos anteriores con problemas UTF-8
```

### **"El QML no funciona"**
```
✅ Usar método manual (2B)
✅ Verificar que el campo sea exactamente: pareto_ganadero_yucatan_FINAL_pareto_grupo
```

---

## 📊 **VALIDACIÓN DEL PRINCIPIO PARETO**

### **Concentración Territorial:**
- 🏆 **11 municipios** = 10.4% del territorio estatal
- 🐄 **558,839 cabezas** = 80.3% del ganado estatal  
- ✅ **Principio 80/20 VALIDADO**

### **Epicentros Ganaderos:**
- 🥇 **Tizimín**: 23.5% del ganado estatal (1 solo municipio)
- 🥈 **Valladolid**: 14.3% del ganado estatal
- 🥉 **Top 3 combinados**: 43.9% del ganado estatal

### **Implicaciones Estratégicas:**
- 📍 **Focalización territorial**: 80% recursos en 11 municipios
- 💰 **Eficiencia presupuestal**: Máximo impacto con mínima dispersión
- 🎯 **Targeting perfecto**: Para el Macroproyecto Renacimiento Ganadero Maya

---

**🎉 ¡Con esta guía tendrás tu mapa Pareto en menos de 5 minutos!**