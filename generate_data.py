import pandas as pd
import numpy as np
import os
import random

# Crear carpeta de entrada si no existe
os.makedirs("input", exist_ok=True)

SUCURSALES = ["Santiago_Centro", "Providencia", "Las_Condes", "Vina_del_Mar", "Concepcion"]
PRODUCTOS = ["Laptop", "Mouse", "Teclado", "Monitor", "HDMI Cable"]

def generar_excel_falso(sucursal):
    # Generamos entre 10 y 50 ventas aleatorias
    num_ventas = random.randint(10, 50)
    
    data = {
        "Fecha": pd.date_range(start="2025-01-01", periods=num_ventas),
        "Producto": [random.choice(PRODUCTOS) for _ in range(num_ventas)],
        "Cantidad": [random.randint(1, 10) for _ in range(num_ventas)],
        "Precio_Unitario": [random.randint(5000, 1500000) for _ in range(num_ventas)],
        "Vendedor": [f"Vendedor_{random.randint(1, 5)}" for _ in range(num_ventas)]
    }
    
    df = pd.DataFrame(data)
    
    # Calculamos Total (que a veces viene, a veces no, para simular realidad)
    df["Total_Venta"] = df["Cantidad"] * df["Precio_Unitario"]
    
    # Guardamos el archivo con nombre típico corporativo
    filename = f"input/Reporte_Ventas_{sucursal}_2025.xlsx"
    df.to_excel(filename, index=False)
    print(f"✅ Generado: {filename}")

if __name__ == "__main__":
    print("🏭 Generando datos de prueba...")
    for suc in SUCURSALES:
        generar_excel_falso(suc)
    print("✨ ¡Listo! Revisa la carpeta 'input/'.")