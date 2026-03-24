def preguntar_cierre(game, jugador):
    game.escribir(f"{jugador.nombre}, ¿quieres cerrar la ronda?", game.colores["amarillo"])
    opcion = input("Escribe S para cerrar, o ENTER para seguir: ").strip().lower()
    return opcion == "s"
