def avanzar_turno(game):
    game.turno_actual = (game.turno_actual + 1) % len(game.jugadores)
