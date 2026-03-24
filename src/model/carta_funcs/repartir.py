def repartir(baraja, n_jugadores, cartas_por_jugador=7):
    """
    Reparte cartas a los jugadores.
    Devuelve una lista de manos: [mano_j1, mano_j2, ...]
    """
    from model.carta_funcs.robar import robar
    manos = []
    for _ in range(n_jugadores):
        mano = [robar(baraja) for _ in range(cartas_por_jugador)]
        manos.append(mano)
    return manos