# src/validation/validador.py

from validation.validador_funcs.filtrar_normales import filtrar_normales
from validation.validador_funcs.detectar_escaleras import detectar_escaleras
from validation.validador_funcs.detectar_grupos import detectar_grupos
from validation.validador_funcs.es_chinchon import es_chinchon


def _filtrar_normales(cartas):
    """Devuelve solo las cartas normales (ignora comodines)."""
    return filtrar_normales(cartas)


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
    return detectar_escaleras(cartas)


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
    return detectar_grupos(cartas)


# ---------------------------------------------------------
# DETECTAR CHINCHÓN
# ---------------------------------------------------------

def es_chinchon(cartas):
    """
    Determina si las 7 cartas forman un Chinchón completo.
    Los comodines NO se usan aquí (versión básica).
    """
    return es_chinchon(cartas)
