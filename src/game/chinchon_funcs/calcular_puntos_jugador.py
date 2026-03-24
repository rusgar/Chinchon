def calcular_puntos_jugador(jugador):
    normales = [c for c in jugador.mano if c.tipo != "comodin"]

    if len(normales) == 7:
        palo = normales[0].palo
        valores = sorted(c.valor for c in normales)
        if all(valores[i] + 1 == valores[i+1] for i in range(6)) and all(c.palo == palo for c in normales):
            return -10

    return sum(c.valor for c in normales)
