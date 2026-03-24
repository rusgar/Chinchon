def crear_baraja(baraja):
    """Genera las 40 cartas normales y los 4 comodines especiales."""
    from model.carta import Carta
    baraja.cartas = []

    # 40 cartas normales
    for palo in baraja.PALOS:
        for valor in baraja.VALORES:
            baraja.cartas.append(Carta(palo, valor, tipo="normal"))

    # 4 comodines numerados 1–4
    for numero in range(1, 5):
        baraja.cartas.append(Carta(None, numero, tipo="comodin"))