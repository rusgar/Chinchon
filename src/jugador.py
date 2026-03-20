# src/jugador.py

class Jugador:
    """
    Representa a un jugador del Chinchón.

    Atributos:
        nombre (str): Nombre del jugador.
        mano (list[Carta]): Cartas actuales en la mano.
        puntos (int): Puntuación acumulada entre rondas.
        eliminado (bool): Estado del jugador (True si está fuera de la partida).
        uso_comodin (dict[int,bool]): Registro de comodines usados (1–4).
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.puntos = 0
        self.eliminado = False

        # Registro de uso de comodines (1–4)
        self.uso_comodin = {
            1: False,  # Estrella Galicia
            2: False,  # Alhambra Verde
            3: False,  # Estrella 1906
            4: False   # SIN CERVEZA (Muerte)
        }

    # -------------------------
    # MÉTODOS DE MANO
    # -------------------------

    def recibir_cartas(self, cartas):
        """Añade varias cartas a la mano (reparto inicial)."""
        self.mano.extend(cartas)

    def robar_carta(self, carta):
        """Añade una carta a la mano del jugador."""
        if carta is not None:
            self.mano.append(carta)
        return carta

    def descartar(self, carta):
        """
        Elimina una carta de la mano y la devuelve.
        Si la carta no está en la mano, devuelve None.
        """
        if carta in self.mano:
            self.mano.remove(carta)
            return carta
        return None

    def limpiar_mano(self):
        """Vacía la mano al final de una ronda."""
        self.mano = []

    # -------------------------
    # PUNTUACIÓN ENTRE RONDAS
    # -------------------------

    def sumar_puntos_ronda(self, puntos):
        """
        Suma los puntos obtenidos en una ronda.
        Comprueba si el jugador queda eliminado.
        """
        self.puntos += puntos

        if self.puntos >= 100:
            self.eliminado = True

    def restar_puntos(self, puntos):
        """
        Resta puntos (usado por comodines).
        Nunca baja de 0.
        """
        self.puntos = max(0, self.puntos - puntos)

    def fijar_puntos(self, nuevo_valor):
        """
        Establece directamente la puntuación del jugador.
        Útil para comodines como Alhambra Verde o Estrella Galicia.
        """
        self.puntos = max(0, nuevo_valor)

        if self.puntos >= 100:
            self.eliminado = True

    # -------------------------

    def __repr__(self):
        estado = "ELIMINADO" if self.eliminado else "activo"
        return f"<Jugador {self.nombre} | {self.puntos} pts | {estado}>"
