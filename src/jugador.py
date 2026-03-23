# src/jugador.py

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.puntos = 0
        self.eliminado = False

        # Puntos sumados en la ronda actual
        self.puntos_ronda = 0

        # Estado de uso de comodines (1–4)
        self.uso_comodin = {1: False, 2: False, 3: False, 4: False}

    def recibir_cartas(self, cartas):
        self.mano = cartas

    def robar_carta(self, carta):
        self.mano.append(carta)

    def descartar(self, carta):
        self.mano.remove(carta)

    def sumar_puntos_ronda(self, puntos):
        self.puntos_ronda = puntos
        self.puntos += puntos
        if self.puntos >= 100:
            self.eliminado = True

    def fijar_puntos(self, valor):
        self.puntos = valor
        if self.puntos >= 100:
            self.eliminado = True

    def restar_puntos(self, valor):
        self.puntos = max(0, self.puntos - valor)
