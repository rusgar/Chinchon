# tests/test_ambos_suman100.py
# Test para el caso donde ambos jugadores superan 100 puntos en la misma ronda
# y gana el que tenga MENOS puntos

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from chinchon import ChinchonGame
from jugador import Jugador
from baraja import Baraja
from comodines import activar_comodin
import pytest


# ============================================================
# Helper para crear cartas comodín
# ============================================================

class CartaComodin:
    def __init__(self, nombre):
        self.tipo = "comodin"
        self.nombre = nombre
        self.valor = None
        self.palo = None


# ============================================================
# TEST: Ambos jugadores superan 100 puntos en la misma ronda
# ============================================================

def test_ambos_superan_100_menos_puntos_gana():
    """
    Simula una ronda donde ambos jugadores superan 100 puntos.
    Según la regla: gana el jugador con MENOS puntos.
    """
    # Crear juego con 2 jugadores
    nombres = ["Jugador1", "Jugador2"]

    # Mock de funciones de UI para evitar interacción
    def limpiar(): pass
    def escribir(texto, color=None): pass
    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    juego = ChinchonGame(nombres, limpiar, escribir, colores)

    # Crear cartas con valores altos para sumar > 100 puntos
    # Usamos cartas normales: valor 12 (Sota) = 12 puntos cada una
    from baraja import Carta
    cartas_j1 = [Carta("oros", 12) for _ in range(9)]  # 9 * 12 = 108 puntos
    cartas_j2 = [Carta("copas", 12) for _ in range(10)]  # 10 * 12 = 120 puntos

    juego.jugadores[0].mano = cartas_j1
    juego.jugadores[1].mano = cartas_j2

    # Simular que el jugador 1 cierra la ronda
    jugador_cierra = juego.jugadores[0]

    # Ejecutar _cerrar_ronda
    resultado = juego._cerrar_ronda(jugador_cierra)

    # Verificaciones
    assert resultado == "fin", "El juego debe terminar cuando ambos superan 100"

    # El ganador debe ser Jugador1 (108 < 120)
    assert len(juego.jugadores) == 1, "Debe quedar solo un jugador"
    assert juego.jugadores[0].puntos == 108, f"El jugador con menos puntos debe ganar, tiene {juego.jugadores[0].puntos}"
    assert juego.jugadores[0].nombre == "Jugador1", "Jugador1 debe ser el ganador"


# ============================================================
# TEST: Ambos jugadores superan 100, pero uno exactamente 100
# ============================================================

def test_ambos_superan_100_con_exactamente_100():
    """
    Caso borde: un jugador tiene exactamente 100 puntos.
    Según la lógica, 100+ también supera el límite.
    """
    nombres = ["JugadorA", "JugadorB"]

    def limpiar(): pass
    def escribir(texto, color=None): pass
    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    juego = ChinchonGame(nombres, limpiar, escribir, colores)

    from baraja import Carta
    # JugadorA: 100 puntos exactos (8 cartas de 12 = 96, + 1 carta de 4 = 100)
    cartas_j1 = [Carta("oros", 12) for _ in range(8)] + [Carta("oros", 4)]
    # JugadorB: 105 puntos (9 cartas de 12 = 108, pero necesitamos 105, usamos 7*12=84 + 3*7=21 = 105)
    cartas_j2 = [Carta("copas", 12) for _ in range(7)] + [Carta("copas", 7) for _ in range(3)]

    juego.jugadores[0].mano = cartas_j1
    juego.jugadores[1].mano = cartas_j2

    jugador_cierra = juego.jugadores[0]
    resultado = juego._cerrar_ronda(jugador_cierra)

    assert resultado == "fin"
    assert len(juego.jugadores) == 1
    # El que tiene 100 puntos (menos) debe ganar
    assert juego.jugadores[0].puntos == 100
    assert juego.jugadores[0].nombre == "JugadorA"


# ============================================================
# TEST: Solo un jugador supera 100, el otro no
# ============================================================

def test_solo_uno_supera_100_se_elimina_al_superador():
    """
    Si solo uno supera 100, ese se elimina y el otro continúa.
    Como solo queda un jugador, la partida termina.
    """
    nombres = ["JugadorX", "JugadorY"]

    def limpiar(): pass
    def escribir(texto, color=None): pass
    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    juego = ChinchonGame(nombres, limpiar, escribir, colores)

    from baraja import Carta
    # JugadorX: 90 puntos (7 cartas de 12 = 84, + 1 carta de 6 = 90)
    cartas_j1 = [Carta("oros", 12) for _ in range(7)] + [Carta("oros", 6)]
    # JugadorY: 110 puntos (9 cartas de 12 = 108, + 1 carta de 2 = 110)
    cartas_j2 = [Carta("copas", 12) for _ in range(9)] + [Carta("copas", 2)]

    juego.jugadores[0].mano = cartas_j1
    juego.jugadores[1].mano = cartas_j2

    jugador_cierra = juego.jugadores[0]
    resultado = juego._cerrar_ronda(jugador_cierra)

    assert resultado == "fin", "La partida termina cuando solo queda un jugador"
    assert len(juego.jugadores) == 1, "Solo debe quedar un jugador (el que no superó 100)"
    assert juego.jugadores[0].puntos == 90
    assert juego.jugadores[0].nombre == "JugadorX"


# ============================================================
# TEST: Tres jugadores, todos superan 100
# ============================================================

def test_tres_jugadores_todos_superan_100():
    """
    Con 3 jugadores, todos superan 100: gana el de menos puntos.
    """
    nombres = ["A", "B", "C"]

    def limpiar(): pass
    def escribir(texto, color=None): pass
    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    juego = ChinchonGame(nombres, limpiar, escribir, colores)

    from baraja import Carta
    # Jugador A: 115 puntos (9 cartas de 12 = 108, + 1 carta de 7 = 115)
    cartas_a = [Carta("oros", 12) for _ in range(9)] + [Carta("oros", 7)]
    # Jugador B: 105 puntos (8 cartas de 12 = 96, + 1 carta de 9 = 105)
    cartas_b = [Carta("copas", 12) for _ in range(8)] + [Carta("copas", 9)]
    # Jugador C: 125 puntos (10 cartas de 12 = 120, + 1 carta de 5 = 125)
    cartas_c = [Carta("espadas", 12) for _ in range(10)] + [Carta("espadas", 5)]

    juego.jugadores[0].mano = cartas_a
    juego.jugadores[1].mano = cartas_b
    juego.jugadores[2].mano = cartas_c

    jugador_cierra = juego.jugadores[0]
    resultado = juego._cerrar_ronda(jugador_cierra)

    assert resultado == "fin"
    assert len(juego.jugadores) == 1
    assert juego.jugadores[0].puntos == 105
    assert juego.jugadores[0].nombre == "B"
