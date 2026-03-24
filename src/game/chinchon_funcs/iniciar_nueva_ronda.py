from model.carta import Baraja


def iniciar_nueva_ronda(game):
    game.baraja = Baraja()
    game.descarte = []

    manos = game.baraja.repartir(len(game.jugadores), 7)
    for jugador, mano in zip(game.jugadores, manos):
        jugador.recibir_cartas(mano)
        jugador.puntos_ronda = 0

    primera = game.baraja.robar()
    if primera:
        game.descarte.append(primera)

    if game.turno_actual >= len(game.jugadores):
        game.turno_actual = 0
