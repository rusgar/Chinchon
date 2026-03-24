# src/model/carta.py

import random
from model.carta_funcs.asignar_nombre_comodin import asignar_nombre_comodin
from model.carta_funcs.formatear_carta_repr import formatear_carta_repr
from model.carta_funcs.crear_baraja import crear_baraja
from model.carta_funcs.barajar import barajar
from model.carta_funcs.robar import robar
from model.carta_funcs.repartir import repartir


class Carta:
    """
    Representa una carta de la baraja española.

    Atributos:
        palo (str | None): 'oros', 'copas', 'espadas', 'bastos' o None si es comodín.
        valor (int): 1–7, 10–12 para cartas normales; 1–4 para comodines especiales.
        tipo (str): 'normal' o 'comodin'.
        nombre (str | None): nombre del comodín (solo si tipo == 'comodin')
    """

    def __init__(self, palo, valor, tipo="normal"):
        self.palo = palo
        self.valor = valor
        self.tipo = tipo

        asignar_nombre_comodin(self)

    def __repr__(self):
        return formatear_carta_repr(self)


class Baraja:
    """
    Baraja española de 40 cartas + 4 comodines numerados (1–4).
    """

    PALOS = ["oros", "copas", "espadas", "bastos"]
    VALORES = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

    def __init__(self):
        self.cartas = []
        self._crear_baraja()
        self.barajar()

    # -------------------------
    # CREACIÓN DE LA BARAJA
    # -------------------------

    def _crear_baraja(self):
        """Genera las 40 cartas normales y los 4 comodines especiales."""
        crear_baraja(self)

    # -------------------------
    # MÉTODOS PRINCIPALES
    # -------------------------

    def barajar(self):
        """Mezcla las cartas de la baraja."""
        barajar(self)

    def robar(self):
        """Devuelve la última carta del mazo (o None si está vacío)."""
        return robar(self)

    def repartir(self, n_jugadores, cartas_por_jugador=7):
        """
        Reparte cartas a los jugadores.
        Devuelve una lista de manos: [mano_j1, mano_j2, ...]
        """
        return repartir(self, n_jugadores, cartas_por_jugador)
