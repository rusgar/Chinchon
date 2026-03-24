from effects.comodines import activar_comodin


def procesar_comodin(game, jugador, carta):
    activar_comodin(jugador, carta, game.limpiar, game.escribir, game.colores)

    indice_actual = game.turno_actual
    game.jugadores = [j for j in game.jugadores if not j.eliminado]

    if len(game.jugadores) == 0:
        return "fin"

    if jugador.eliminado:
        if indice_actual >= len(game.jugadores):
            game.turno_actual = 0
    else:
        if game.turno_actual >= len(game.jugadores):
            game.turno_actual = 0

    if len(game.jugadores) == 1:
        return "ganador"

    return "continuar"
