import pandas as pd
import os
from src.processor import ReportConsolidator

def main():
    # Configuración de carpetas
    INPUT_DIR = "input"
    OUTPUT_DIR = "output"
    
    # Asegurar que existe output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 1. Instanciar y Consolidar
    consolidator = ReportConsolidator(INPUT_DIR, OUTPUT_DIR)
    master_df = consolidator.consolidate_files()
    
    if master_df is not None:
        # 2. Guardar el "Master Data" (Todos los datos crudos unidos)
        master_path = os.path.join(OUTPUT_DIR, "Master_Report_Completo.xlsx")
        
        # Usamos ExcelWriter para guardar dos hojas en el mismo Excel
        with pd.ExcelWriter(master_path, engine='xlsxwriter') as writer:
            
            # Hoja 1: Data Cruda (Detalle)
            master_df.to_excel(writer, sheet_name='Detalle_Ventas', index=False)
            
            # Hoja 2: Resumen Ejecutivo (KPIs)
            summary_df = consolidator.generate_summary(master_df)
            summary_df.to_excel(writer, sheet_name='Resumen_Por_Sucursal', index=False)
            
            print(f"\n💾 Reporte guardado en: {master_path}")
            print("   (Contiene dos pestañas: 'Detalle_Ventas' y 'Resumen_Por_Sucursal')")

if __name__ == "__main__":
    main()