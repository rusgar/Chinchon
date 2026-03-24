def procesar_eliminaciones_y_ganador(juego, limpiar, escribir, colores):
    jugadores_antes = juego.jugadores.copy()

    eliminados = []
    for j in juego.jugadores:
        if j.puntos >= 100 and not j.eliminado:
            j.eliminado = True
            eliminados.append(j)

    if eliminados:
        escribir("\n=== JUGADORES ELIMINADOS ===", colores["rojo"])
        for e in eliminados:
            escribir(f"{e.nombre} ha sido eliminado con {e.puntos} puntos.", colores["rojo"])

    juego.jugadores = [j for j in juego.jugadores if not j.eliminado]

    if len(juego.jugadores) == 0:
        ganador = min(jugadores_antes, key=lambda x: x.puntos)
        ganador.eliminado = False
        juego.jugadores = [ganador]
        escribir("\n⚠️ TODOS LOS JUGADORES SUPERARON 100 PUNTOS", colores["amarillo"])
        escribir(f"🏆 GANADOR POR MENOR PUNTUACIÓN: {ganador.nombre}", colores["verde"])
        return "fin"

    if juego.turno_actual >= len(juego.jugadores):
        juego.turno_actual = 0

    if len(juego.jugadores) == 1:
        ganador = juego.jugadores[0]
        escribir(f"\n🏆 GANADOR DE LA PARTIDA: {ganador.nombre}", colores["verde"])
        return "fin"

    input("\nPulsa ENTER para continuar...")
    return "cerrado"
