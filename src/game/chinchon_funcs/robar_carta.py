def robar_carta(game, jugador):
    game.escribir("\nOpciones de robo:", game.colores["amarillo"])
    game.escribir("1. Robar del mazo (boca abajo)")
    game.escribir("2. Robar del descarte (boca arriba)")

    if len(game.descarte) > 0:
        carta_superior = game.descarte[-1]
        game.escribir(f"Carta visible: {game._formatear_carta(carta_superior)}", game.colores["cian"])
    else:
        game.escribir("No hay cartas en el descarte.", game.colores["rojo"])

    while True:
        eleccion = input("Elige opción (1 o 2): ").strip()

        if eleccion == "1":
            carta = game.baraja.robar()
            if carta is None:
                game.escribir("El mazo está vacío.", game.colores["rojo"])
                continue

            jugador.robar_carta(carta)
            game.escribir(f"Has robado del mazo: {game._formatear_carta(carta)}", game.colores["verde"])
            return carta

        elif eleccion == "2":
            if len(game.descarte) == 0:
                game.escribir("No hay carta en el descarte.", game.colores["rojo"])
                continue

            carta = game.descarte.pop()
            jugador.robar_carta(carta)
            game.escribir(f"Has robado del descarte: {game._formatear_carta(carta)}", game.colores["verde"])
            return carta

        else:
            game.escribir("Opción inválida.", game.colores["rojo"])
