def preguntar_cierre(game, jugador):
    while True:
        game.escribir(f"{jugador.nombre}, ¿quieres cerrar la ronda?", game.colores["amarillo"])
        opcion = input("Escribe S para cerrar, o ENTER para seguir: ").strip().lower()
        if opcion == "" or opcion == "s":
            return opcion == "s"
        game.escribir("Opción inválida. Solo ENTER o S están permitidos.", game.colores["rojo"])
