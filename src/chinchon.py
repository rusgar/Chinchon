# src/chinchon.py

from baraja import Baraja
from jugador import Jugador
from validador import detectar_escaleras, detectar_grupos, es_chinchon


# ---------------------------------------------------------
# VALIDACIÓN DE MANO PARA CIERRE DE RONDA
# ---------------------------------------------------------

def mano_valida(cartas):
    """
    Comprueba si la mano puede cerrar:
        - Es un Chinchón (7 cartas)
        - O descartando 1 carta, el resto forma combinaciones válidas
    """

    # Caso especial: Chinchón completo
    if es_chinchon(cartas):
        return True

    # Probar descartar cada carta
    for i in range(len(cartas)):
        mano_sin = cartas[:i] + cartas[i+1:]

        escaleras = detectar_escaleras(mano_sin)
        grupos = detectar_grupos(mano_sin)

        total = sum(len(e) for e in escaleras) + sum(len(g) for g in grupos)

        if total == len(mano_sin):
            return True

    return False


# ---------------------------------------------------------
# CLASE PRINCIPAL DEL JUEGO
# ---------------------------------------------------------

class ChinchonGame:
    """
    Controla el flujo de la partida de Chinchón.
    Gestiona:
        - mazo
        - pila de descarte
        - turnos
        - activación automática de comodines
        - cierre de ronda
    """

    def __init__(self, nombres_jugadores):
        self.baraja = Baraja()
        self.descarte = []
        self.jugadores = [Jugador(nombre) for nombre in nombres_jugadores]
        self.turno_actual = 0

        # Reparto inicial
        manos = self.baraja.repartir(len(self.jugadores), 7)
        for jugador, mano in zip(self.jugadores, manos):
            jugador.recibir_cartas(mano)

        # Primera carta al descarte
        primera = self.baraja.robar()
        if primera:
            self.descarte.append(primera)

    # ---------------------------------------------------------
    # GESTIÓN DE MAZO Y DESCARTE
    # ---------------------------------------------------------

    def _robar_del_mazo(self):
        """Roba una carta del mazo. Si está vacío, recicla el descarte."""
        carta = self.baraja.robar()

        if carta is None:
            print(">>> El mazo está vacío. Reciclando descarte...")

            if len(self.descarte) <= 1:
                print(">>> No hay suficientes cartas para reciclar.")
                return None

            # Guardar la carta superior del descarte
            carta_superior = self.descarte.pop()

            # Pasar el resto al mazo
            self.baraja.cartas = self.descarte[:]
            self.descarte = [carta_superior]

            # Barajar el nuevo mazo
            self.baraja.barajar()

            # Robar ahora sí
            carta = self.baraja.robar()

        return carta

    # ---------------------------------------------------------
    # FLUJO DE UN TURNO
    # ---------------------------------------------------------

    def jugar_turno(self):
        jugador = self.jugadores[self.turno_actual]
        print(f"\nTurno de {jugador.nombre}")

        # 1. ROBAR
        carta_robada = self._robar_del_mazo()
        print(f"{jugador.nombre} roba: {carta_robada}")
        jugador.robar_carta(carta_robada)

        # 2. ACTIVAR COMODÍN AUTOMÁTICAMENTE
        if carta_robada.tipo == "comodin":
            self._activar_comodin(jugador, carta_robada)

        # 3. ¿PUEDE CERRAR?
        if mano_valida(jugador.mano):
            print(f"  >>> {jugador.nombre} puede CERRAR la ronda")
            self._cerrar_ronda(jugador)
            return  # La ronda termina aquí

        # 4. DESCARTAR
        carta_descartada = self._descartar_carta(jugador)
        self.descarte.append(carta_descartada)
        print(f"{jugador.nombre} descarta: {carta_descartada}")

        # Pasar turno
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)

    # ---------------------------------------------------------
    # ACTIVACIÓN DE COMODINES
    # ---------------------------------------------------------

    def _activar_comodin(self, jugador, carta):
        numero = carta.valor
        jugador.uso_comodin[numero] = True

        print(f"  >>> {jugador.nombre} activa el COMODÍN #{numero}")

        if numero == 1:
            print("  Efecto: Estrella Galicia → fijar puntos a 80")
            jugador.fijar_puntos(80)

        elif numero == 2:
            print("  Efecto: Alhambra Verde → fijar puntos a 25")
            jugador.fijar_puntos(25)

        elif numero == 3:
            print("  Efecto: Estrella 1906 → restar 25 puntos")
            jugador.restar_puntos(25)

        elif numero == 4:
            print("  Efecto: MUERTE → jugador eliminado")
            jugador.eliminado = True

    # ---------------------------------------------------------
    # DECISIÓN DE JUGADA (informativa)
    # ---------------------------------------------------------

    def _decidir_jugada(self, jugador):
        escaleras = detectar_escaleras(jugador.mano)
        grupos = detectar_grupos(jugador.mano)

        if escaleras:
            print(f"  Escaleras detectadas: {escaleras}")
        if grupos:
            print(f"  Grupos detectados: {grupos}")

        if es_chinchon(jugador.mano):
            print(f"  ¡{jugador.nombre} tiene CHINCHÓN!")

    # ---------------------------------------------------------
    # DESCARTAR
    # ---------------------------------------------------------

    def _descartar_carta(self, jugador):
        """Versión básica: descarta la última carta de la mano."""
        carta = jugador.mano[-1]
        jugador.descartar(carta)
        return carta

    # ---------------------------------------------------------
    # CIERRE DE RONDA
    # ---------------------------------------------------------

    def _cerrar_ronda(self, jugador):
        print(f"\n>>> {jugador.nombre} CIERRA LA RONDA")

        escaleras = detectar_escaleras(jugador.mano)
        grupos = detectar_grupos(jugador.mano)

        print("  Escaleras:", escaleras)
        print("  Grupos:", grupos)

        if es_chinchon(jugador.mano):
            print("  ¡CHINCHÓN!")

        # Aquí luego se calcularán los puntos y se preparará la siguiente ronda
