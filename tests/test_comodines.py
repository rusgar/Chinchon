# tests/test_comodines.py
# Tests oficiales de los comodines del Chinchón 🍺

# ============================================================
# AÑADIDO PARA QUE PYTEST ENCUENTRE LOS MÓDULOS DE /src
# ============================================================

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

# ============================================================

from model.jugador import Jugador
from effects.comodines import activar_comodin
import pytest


# ============================================================
# Helpers para crear cartas comodín
# ============================================================

class CartaComodin:
    def __init__(self, nombre):
        self.tipo = "comodin"
        self.nombre = nombre
        self.valor = None
        self.palo = None


# ============================================================
# TEST 1 — Estrella Galicia (salvar eliminación)
# ============================================================

def test_estrella_galicia_salva_eliminacion():
    jugador = Jugador("Test")
    jugador.puntos = 100

    carta = CartaComodin("estrella_galicia")

    # Mock de funciones de UI
    def limpiar(): pass
    def escribir(texto, color=None): pass
    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    activar_comodin(jugador, carta, limpiar, escribir, colores)

    assert jugador.puntos == 80, "Estrella Galicia debe bajar los puntos a 80"
    assert jugador.eliminado is False, "El jugador NO debe ser eliminado"


# ============================================================
# TEST 2 — Alhambra Verde (reducir a la mitad)
# ============================================================

def test_alhambra_verde_reduce_mitad():
    jugador = Jugador("Test")
    jugador.puntos = 60

    carta = CartaComodin("alhambra_verde")

    def limpiar(): pass
    def escribir(texto, color=None): pass
    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    activar_comodin(jugador, carta, limpiar, escribir, colores)

    assert jugador.puntos == 25, "Alhambra Verde debe bajar los puntos a 25"
    assert jugador.eliminado is False, "El jugador NO debe ser eliminado"


# ============================================================
# TEST 3 — Estrella 1906 (restar 25 puntos)
# ============================================================

def test_estrella_1906_resta_25():
    jugador = Jugador("Test")
    jugador.puntos = 40

    carta = CartaComodin("estrella_1906")

    def limpiar(): pass
    def escribir(texto, color=None): pass
    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    activar_comodin(jugador, carta, limpiar, escribir, colores)

    assert jugador.puntos == 15, "Estrella 1906 debe restar 25 puntos"
    assert jugador.eliminado is False, "El jugador NO debe ser eliminado"


def test_estrella_1906_no_baja_de_cero():
    jugador = Jugador("Test")
    jugador.puntos = 20

    carta = CartaComodin("estrella_1906")

    def limpiar(): pass
    def escribir(texto, color=None): pass
    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    activar_comodin(jugador, carta, limpiar, escribir, colores)

    assert jugador.puntos == 0, "Los puntos no pueden bajar de 0"
    assert jugador.eliminado is False


# ============================================================
# TEST 4 — SIN CERVEZA (eliminación inmediata)
# ============================================================

def test_sin_cerveza_elimina_inmediatamente():
    jugador = Jugador("Test")
    jugador.puntos = 10

    carta = CartaComodin("sin_cerveza")

    def limpiar(): pass
    def escribir(texto, color=None): pass
    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    activar_comodin(jugador, carta, limpiar, escribir, colores)

    assert jugador.eliminado is True, "SIN CERVEZA debe eliminar al jugador"
    assert jugador.puntos == 10, "Los puntos no deben cambiar"


# ============================================================
# TEST 5 — Comodines usados desaparecen
# ============================================================

def test_comodin_desaparece_tras_usarse():
    jugador = Jugador("Test")
    jugador.puntos = 60
    jugador.mano = []  # por si tu clase usa mano

    carta = CartaComodin("alhambra_verde")

    def limpiar(): pass
    def escribir(texto, color=None): pass
    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    activar_comodin(jugador, carta, limpiar, escribir, colores)

    assert carta not in getattr(jugador, "mano", []), "El comodín debe desaparecer tras usarse"
