def es_chinchon(cartas):
    """
    Determina si las 7 cartas forman un Chinchón completo.
    Los comodines NO se usan aquí (versión básica).
    """
    from validation.validador_funcs.detectar_escaleras import detectar_escaleras

    if len(cartas) != 7:
        return False

    # Escalera de 7 cartas
    escaleras = detectar_escaleras(cartas)
    for escalera in escaleras:
        if len(escalera) == 7:
            return True

    # Grupo de 7 (teóricamente imposible en baraja española)
    return False