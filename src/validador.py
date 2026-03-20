# src/validador.py

def _filtrar_normales(cartas):
    """Devuelve solo las cartas normales (ignora comodines)."""
    return [c for c in cartas if c.tipo == "normal"]


# ---------------------------------------------------------
# DETECTAR ESCALERAS
# ---------------------------------------------------------

def detectar_escaleras(cartas):
    """
    Detecta escaleras válidas en una lista de cartas.
    Una escalera es:
        - 3 o más cartas
        - mismo palo
        - valores consecutivos
    Los comodines se ignoran en esta validación básica.
    """

    cartas_normales = _filtrar_normales(cartas)

    # Agrupar por palo
    palos = {}
    for carta in cartas_normales:
        palos.setdefault(carta.palo, []).append(carta)

    escaleras = []

    for palo, grupo in palos.items():
        grupo_ordenado = sorted(grupo, key=lambda c: c.valor)
        secuencia = [grupo_ordenado[0]]

        for i in range(1, len(grupo_ordenado)):
            actual = grupo_ordenado[i]
            anterior = grupo_ordenado[i - 1]

            if actual.valor == anterior.valor + 1:
                secuencia.append(actual)
            else:
                if len(secuencia) >= 3:
                    escaleras.append(secuencia)
                secuencia = [actual]

        if len(secuencia) >= 3:
            escaleras.append(secuencia)

    return escaleras


# ---------------------------------------------------------
# DETECTAR GRUPOS
# ---------------------------------------------------------

def detectar_grupos(cartas):
    """
    Detecta grupos válidos en una lista de cartas.
    Un grupo es:
        - 3 o más cartas
        - mismo valor
        - palos distintos
    Los comodines se ignoran.
    """

    cartas_normales = _filtrar_normales(cartas)

    valores = {}
    for carta in cartas_normales:
        valores.setdefault(carta.valor, []).append(carta)

    grupos = []

    for valor, grupo in valores.items():
        if len(grupo) >= 3:
            grupos.append(grupo)

    return grupos


# ---------------------------------------------------------
# DETECTAR CHINCHÓN
# ---------------------------------------------------------

def es_chinchon(cartas):
    """
    Determina si las 7 cartas forman un Chinchón completo.
    Los comodines NO se usan aquí (versión básica).
    """

    if len(cartas) != 7:
        return False

    # Escalera de 7 cartas
    escaleras = detectar_escaleras(cartas)
    for escalera in escaleras:
        if len(escalera) == 7:
            return True

    # Grupo de 7 (teóricamente imposible en baraja española)
    grupos = detectar_grupos(cartas)
    for grupo in grupos:
        if len(grupo) == 7:
            return True

    return False
