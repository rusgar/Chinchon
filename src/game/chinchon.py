# src/game/chinchon.py

from model.carta import Baraja
from model.jugador import Jugador
from game.chinchon_funcs.iniciar_nueva_ronda import iniciar_nueva_ronda
from game.chinchon_funcs.robar_carta import robar_carta
from game.chinchon_funcs.procesar_comodin import procesar_comodin
from game.chinchon_funcs.avisar_mano_valida import avisar_mano_valida
from game.chinchon_funcs.preguntar_cierre import preguntar_cierre
from game.chinchon_funcs.procesar_descarte import procesar_descarte
from game.chinchon_funcs.avanzar_turno import avanzar_turno
from game.chinchon_funcs.elegir_descartar import elegir_descartar
from game.chinchon_funcs.mostrar_resumen_ronda import mostrar_resumen_ronda
from game.chinchon_funcs.calcular_y_mostrar_puntuaciones import calcular_y_mostrar_puntuaciones
from game.chinchon_funcs.cerrar_ronda import cerrar_ronda
from game.chinchon_funcs.jugar_turno import jugar_turno
from game.chinchon_funcs.mano_valida import mano_valida
from game.chinchon_funcs.formatear_carta import formatear_carta
from game.chinchon_funcs.calcular_puntos_jugador import calcular_puntos_jugador
from game.chinchon_funcs.procesar_eliminaciones_y_ganador import procesar_eliminaciones_y_ganador
from game.chinchon_funcs.detectar_ganador import detectar_ganador


# ============================================================
# CLASE PRINCIPAL DEL JUEGO
# ============================================================

class ChinchonGame:
    def __init__(self, nombres_jugadores, limpiar, escribir, colores):
        self.limpiar = limpiar
        self.escribir = escribir
        self.colores = colores

        self.jugadores = [Jugador(nombre) for nombre in nombres_jugadores]
        self.todos_jugadores = self.jugadores.copy()  # Guardar copia original para estadísticas (puntos acumulados)
        self.turno_actual = 0

        self._iniciar_nueva_ronda()

    def _iniciar_nueva_ronda(self):
        iniciar_nueva_ronda(self)

    # ============================================================
    # ROBAR DEL MAZO O DEL DESCARTES
    # ============================================================

    def _robar_carta(self, jugador):
        return robar_carta(self, jugador)

    # ============================================================
    # TURNO COMPLETO
    # ============================================================

    def jugar_turno(self):
        return jugar_turno(self)

    def _procesar_comodin(self, jugador, carta):
        return procesar_comodin(self, jugador, carta)

    def _avisar_mano_valida(self, jugador):
        return avisar_mano_valida(self, jugador)

    def _preguntar_cierre(self, jugador):
        return preguntar_cierre(self, jugador)

    def _procesar_descarte(self, jugador):
        return procesar_descarte(self, jugador)

    def _avanzar_turno(self):
        return avanzar_turno(self)

    # ============================================================
    # ELEGIR CARTA A DESCARTAR (1–8)
    # ============================================================

    def _elegir_descartar(self, jugador):
        return elegir_descartar(self, jugador)

    # ============================================================
    # CIERRE DE RONDA
    # ============================================================

    def _cerrar_ronda(self, jugador_cierra):
        return cerrar_ronda(self, jugador_cierra)

    def _mostrar_resumen_ronda(self, jugador_cierra):
        return mostrar_resumen_ronda(self, jugador_cierra)

    def _calcular_y_mostrar_puntuaciones(self):
        return calcular_y_mostrar_puntuaciones(self)

    def _calcular_puntos_jugador(self, jugador):
        """Calcula los puntos de un jugador en esta ronda usando la función externa."""
        return calcular_puntos_jugador(jugador)

    def _procesar_eliminaciones_y_ganador(self):
        """Procesa eliminaciones y determina si hay ganador usando módulo externo."""
        return procesar_eliminaciones_y_ganador(self, self.limpiar, self.escribir, self.colores)

    # ============================================================
    # FORMATEAR CARTA
    # ============================================================

    def _formatear_carta(self, carta):
        return formatear_carta(carta)

    # ============================================================
    # DETECTAR GANADOR
    # ============================================================

    def detectar_ganador(self):
        return detectar_ganador(self)


# Re-exportar la clase para compatibilidad
__all__ = ["ChinchonGame"]
