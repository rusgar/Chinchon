def fijar_puntos(jugador, valor):
    jugador.puntos = valor
    if jugador.puntos >= 100:
        jugador.eliminado = True