def calcular_y_mostrar_puntuaciones(game):
    game.escribir("\nPuntuaciones de la ronda:", game.colores["verde"])

    for jugador in game.jugadores:
        if jugador.eliminado:
            continue

        puntos = game._calcular_puntos_jugador(jugador)
        jugador.sumar_puntos_ronda(puntos)

        game.escribir(
            f"{jugador.nombre}: +{jugador.puntos_ronda} puntos (Total: {jugador.puntos})",
            game.colores["reset"]
        )
