# GUÍA DEFINITIVA: Aplicar Coloración en QGIS

## 🎯 **OBJETIVO**
Colorear los municipios de Yucatán según su organización ganadera:
- 🔵 **Azul SADER (RGB: 0,51,102)**: UGROY (Oriente)  
- 🟡 **Dorado SADER (RGB: 204,153,0)**: UGRY (Centro)
- ⚪ **Gris claro**: Sin clasificar

---

## ⚡ **MÉTODO 1: ARCHIVO QML (MÁS RÁPIDO)**

### Opción A: estilo_pareto_simple.qml (RECOMENDADO)
```
1. Click derecho en capa "31mun" → Propiedades
2. Simbología → Estilo → Cargar Estilo  
3. Seleccionar: estilo_pareto_simple.qml
4. Cargar → Aceptar
```

### Opción B: estilo_pareto_ganadero.qml (BACKUP)
```
1. Same steps as above
2. Seleccionar: estilo_pareto_ganadero.qml  
3. Si no funciona → usar Método 2
```

---

## 🔧 **MÉTODO 2: CONFIGURACIÓN MANUAL (100% EFECTIVO)**

### **PASO 1: Verificar Datos Unidos**
```
1. Click derecho "31mun" → Abrir tabla de atributos
2. ¿Ves columna "pareto_ganadero_yucatan_FINAL_organizacion"?
   ✅ SÍ → Continuar PASO 2
   ❌ NO → Rehacer unión de datos (PASO 3 de la guía principal)
```

### **PASO 2: Configurar Simbología Categorizada**
```
1. Click derecho "31mun" → Propiedades → Simbología
2. Cambiar de "Símbolo único" a "Categorizado"
3. Campo valor: "pareto_ganadero_yucatan_FINAL_organizacion"
4. Click "Clasificar"
```

### **PASO 3: Asignar Colores Manualmente**

**Para categoría "UGROY":**
```
1. Doble click en símbolo cuadrado
2. Color → RGB: R=0, G=51, B=102 (Azul SADER)
3. Contorno → Blanco, grosor 0.5mm
4. Etiqueta → "UGROY (Oriente)"
5. Aceptar
```

**Para categoría "UGRY":**
```  
1. Doble click en símbolo cuadrado
2. Color → RGB: R=204, G=153, B=0 (Dorado SADER)
3. Contorno → Blanco, grosor 0.5mm  
4. Etiqueta → "UGRY (Centro)"
5. Aceptar
```

**Para valores vacíos/NULL:**
```
1. Doble click en símbolo cuadrado
2. Color → RGB: R=230, G=230, B=230 (Gris claro)
3. Transparencia → 70%
4. Contorno → Gris, grosor 0.2mm
5. Etiqueta → "Sin clasificar"  
6. Aceptar
```

### **PASO 4: Aplicar y Verificar**
```
1. Click "Aplicar" → "Aceptar"
2. Verificar que municipios clave estén coloreados:
   - Tizimín → AZUL (UGROY)
   - Valladolid → AZUL (UGROY)  
   - Tekax → DORADO (UGRY)
   - Maxcanú → DORADO (UGRY)
```

---

## 🚨 **DIAGNÓSTICO DE PROBLEMAS**

### **"Todos aparecen grises"**
**CAUSA:** Campo de unión incorrecto
**SOLUCIÓN:** 
1. Verificar que campo sea exactamente: `pareto_ganadero_yucatan_FINAL_organizacion`
2. Si nombre es diferente, usar el nombre exacto que aparece

### **"Solo algunos se colorean"**  
**CAUSA:** Nombres de municipios no coinciden
**SOLUCIÓN:** Usar archivo `pareto_ganadero_yucatan_FINAL.csv` (nombres INEGI correctos)

### **"El QML no carga"**
**CAUSA:** Versión QGIS o campo incorrecto  
**SOLUCIÓN:** Usar Método 2 (configuración manual)

### **"No veo la columna organizacion"**
**CAUSA:** Unión de datos falló
**SOLUCIÓN:**
1. Eliminar unión existente (Propiedades → Uniones → Seleccionar → -)
2. Crear nueva unión:
   - Capa unir: pareto_ganadero_yucatan_FINAL
   - Campo unión: CVEGEO  
   - Campo objetivo: CVE_MUN
3. Aplicar → Aceptar

---

## ✅ **RESULTADO ESPERADO**

### **Municipios que DEBEN aparecer en AZUL (UGROY):**
- Tizimín ⭐ (131,108 cabezas - municipio líder)
- Valladolid ⭐ (80,146 cabezas - segundo lugar)
- Otros municipios UGROY (Chemax, Espita, etc.)

### **Municipios que DEBEN aparecer en DORADO (UGRY):**  
- Tekax de Álvaro Obregón ⭐ (40,613 cabezas)
- Maxcanú ⭐ (51,362 cabezas) 
- Ticul ⭐ (47,377 cabezas)
- Mérida, Hunucmá, Umán, Motul, Kanasín, Oxkutzcab

### **Concentración Pareto Validada:**
- 📊 **11 municipios** = 80.3% del ganado estatal
- 📊 **558,839 cabezas** total (SIAP 2023)
- 📊 **2 organizaciones** territorialmente diferenciadas

---

**🎉 ¡Con esta guía tu mapa DEBE funcionar correctamente!**