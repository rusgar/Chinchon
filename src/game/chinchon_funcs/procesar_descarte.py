def procesar_descarte(game, jugador):
    carta_descartada = game._elegir_descartar(jugador)
    if carta_descartada.tipo != "comodin":
        game.descarte.append(carta_descartada)
