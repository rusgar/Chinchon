# src/model/jugador.py

from model.jugador_funcs.inicializar_jugador import inicializar_jugador
from model.jugador_funcs.recibir_cartas import recibir_cartas
from model.jugador_funcs.robar_carta import robar_carta
from model.jugador_funcs.descartar import descartar
from model.jugador_funcs.sumar_puntos_ronda import sumar_puntos_ronda
from model.jugador_funcs.fijar_puntos import fijar_puntos
from model.jugador_funcs.restar_puntos import restar_puntos


class Jugador:
    def __init__(self, nombre):
        inicializar_jugador(self, nombre)

    def recibir_cartas(self, cartas):
        recibir_cartas(self, cartas)

    def robar_carta(self, carta):
        robar_carta(self, carta)

    def descartar(self, carta):
        descartar(self, carta)

    def sumar_puntos_ronda(self, puntos):
        sumar_puntos_ronda(self, puntos)

    def fijar_puntos(self, valor):
        fijar_puntos(self, valor)

    def restar_puntos(self, valor):
        restar_puntos(self, valor)
