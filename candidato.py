class Candidato:
    def __init__(self, nombre, nota, disponible, anios_experiencia):
        self.nombre = nombre
        self.nota = nota
        self.disponible = disponible
        self.anios_experiencia = anios_experiencia

    def clasificar(self):
        if self.nota >= 80:
            if self.disponible:
                return "Recomendado"
            else:
                return "No disponible"
        elif self.nota >= 50:
            return "A revisar"
        else:
            return "No recomendado"




# joaquin = Candidato("Joaquín", 85, True, 3)
#lou = Candidato("Lou", 90, False, 4)

#print(joaquin.clasificar())
#print(lou.clasificar())