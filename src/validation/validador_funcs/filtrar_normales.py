def filtrar_normales(cartas):
    """Devuelve solo las cartas normales (ignora comodines)."""
    return [c for c in cartas if c.tipo == "normal"]