# Automated Report Consolidator ![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

Script de automatización administrativa para procesar, limpiar y unificar múltiples fuentes de datos (Excel/CSV/PDF) en un reporte maestro coherente. Diseñado para reducir el tiempo de procesamiento de datos manual en entornos corporativos.

## Solución
Transforma una tarea manual de horas en un proceso de segundos. Itera sobre una carpeta de entrada, normaliza los datos de archivos dispares y genera un archivo `Master_Report.xlsx` con métricas consolidadas.

## Características Técnicas
- **Ingesta Masiva:** Soporte para iteración automática sobre directorios (`os`, `glob`).
- **Data Cleaning:** Normalización de formatos de fecha y limpieza de valores nulos con Pandas.
- **Excel Automation:** Formateo condicional y generación de fórmulas automáticas usando OpenPyXL.

## Stack Tecnológico
- Python 3.x
- Pandas
- OpenPyXL
- OS/Glob

## Ejecución
Colocar archivos raw en la carpeta `/input` y ejecutar `python main.py`. El reporte se generará en `/output`.
