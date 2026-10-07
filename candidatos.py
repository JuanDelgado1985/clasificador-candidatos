from leer_candidatos_csv import leer_candidatos_csv
from candidato import Candidato


candidatos = leer_candidatos_csv("candidatos.csv")



def clasificador_candidatos(candidatos):
    count_recomendados = 0
    count_no_recomendados = 0
    count_a_revisar = 0
    count_no_disponible = 0
    recomendados_disponibles = []

    for candidato in candidatos:
        resultado = candidato.clasificar()
        if resultado == "Recomendado":
            count_recomendados += 1
            recomendados_disponibles.append(candidato) 
        elif resultado == "No disponible":
            count_no_disponible += 1
        elif resultado == "A revisar":
            count_a_revisar += 1
        else:
            count_no_recomendados += 1  

    print(recomendados_disponibles)
    print(f"""cantidad de recomendados = {count_recomendados}, 
    cantidad de no recomendados = {count_no_recomendados}, 
    cantidad de candidatos a revisar = {count_a_revisar}""")
    print(f"""Cantidad de candidatos que tienen una buena nota pero no están disponibles {count_no_disponible}""")

clasificador_candidatos(candidatos)

    #for candidato in candidatos:
    #   if candidato["nota"] >= 80:
    #       if candidato["disponible"]:
    #          count_recomendados = count_recomendados + 1
    #            recomendados_disponibles.append(candidato)
    #        else:
    #            count_no_disponible = count_no_disponible + 1
    #    elif candidato["nota"] >= 50:
    #        count_a_revisar = count_a_revisar + 1
    #    else:
    #        count_no_recomendados = count_no_recomendados + 1

    ###return recomendados_disponibles, count_recomendados, count_no_recomendados, count_a_revisar, count_no_disponible





#recomendados_disponibles, count_recomendados, count_no_recomendados, count_a_revisar, count_no_disponible = clasificador_candidatos(candidatos)

