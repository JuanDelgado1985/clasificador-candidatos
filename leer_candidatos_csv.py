import csv

def leer_candidatos_csv(nombre_archivo):
    candidatos = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fila["nota"] = int(fila["nota"])  # Convertir la nota a entero
            fila["anios_experiencia"] = int(fila["anios_experiencia"])  # Convertir los años de experiencia a entero
            if fila["disponible"] == "True":
                fila["disponible"] = True
            else:
                fila["disponible"] = False
            
            candidatos.append(fila)
    return candidatos
