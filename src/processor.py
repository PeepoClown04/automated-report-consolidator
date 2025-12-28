import pandas as pd
import os
import glob

class ReportConsolidator:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
    
    def consolidate_files(self):
        print(f"📂 Buscando archivos Excel en: {self.input_folder}...")
        
        # 1. Encontrar todos los .xlsx
        # glob es genial para esto: busca patrones *.xlsx
        files = glob.glob(os.path.join(self.input_folder, "*.xlsx"))
        
        if not files:
            print("❌ No se encontraron archivos Excel.")
            return None
        
        print(f"found {len(files)} archivos. Iniciando fusión...")
        
        all_data = []
        
        for file in files:
            try:
                # Leemos el Excel
                df = pd.read_excel(file)
                
                # TRUCO PRO: Agregamos una columna con el nombre del archivo
                # para saber de qué sucursal vino cada venta.
                filename = os.path.basename(file)
                df["Origen_Archivo"] = filename
                
                all_data.append(df)
                print(f"   ✅ Leído: {filename} ({len(df)} filas)")
            except Exception as e:
                print(f"   ⚠️ Error leyendo {file}: {e}")
        
        # 2. Fusión (Concatenar)
        if all_data:
            master_df = pd.concat(all_data, ignore_index=True)
            print("-" * 30)
            print(f"🚀 FUSIÓN COMPLETA: {len(master_df)} filas totales procesadas.")
            return master_df
        else:
            return None

    def generate_summary(self, df):
        # Generamos un pequeño reporte de resumen (KPIs)
        print("📊 Calculando métricas de negocio...")
        
        # Agrupamos por 'Origen_Archivo' (Sucursal) y sumamos 'Total_Venta'
        kpi_sucursal = df.groupby("Origen_Archivo")["Total_Venta"].sum().reset_index()
        
        # Formateamos para que se vea bonito (opcional)
        kpi_sucursal["Total_Venta"] = kpi_sucursal["Total_Venta"].apply(lambda x: f"${x:,.0f}")
        
        return kpi_sucursal