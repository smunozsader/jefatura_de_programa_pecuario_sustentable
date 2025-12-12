#!/usr/bin/env python3
"""
Script para extraer municipios de Yucatán del archivo INEGI Excel
con codificación UTF-8 correcta
"""

import pandas as pd
import sys

def extraer_municipios_yucatan():
    print("=== EXTRACCIÓN MUNICIPIOS YUCATÁN - INEGI ===")
    
    try:
        # Leer archivo Excel
        archivo_excel = r"H:\My Drive\2025. 1.0 JEFATURA PROGRAMA\marco_geoestadistico_inegi\AGEEML_2025102162256_UTF.xlsx"
        print(f"Leyendo archivo: {archivo_excel}")
        
        # Probar diferentes hojas
        try:
            df = pd.read_excel(archivo_excel, sheet_name=0)  # Primera hoja
        except:
            try:
                df = pd.read_excel(archivo_excel)
            except Exception as e:
                print(f"Error leyendo Excel: {e}")
                return
        
        print(f"Columnas disponibles: {list(df.columns)}")
        print(f"Total registros: {len(df)}")
        
        # Buscar municipios de Yucatán (clave entidad 31)
        if 'CVE_ENT' in df.columns:
            yucatan = df[df['CVE_ENT'] == '31']
        elif 'Clave de Entidad' in df.columns:
            yucatan = df[df['Clave de Entidad'] == '31']
        else:
            # Buscar por texto Yucatán
            for col in df.columns:
                if df[col].astype(str).str.contains('Yucatán', na=False).any():
                    print(f"Encontrada referencia a Yucatán en columna: {col}")
                    yucatan = df[df[col].astype(str).str.contains('Yucatán', na=False)]
                    break
            else:
                print("No se encontró Yucatán. Mostrando primeras 10 filas:")
                print(df.head(10))
                return
        
        if len(yucatan) > 0:
            print(f"\n=== MUNICIPIOS DE YUCATÁN ENCONTRADOS ({len(yucatan)}) ===")
            
            # Mostrar municipios
            for idx, row in yucatan.iterrows():
                print(f"Fila {idx}: {dict(row)}")
                
        else:
            print("No se encontraron municipios de Yucatán")
            print("Mostrando muestra de datos:")
            print(df.head())
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    extraer_municipios_yucatan()