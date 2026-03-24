from validation.validador import detectar_grupos, detectar_escaleras, _filtrar_normales


def mano_valida(cartas):
    """Determina si una mano de 7 cartas es válida para cerrar."""
    normales = _filtrar_normales(cartas)

    if len(normales) != 7:
        return False

    for i in range(7):
        resto = normales[:i] + normales[i+1:]
        grupos = detectar_grupos(resto)
        escaleras = detectar_escaleras(resto)
        total_cartas_usadas = sum(len(g) for g in grupos) + sum(len(e) for e in escaleras)

        if total_cartas_usadas == 6:
            return True

    return False
