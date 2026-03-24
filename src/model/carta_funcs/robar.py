def robar(baraja):
    """Devuelve la última carta del mazo (o None si está vacío)."""
    if not baraja.cartas:
        return None
    return baraja.cartas.pop()