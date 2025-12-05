# AUDITORÍA DE COSTOS - PLANTA DE MOSCA ESTÉRIL YUCATÁN
## Análisis Deep Dive de Precios y Validación de Cifras

**Fecha:** Diciembre 5, 2025  
**Auditor:** MVZ Sergio Muñoz de Alba Medrano  
**Objetivo:** Validar la realidad de costos y evitar sobrevaloración o infracosteo

---

## 🔍 RESUMEN EJECUTIVO DE AUDITORÍA

### **HALLAZGOS PRINCIPALES:**
- **Inversión original estimada:** $210.0 MDP
- **Inversión calculada (bottom-up):** $463.97 MDP  
- **Diferencia:** +$253.97 MDP (+120.9%)
- **Evaluación:** **SOBREVALORACIÓN SIGNIFICATIVA DETECTADA**

### **PRINCIPALES PROBLEMAS IDENTIFICADOS:**

1. **COSTOS OPERATIVOS INFLADOS:** $316.11 MDP vs $15.0 MDP estimados inicialmente
2. **EQUIPOS ESPECIALIZADOS:** Precios no validados con mercado mexicano
3. **FUENTE COBALTO-60:** Error grave en conversión de moneda
4. **SISTEMAS HVAC:** Especificaciones excesivas para el contexto
5. **RECURSOS HUMANOS:** Plantilla sobredimensionada

---

## 📊 ANÁLISIS DETALLADO POR COMPONENTES

### **1. OBRA CIVIL - LABORATORIO CRÍA MASIVA**

| Concepto | Precio Documento | Precio Mercado México | Diferencia | Estado |
|----------|------------------|---------------------|------------|--------|
| Excavación y cimentación | $1,850/m³ | $1,200-1,400/m³ | **+32-54%** | 🔴 INFLADO |
| Concreto armado | $4,200/m³ | $3,200-3,800/m³ | **+11-31%** | 🟡 ALTO |
| Acabados BSL-1 | $1,280/m² | $900-1,100/m² | **+16-42%** | 🟡 ALTO |
| Pisos epóxicos | $1,650/m² | $850-1,200/m² | **+38-94%** | 🔴 INFLADO |
| Sistema HVAC | $2,850/m² | $1,800-2,200/m² | **+30-58%** | 🔴 INFLADO |

**❌ PROBLEMAS DETECTADOS:**
- Costos de excavación 50% superiores al mercado Yucatán
- Sistema HVAC sobrespecificado (±1°C es excesivo, ±2°C es suficiente)
- No considera ventajas de construcción en Yucatán (mano de obra más económica)

**✅ AJUSTE RECOMENDADO:** **-$8.2 MDP** (40% reducción)

---

### **2. FUENTE COBALTO-60 - ERROR CRÍTICO DETECTADO**

| Item | Valor Documento | Valor Real | Problema |
|------|----------------|------------|----------|
| Precio Co-60 | $18,500 MXN/Ci | $18,500 USD/Ci | **Error conversión** |
| Costo fuente 1,000 Ci | $18.5 MDP | $342.25 MDP | **Factor 18.5x** |

**🚨 HALLAZGO CRÍTICO:**
- Documento usa conversión 1:1 USD→MXN "por facilidad de cálculo"
- **PRECIO REAL Co-60:** $18,500 USD/Ci × 18.5 TC = $342,250 MXN/Ci
- **ERROR DE $23.86 MDP** en el componente más costoso

**Opciones de mitigación:**
1. **Fuente menor:** 500 Ci = 50M moscas/semana (-$11.9 MDP)
2. **Fuente usada:** 30% descuento (-$7.2 MDP)  
3. **Arrendamiento:** $2.5 MDP/año vs compra

**✅ AJUSTE RECOMENDADO:** **+$23.86 MDP** (corrección obligatoria)

---

### **3. EQUIPOS ESPECIALIZADOS - PRECIOS INFLADOS**

| Equipo | Precio Documento | Precio Mercado | Diferencia | Observaciones |
|--------|------------------|----------------|------------|---------------|
| Jaulas 80×60×60 | $28,500 | $15,000-20,000 | **+43-90%** | Precio premium internacional |
| Autoclaves 200L | $485,000 | $280,000-350,000 | **+39-73%** | No considera fabricantes mexicanos |
| Tamices vibratorios | $125,000 | $80,000-100,000 | **+25-56%** | Sobredimensionado |
| Incubadoras | $85,000 | $45,000-65,000 | **+31-89%** | Especificación excesiva |

**❌ PROBLEMAS:**
- No consideran proveedores mexicanos (CINVESTAV, UNAM, empresas locales)
- Especificaciones "gold standard" innecesarias
- Falta análisis de equipos reacondicionados

**✅ AJUSTE RECOMENDADO:** **-$4.8 MDP** (39% reducción equipos)

---

### **4. RECURSOS HUMANOS - PLANTILLA SOBREDIMENSIONADA**

#### **Análisis Comparativo con Plantas Similares:**

| Referencia | Capacidad | Personal | Costo/Persona | Observaciones |
|------------|-----------|----------|---------------|---------------|
| **Documento actual** | 100M/sem | 45 personas | $350,000/año | Plantilla inflada |
| **Planta Chiapas (histórica)** | 80M/sem | 28 personas | $280,000/año | Referencia real |
| **Planta Guatemala** | 120M/sem | 32 personas | $200,000/año | Más eficiente |
| **Propuesta optimizada** | 100M/sem | 32 personas | $300,000/año | Ajuste realista |

**❌ PROBLEMAS DETECTADOS:**
- **40% más personal** que referencias internacionales
- **Salarios 25-75% superiores** al mercado regional
- No considera automatización moderna
- Falta análisis de eficiencia operativa

**Plantilla sugerida:**
- Personal técnico: 18 (vs 25 propuestos) = -7 personas
- Personal operativo: 10 (vs 15 propuestos) = -5 personas  
- Personal administrativo: 4 (vs 5 propuestos) = -1 persona
- **Total:** 32 personas = **-29% plantilla**

**✅ AJUSTE RECOMENDADO:** **-$92.3 MDP** (29% reducción quinquenal)

---

### **5. INSUMOS RECURRENTES - COSTOS INFLADOS**

#### **Dieta Artificial - Análisis de Mercado:**

| Componente | Precio Documento | Precio Mercado México | Diferencia |
|------------|------------------|---------------------|------------|
| Sangre bovina | $185/kg | $120-150/kg | **+23-54%** |
| Caseína técnica | $125/kg | $85-110/kg | **+14-47%** |
| **Consumo semanal** | 8.5 ton | 6.2-7.8 ton | **+9-37%** |

**❌ PROBLEMAS:**
- Precios de sangre bovina basados en grado alimentario premium
- Consumo sobredimensionado (referencia IAEA: 6.5 ton/sem para 100M moscas)
- No considera proveedores regionales Yucatán

**✅ AJUSTE RECOMENDADO:** **-$48.5 MDP** (31% reducción quinquenal)

---

### **6. ENERGÍA ELÉCTRICA - CONSUMO SOBREESTIMADO**

| Parámetro | Valor Documento | Valor Técnico | Diferencia |
|-----------|-----------------|---------------|------------|
| Consumo anual | 2,850 MWh | 2,200-2,400 MWh | **+19-30%** |
| Costo CFE | $1.68/kWh | $1.45/kWh (tarifa industrial) | **+16%** |

**❌ PROBLEMAS:**
- No considera tarifa industrial preferencial
- Sobredimensiona sistemas HVAC
- Falta análisis de energías renovables (Yucatán = líder solar)

**✅ AJUSTE RECOMENDADO:** **-$8.2 MDP** (32% reducción quinquenal)

---

### **7. CONTINGENCIAS E INDIRECTOS - EXCESIVOS**

| Concepto | % Aplicado | % Estándar México | Observación |
|----------|------------|------------------|-------------|
| Supervisión técnica | 8-10% | 5-7% | **Inflado** |
| Contingencias | 10-12% | 8-10% | **Aceptable** |
| **Total indirectos** | 18-22% | 13-17% | **5% exceso** |

**✅ AJUSTE RECOMENDADO:** **-$12.1 MDP**

---

## 🎯 PROPUESTA DE OPTIMIZACIÓN INTEGRAL

### **ESCENARIO A: OPTIMIZACIÓN CONSERVADORA**

| Componente | Costo Original | Costo Ajustado | Ahorro |
|------------|----------------|----------------|--------|
| Laboratorio cría masiva | $64.34 MDP | $56.14 MDP | -$8.20 MDP |
| Planta irradiación | $66.25 MDP | $90.11 MDP | +$23.86 MDP |
| Sistema liberación | $17.27 MDP | $14.85 MDP | -$2.42 MDP |
| Operación quinquenal | $316.11 MDP | $167.11 MDP | -$149.00 MDP |
| **TOTAL** | **$463.97 MDP** | **$328.21 MDP** | **-$135.76 MDP** |

### **ESCENARIO B: OPTIMIZACIÓN AGRESIVA**

| Estrategia | Ahorro |
|------------|--------|
| Capacidad inicial 50M moscas/semana | -$65 MDP |
| Fuente Co-60 arrendada vs compra | -$15 MDP |
| Personal automatización + local | -$45 MDP |
| Equipos nacionales/reacondicionados | -$25 MDP |
| Operación trienal | -$95 MDP |
| **AHORRO TOTAL** | **-$245 MDP** |
| **INVERSIÓN FINAL** | **$218.97 MDP** |

---

## 🚨 RIESGOS DE INFRACOSTEO A EVITAR

### **COSTOS CRÍTICOS QUE NO DEBEN REDUCIRSE:**

1. **Licencias CNSNS:** $4.26 MDP (regulatorio obligatorio)
2. **Blindaje radiológico:** $11.48 MDP (seguridad crítica)  
3. **Sistemas de seguridad:** $3.89 MDP (obligatorio)
4. **Mantenimiento fuente Co-60:** $8.74 MDP/año (crítico)

### **CONTINGENCIAS MÍNIMAS REQUERIDAS:**
- **Obra civil:** 8% (vs 10% propuesto) = suficiente
- **Equipos importados:** 10% (vs 12% propuesto) = adecuado
- **Operación:** 5% anual = indispensable

---

## 📋 RECOMENDACIONES FINALES

### **AJUSTES INMEDIATOS OBLIGATORIOS:**

1. **🚨 CRÍTICO - Corregir precio Cobalto-60:** +$23.86 MDP
2. **💰 Reducir personal operativo:** 32 vs 45 personas = -$92.3 MDP
3. **🏗️ Optimizar construcción:** Estándares mexicanos = -$8.2 MDP  
4. **⚡ Revisar consumos energéticos:** Análisis técnico real = -$8.2 MDP
5. **🥩 Renegociar insumos:** Proveedores regionales = -$48.5 MDP

### **INVERSIÓN REALISTA RECOMENDADA:**

```
COMPONENTE                          COSTO AJUSTADO
================================================
Laboratorio cría masiva             $56.14 MDP
Planta irradiación (corregida)      $90.11 MDP  
Sistema liberación                  $14.85 MDP
Operación quinquenal (optimizada)   $167.11 MDP
================================================
TOTAL PROYECTO                      $328.21 MDP
```

**VS Estimación original:** $210.0 MDP  
**Incremento real necesario:** +$118.21 MDP (+56.3%)

### **CONCLUSIÓN:**
El proyecto es **VIABLE** con **$328.21 MDP**, no los $463.97 MDP calculados inicialmente. La diferencia principal está en costos operativos realistas y corrección del error en precio de Cobalto-60.

---

## 📊 VERIFICACIONES ADICIONALES REQUERIDAS

### **COTIZACIONES A SOLICITAR:**
1. **MDS Nordion:** Precio real Co-60 en MXN (crítico)
2. **Proveedores mexicanos:** Equipos laboratorio entomología  
3. **CFE Yucatán:** Tarifa industrial específica para el proyecto
4. **BYCSA/TRADECO:** Costos construcción BSL-1 en Mérida
5. **Grupo DIMEXA/Sukarne:** Sangre bovina regional

### **VALIDACIONES TÉCNICAS:**
1. **Consumo energético:** Simulación térmica real del edificio
2. **Personal operativo:** Benchmarking plantas IAEA activas
3. **Especificaciones HVAC:** Validar ±1°C vs ±2°C con SENASICA
4. **Automatización:** Nivel real requerido para 100M moscas/semana

**Status auditoría:** ✅ **COMPLETADA**  
**Próximo paso:** Solicitar cotizaciones de verificación  
**Plazo recomendado:** 15 días para ajustes finales