# src/model/carta.py

import random


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

        # ============================================================
        # AÑADIDO: nombre del comodín según su valor
        # ============================================================
        if tipo == "comodin":
            nombres = {
                1: "estrella_galicia",
                2: "alhambra_verde",
                3: "estrella_1906",
                4: "sin_cerveza"
            }
            self.nombre = nombres.get(valor, None)
        else:
            self.nombre = None

    def __repr__(self):
        if self.tipo == "comodin":
            nombres = {
                1: "Estrella Galicia",
                2: "Alhambra Verde",
                3: "Estrella 1906",
                4: "SIN CERVEZA"
            }
            return f"<Comodín #{self.valor}: {nombres.get(self.valor, 'Desconocido')}>"
        return f"<Carta {self.valor} de {self.palo}>"


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

        # 40 cartas normales
        for palo in self.PALOS:
            for valor in self.VALORES:
                self.cartas.append(Carta(palo, valor, tipo="normal"))

        # 4 comodines numerados 1–4
        for numero in range(1, 5):
            self.cartas.append(Carta(None, numero, tipo="comodin"))

    # -------------------------
    # MÉTODOS PRINCIPALES
    # -------------------------

    def barajar(self):
        """Mezcla las cartas de la baraja."""
        random.shuffle(self.cartas)

    def robar(self):
        """Devuelve la última carta del mazo (o None si está vacío)."""
        if not self.cartas:
            return None
        return self.cartas.pop()

    def repartir(self, n_jugadores, cartas_por_jugador=7):
        """
        Reparte cartas a los jugadores.
        Devuelve una lista de manos: [mano_j1, mano_j2, ...]
        """
        manos = []
        for _ in range(n_jugadores):
            mano = [self.robar() for _ in range(cartas_por_jugador)]
            manos.append(mano)
        return manos
