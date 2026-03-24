def aplicar_penalizacion_comodines_no_usados(game, ganador):
    """
    Aplica penalización de -5 puntos por cada comodín no usado en la mano del ganador.
    """
    comodines_no_usados = sum(1 for c in ganador.mano if c.tipo == "comodin")

    if comodines_no_usados > 0:
        penalizacion = comodines_no_usados * 5
        game.escribir(f"\nPenalización por comodines no usados: -{penalizacion} puntos", game.colores["rojo"])
        ganador.restar_puntos(penalizacion)
        game.escribir(f"Puntuación final de {ganador.nombre}: {ganador.puntos} puntos", game.colores["verde"])