def elegir_descartar(game, jugador):
    game.escribir("\nElige qué carta descartar:", game.colores["amarillo"])

    for i, carta in enumerate(jugador.mano):
        game.escribir(f"{i+1}. {game._formatear_carta(carta)}")

    while True:
        eleccion = input("Número de carta a descartar: ").strip()

        if eleccion.isdigit():
            idx = int(eleccion) - 1
            if 0 <= idx < len(jugador.mano):
                carta = jugador.mano[idx]
                jugador.descartar(carta)
                return carta

        game.escribir("Opción inválida.", game.colores["rojo"])
