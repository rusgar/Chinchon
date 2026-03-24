def sumar_puntos_ronda(jugador, puntos):
    jugador.puntos_ronda = puntos
    jugador.puntos += puntos
    if jugador.puntos >= 100:
        jugador.eliminado = True