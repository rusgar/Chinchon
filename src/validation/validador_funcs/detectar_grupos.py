def detectar_grupos(cartas):
    """
    Detecta grupos válidos en una lista de cartas.
    Un grupo es:
        - 3 o más cartas
        - mismo valor
        - palos distintos
    Los comodines se ignoran.
    """
    from validation.validador_funcs.filtrar_normales import filtrar_normales

    cartas_normales = filtrar_normales(cartas)

    valores = {}
    for carta in cartas_normales:
        valores.setdefault(carta.valor, []).append(carta)

    grupos = []

    for valor, grupo in valores.items():
        if len(grupo) >= 3:
            grupos.append(grupo)

    return grupos