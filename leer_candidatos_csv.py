import csv

def leer_candidatos_csv(nombre_archivo):
    candidatos = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    fila["nota"] = int(fila["nota"])
                    fila["anios_experiencia"] = int(fila["anios_experiencia"]) 
                    fila["disponible"] = fila["disponible"].lower() == "true"
                except ValueError:
                    print(f"Fila con error o datos invalidos, se omite registro : {fila}")
                    continue
                candidatos.append(fila)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no fue encontrado.")

    return candidatos
