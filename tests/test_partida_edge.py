import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import pytest
from model.carta import Baraja, Carta
from game.chinchon import ChinchonGame


def test_mazo_vacio_robar_card_desde_descartar(monkeypatch):
    def limpiar():
        pass

    def escribir(texto, color=None):
        pass

    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    juego = ChinchonGame(["Jugador1", "Jugador2"], limpiar, escribir, colores)
    juego.baraja.cartas = []
    juego.descarte = [Carta("oros", 5)]

    jugador = juego.jugadores[0]
    inputs = iter(["1", "2"])

    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    carta = juego._robar_carta(jugador)

    assert carta is not None
    assert carta.palo == "oros"
    assert carta.valor == 5
    assert len(juego.descarte) == 0


def test_un_solo_jugador_detectar_ganador():
    def limpiar():
        pass

    def escribir(texto, color=None):
        pass

    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    juego = ChinchonGame(["Solo"], limpiar, escribir, colores)

    # Con un único jugador, debería detectarse ganador inmediato
    ganador = juego.detectar_ganador()
    assert ganador is not None
    assert ganador.nombre == "Solo"


def test_partida_completa_cierre_mano_valida_y_eliminacion(monkeypatch):
    def limpiar():
        pass

    def escribir(texto, color=None):
        pass

    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    juego = ChinchonGame(["PlayerA", "PlayerB"], limpiar, escribir, colores)

    # Forzar manos para que al cerrar ambos se eliminen en la misma ronda
    juego.jugadores[0].mano = [Carta("oros", 12) for _ in range(7)]
    juego.jugadores[1].mano = [Carta("copas", 12) for _ in range(7)]
    juego.jugadores[0].puntos = 95
    juego.jugadores[1].puntos = 98

    # Saltar el prompt de continuar
    monkeypatch.setattr("builtins.input", lambda prompt="": "")

    resultado = juego._cerrar_ronda(juego.jugadores[0])

    assert resultado == "fin"
    assert len(juego.jugadores) == 1
    assert juego.jugadores[0].nombre == "PlayerA"
    assert juego.jugadores[0].puntos <= juego.jugadores[0].puntos
