def mostrar_resumen_ronda(game, jugador_cierra):
    game.escribir("=== RESUMEN DE LA RONDA ===", game.colores["cian"])
    game.escribir(f"Jugador que cierra: {jugador_cierra.nombre}\n", game.colores["amarillo"])
    game.escribir("Cartas de cada jugador:\n", game.colores["verde"])
    for j in game.jugadores:
        mano_str = ", ".join(game._formatear_carta(c) for c in j.mano)
        game.escribir(f"{j.nombre}: {mano_str}", game.colores["reset"])
