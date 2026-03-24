def formatear_carta(carta):
    if carta.tipo == "comodin":
        nombres_legibles = {
            "estrella_galicia": "🍺 Estrella Galicia",
            "alhambra_verde": "🍀 Alhambra Verde",
            "estrella_1906": "⭐ Estrella 1906",
            "sin_cerveza": "☠️ SIN CERVEZA"
        }
        return nombres_legibles.get(carta.nombre, "🃏 JOKER")

    if carta.valor == 10:
        letra = "S"
    elif carta.valor == 11:
        letra = "C"
    elif carta.valor == 12:
        letra = "R"
    else:
        letra = str(carta.valor)

    emojis = {
        "oros": "🪙",
        "copas": "🍷",
        "espadas": "⚔️",
        "bastos": "🪵"
    }

    emoji = emojis.get(carta.palo, "?")
    return f"{letra} {emoji}"
