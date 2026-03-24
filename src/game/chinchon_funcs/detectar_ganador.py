def detectar_ganador(game):
    activos = [j for j in game.jugadores if not j.eliminado]

    if len(activos) == 1:
        return activos[0]

    return None