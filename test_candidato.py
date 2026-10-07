from candidato import Candidato

def test_clasificar_recomendado():
    candidato = Candidato("Ana", 85, True, 3)
    assert candidato.clasificar() == "Recomendado"

def test_clasificar_recomendado_no_disponible():
    candidato = Candidato("Lou", 90, False, 4)
    assert candidato.clasificar() == "No disponible"

def test_clasificar_a_revisar():
    candidato = Candidato("Juan", 70, True, 4)
    assert candidato.clasificar() == "A revisar"

def test_clasificar_no_recomendado():
    candidato = Candidato("Luis", 45, True, 2)
    assert candidato.clasificar() == "No recomendado"

def test_clasificar_limite_80():
    candidato = Candidato("Carlos", 80, True, 5)
    assert candidato.clasificar() == "Recomendado"

def test_clasificar_limite_50():
    candidato = Candidato("Marta", 50, True, 1)
    assert candidato.clasificar() == "A revisar"