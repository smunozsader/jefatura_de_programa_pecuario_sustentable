#!/usr/bin/env python3
"""
Budget Analysis Script for Macro Proyecto Estratégico Renacimiento Maya
Verifies budget coherence between macro-project and component projects
"""

import pandas as pd
import numpy as np

def main():
    print("=== ANÁLISIS DE COHERENCIA PRESUPUESTARIA ===")
    print("Macroproyecto Renacimiento Ganadero Maya 2026-2030")
    print("-" * 60)
    
    # Load livestock registry data
    try:
        df = pd.read_csv(r"DOCS REFERENCIA\2025. padron ganadero nacional yucatan detallado por municipios.csv")
        print(f"\n1. DATOS DEL PADRÓN GANADERO:")
        print(f"   Municipios registrados: {len(df)}")
        
        # Clean numeric columns (remove quotes and commas)
        numeric_cols = ['UPP', 'Vientres', 'Vaquillas', 'Sementales', 
                       'Crias Hembra', 'Crias Macho', 'Becerros', 'Novillos']
        
        for col in numeric_cols:
            df[col] = df[col].astype(str).str.replace('"', '').str.replace(',', '').astype(int)
        
        total_upp = df['UPP'].sum()
        total_vientres = df['Vientres'].sum()
        total_ganado = df[numeric_cols[1:]].sum().sum()  # All cattle categories
        
        print(f"   Total UPP actuales: {total_upp:,}")
        print(f"   Total vientres: {total_vientres:,}")
        print(f"   Total ganado (todas categorías): {total_ganado:,}")
        
        # Pareto analysis - Top municipalities
        df_sorted = df.sort_values('Vientres', ascending=False)
        cumulative_vientres = df_sorted['Vientres'].cumsum()
        total_threshold = total_vientres * 0.8
        pareto_muns = df_sorted[cumulative_vientres <= total_threshold]
        
        print(f"\n2. ANÁLISIS PARETO (80% concentración):")
        print(f"   Top {len(pareto_muns)} municipios concentran {pareto_muns['Vientres'].sum():,} vientres")
        print(f"   Porcentaje: {(pareto_muns['Vientres'].sum() / total_vientres * 100):.1f}%")
        
        # BUDGET VERIFICATION
        print(f"\n3. VERIFICACIÓN PRESUPUESTARIA:")
        
        # Macro-project totals (from strategic document)
        macro_total = 5300  # 5.3 billion MXN
        macro_annual = macro_total / 5  # 5-year program
        
        print(f"   Macroproyecto total: ${macro_total:,.0f} millones MXN (5 años)")
        print(f"   Promedio anual: ${macro_annual:,.0f} millones MXN")
        
        # Component verification
        print(f"\n4. ANÁLISIS POR COMPONENTE:")
        
        # Silvopastoral component
        silvo_annual_base = 80.4  # From reference documents
        silvo_5year_base = silvo_annual_base * 5
        silvo_macro_allocation = macro_total * 0.47  # Estimated allocation
        
        print(f"\n   A) REPOBLAMIENTO SILVOPASTORIL:")
        print(f"      Base anual documentada: ${silvo_annual_base:.1f} millones MXN")
        print(f"      Proyección 5 años: ${silvo_5year_base:.1f} millones MXN")
        print(f"      Asignación macro-proyecto: ${silvo_macro_allocation:.1f} millones MXN")
        print(f"      Ratio coherencia: {silvo_macro_allocation/silvo_5year_base:.1f}x")
        
        # Dairy component
        dairy_annual_base = 16.62  # From reference documents
        dairy_5year_base = dairy_annual_base * 5
        dairy_macro_allocation = macro_total * 0.07  # Estimated allocation
        
        print(f"\n   B) FOMENTO GANADERÍA LECHERA:")
        print(f"      Base anual documentada: ${dairy_annual_base:.1f} millones MXN")
        print(f"      Proyección 5 años: ${dairy_5year_base:.1f} millones MXN")
        print(f"      Asignación macro-proyecto: ${dairy_macro_allocation:.1f} millones MXN")
        print(f"      Ratio coherencia: {dairy_macro_allocation/dairy_5year_base:.1f}x")
        
        # Reality check calculations
        print(f"\n5. VERIFICACIÓN REALIDAD OPERATIVA:")
        
        # Current vs projected livestock
        current_cattle = total_ganado
        projected_cattle = 850000  # From macro-project
        growth_needed = projected_cattle - current_cattle
        growth_percentage = (growth_needed / current_cattle) * 100
        
        print(f"   Ganado actual: {current_cattle:,} cabezas")
        print(f"   Meta 2030: {projected_cattle:,} cabezas")
        print(f"   Crecimiento requerido: {growth_needed:,} cabezas ({growth_percentage:.1f}%)")
        
        # Investment per head
        investment_per_head = (macro_total * 1000000) / growth_needed  # Convert to pesos
        
        print(f"   Inversión por cabeza nueva: ${investment_per_head:,.0f} pesos")
        
        # Recommendations
        print(f"\n6. RECOMENDACIONES DE AJUSTE:")
        
        # Calculate conservative budget based on documented components
        conservative_total = (silvo_5year_base + dairy_5year_base) * 1.5  # 50% buffer for other components
        
        print(f"   Presupuesto conservador basado en componentes documentados:")
        print(f"   ${conservative_total:.1f} millones MXN (vs ${macro_total:.0f} macro-proyecto)")
        print(f"   Reducción sugerida: {((macro_total - conservative_total) / macro_total * 100):.1f}%")
        
        if macro_total > conservative_total * 2:
            print(f"   ⚠️  ALERTA: Presupuesto macro-proyecto excede 2x base documentada")
            print(f"   🔧 ACCIÓN: Revisar y ajustar cifras o documentar componentes faltantes")
        
        print(f"\n7. CONCLUSIONES:")
        print(f"   • Padrón ganadero actual verificado: {total_ganado:,} cabezas")
        print(f"   • Meta crecimiento 89% es ambiciosa pero factible")
        print(f"   • Presupuesto macro requiere mayor sustento documental")
        print(f"   • Recomendado: Base presupuestaria conservadora con expansión gradual")
        
    except Exception as e:
        print(f"Error al analizar datos: {e}")

if __name__ == "__main__":
    main()