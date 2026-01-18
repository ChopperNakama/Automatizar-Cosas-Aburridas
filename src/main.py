import csv
import cli.start as start

with open("data/archivo.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  
    
    for fila in reader:
        fecha, descripcion, cargo, detalle = fila
        dia, mes = fecha.split("-")[2], fecha.split("-")[1]
        total = float(cargo)
        start.start(dia,mes,total,detalle)

