from game.chinchon_funcs.mano_valida import mano_valida


def avisar_mano_valida(game, jugador):
    if mano_valida(jugador.mano):
        game.escribir("Tu mano es válida.", game.colores["verde"])
    else:
        game.escribir("Tu mano NO es válida.", game.colores["rojo"])
