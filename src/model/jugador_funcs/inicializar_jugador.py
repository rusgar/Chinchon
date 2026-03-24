def inicializar_jugador(jugador, nombre):
    jugador.nombre = nombre
    jugador.mano = []
    jugador.puntos = 0
    jugador.eliminado = False
    jugador.puntos_ronda = 0
    jugador.uso_comodin = {1: False, 2: False, 3: False, 4: False}