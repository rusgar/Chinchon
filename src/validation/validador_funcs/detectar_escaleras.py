def detectar_escaleras(cartas):
    """
    Detecta escaleras válidas en una lista de cartas.
    Una escalera es:
        - 3 o más cartas
        - mismo palo
        - valores consecutivos
    Los comodines se ignoran en esta validación básica.
    """
    from validation.validador_funcs.filtrar_normales import filtrar_normales

    cartas_normales = filtrar_normales(cartas)

    # Agrupar por palo
    palos = {}
    for carta in cartas_normales:
        palos.setdefault(carta.palo, []).append(carta)

    escaleras = []

    for palo, grupo in palos.items():
        grupo_ordenado = sorted(grupo, key=lambda c: c.valor)
        secuencia = [grupo_ordenado[0]]

        for i in range(1, len(grupo_ordenado)):
            actual = grupo_ordenado[i]
            anterior = grupo_ordenado[i - 1]

            if actual.valor == anterior.valor + 1:
                secuencia.append(actual)
            else:
                if len(secuencia) >= 3:
                    escaleras.append(secuencia)
                secuencia = [actual]

        if len(secuencia) >= 3:
            escaleras.append(secuencia)

    return escaleras