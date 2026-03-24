def asignar_nombre_comodin(carta):
    if carta.tipo == "comodin":
        nombres = {
            1: "estrella_galicia",
            2: "alhambra_verde",
            3: "estrella_1906",
            4: "sin_cerveza"
        }
        carta.nombre = nombres.get(carta.valor, None)
    else:
        carta.nombre = None