def jugar_turno(game):
    """Ejecuta un turno completo del jugador actual."""
    # Si no quedan jugadores, terminar
    if len(game.jugadores) == 0:
        return "fin"

    # Asegurar que turno_actual sea válido
    if game.turno_actual >= len(game.jugadores):
        game.turno_actual = 0

    jugador = game.jugadores[game.turno_actual]

    # Si el jugador está eliminado → saltar turno
    if jugador.eliminado:
        game._avanzar_turno()
        return "continuar"

    # 1. ROBAR
    carta_robada = game._robar_carta(jugador)

    # 2. PROCESAR COMODÍN (si corresponde)
    if carta_robada.tipo == "comodin":
        resultado = game._procesar_comodin(jugador, carta_robada)
        # Si el jugador fue eliminado por el comodín, terminar turno sin avanzar (ya se ajustó en _procesar_comodin)
        if jugador.eliminado:
            return resultado if resultado in ["fin", "ganador"] else "continuar"
        # Si el juego terminó, devolver resultado
        if resultado in ["fin", "ganador"]:
            return resultado
        # Si el jugador sobrevivió y el juego continúa, seguir con el turno normal

    # 3. AVISAR SOBRE LA MANO
    game._avisar_mano_valida(jugador)

    # 4. PREGUNTAR CIERRE
    if game._preguntar_cierre(jugador):
        return game._cerrar_ronda(jugador)

    # 5. DESCARTAR
    game._procesar_descarte(jugador)

    # 6. AVANZAR TURNO (solo si el jugador no fue eliminado durante su turno)
    if not jugador.eliminado:
        game._avanzar_turno()
    return "continuar"