"""
Este módulo se encarga de leer un archivo CSV con información de movimientos
y enviar los datos procesados a la función start del módulo cli.start.
"""

import csv
import cli.start as start

# Abrir el archivo CSV en modo lectura
# newline="" evita líneas en blanco adicionales
# encoding="utf-8" permite leer caracteres especiales
with open("data/archivo.csv", newline="", encoding="utf-8") as f:
    
    # Crear el lector CSV
    reader = csv.reader(f)
    
    # Saltar la primera fila (cabecera del archivo)
    next(reader)
    
    # Recorrer cada fila del archivo
    for fila in reader:
        
        # Desempaquetar los valores de la fila
        fecha, descripcion, cargo, detalle = fila
        
        # Extraer día y mes desde la fecha (formato esperado: YYYY-MM-DD)
        dia = fecha.split("-")[2]
        mes = fecha.split("-")[1]
        
        # Convertir el cargo a tipo float
        total = float(cargo)
        
        # Enviar los datos procesados a la función start
        start.start(dia, mes, total, detalle)
