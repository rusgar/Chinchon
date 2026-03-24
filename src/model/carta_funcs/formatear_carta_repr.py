def formatear_carta_repr(carta):
    if carta.tipo == "comodin":
        nombres = {
            1: "Estrella Galicia",
            2: "Alhambra Verde",
            3: "Estrella 1906",
            4: "SIN CERVEZA"
        }
        return f"<Comodín #{carta.valor}: {nombres.get(carta.valor, 'Desconocido')}>"
    return f"<Carta {carta.valor} de {carta.palo}>"