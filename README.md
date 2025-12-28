# Automated Report Consolidator 
![Status](https://img.shields.io/badge/Status-Completed-green)

Script de automatización administrativa para procesar, limpiar y unificar múltiples fuentes de datos (Excel/CSV) en un reporte maestro coherente. Diseñado para reducir el tiempo de procesamiento de datos manual en entornos corporativos.

## Solución
Transforma una tarea manual de horas en un proceso de segundos. Itera sobre una carpeta de entrada con múltiples reportes de sucursales, normaliza los datos y genera un archivo `Master_Report.xlsx` con dos pestañas: detalle completo y resumen de métricas (KPIs).

## Características Técnicas
- **Ingesta Masiva:** Soporte para iteración automática sobre directorios (`glob`).
- **Data Cleaning:** Identificación del origen de datos y unificación de formatos con `Pandas`.
- **Excel Automation:** Generación de reportes multicapa (Hojas de Detalle + Resumen) usando `XlsxWriter`.

## Stack Tecnológico
- Python 3.x
- Pandas
- XlsxWriter / OpenPyXL
- OS/Glob

## Ejecución
1. Generar datos de prueba (opcional): `python generate_data.py`
2. Asegurar que los archivos estén en la carpeta `/input`.
3. Ejecutar el consolidador: `python main.py`.
4. El reporte final aparecerá en la carpeta `/output`.