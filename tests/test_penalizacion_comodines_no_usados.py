# tests/test_penalizacion_comodines_no_usados.py
# Test para verificar la penalización por comodines no usados al ganador

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import pytest
from model.carta import Baraja, Carta
from game.chinchon import ChinchonGame


def test_penalizacion_comodines_no_usados_ganador(monkeypatch):
    """Test que verifica que el ganador recibe -5 puntos por cada comodín no usado en su mano."""

    def limpiar():
        pass

    def escribir(texto, color=None):
        pass

    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    # Crear juego con 2 jugadores
    juego = ChinchonGame(["Ganador", "Perdedor"], limpiar, escribir, colores)

    # Forzar que el primer jugador tenga 3 comodines en su mano (no usados)
    # y cartas normales que sumen pocos puntos
    comodines = [Carta(None, 1, "comodin"),  # Estrella Galicia
                 Carta(None, 2, "comodin"),  # Alhambra Verde
                 Carta(None, 3, "comodin")]  # Estrella 1906
    cartas_normales = [Carta("oros", 1), Carta("oros", 2), Carta("oros", 3), Carta("oros", 4)]
    juego.jugadores[0].mano = comodines + cartas_normales

    # El segundo jugador tiene una mano que suma más puntos
    juego.jugadores[1].mano = [Carta("copas", 12) for _ in range(7)]
    juego.jugadores[1].puntos = 95  # Cerca de eliminación

    # El primer jugador tiene pocos puntos inicialmente
    juego.jugadores[0].puntos = 10

    # Simular que el primer jugador cierra la ronda
    # Saltar el prompt de continuar
    monkeypatch.setattr("builtins.input", lambda prompt="": "")

    # Cerrar ronda con el primer jugador
    resultado = juego._cerrar_ronda(juego.jugadores[0])

    # Verificar que terminó la partida
    assert resultado == "fin"

    # Verificar que queda solo el ganador
    assert len(juego.jugadores) == 1
    assert juego.jugadores[0].nombre == "Ganador"

    # Verificar penalización: 3 comodines * 5 puntos = 15 puntos menos
    # Puntos iniciales: 10
    # Puntos de ronda: suma de cartas normales (1+2+3+4=10)
    # Penalización: -15
    # Total esperado: 10 + 10 - 15 = 5
    assert juego.jugadores[0].puntos == 5, f"Puntos esperados: 5, obtenidos: {juego.jugadores[0].puntos}"


def test_sin_penalizacion_sin_comodines(monkeypatch):
    """Test que verifica que no hay penalización si el ganador no tiene comodines."""

    def limpiar():
        pass

    def escribir(texto, color=None):
        pass

    colores = {"rojo": "", "verde": "", "amarillo": "", "cian": "", "reset": ""}

    # Crear juego con 2 jugadores
    juego = ChinchonGame(["Ganador", "Perdedor"], limpiar, escribir, colores)

    # El ganador tiene solo cartas normales
    juego.jugadores[0].mano = [Carta("oros", 1), Carta("oros", 2), Carta("oros", 3),
                               Carta("oros", 4), Carta("oros", 5), Carta("oros", 6), Carta("oros", 7)]

    # El perdedor tiene cartas que suman más
    juego.jugadores[1].mano = [Carta("copas", 12) for _ in range(7)]
    juego.jugadores[1].puntos = 95

    juego.jugadores[0].puntos = 10

    # Simular cierre
    monkeypatch.setattr("builtins.input", lambda prompt="": "")

    resultado = juego._cerrar_ronda(juego.jugadores[0])

    assert resultado == "fin"
    assert len(juego.jugadores) == 1
    assert juego.jugadores[0].nombre == "Ganador"

    # Chinchón: -10 puntos
    # Total esperado: 10 - 10 = 0 (sin penalización por comodines)
    assert juego.jugadores[0].puntos == 0, f"Puntos esperados: 0, obtenidos: {juego.jugadores[0].puntos}"