# src/chinchon.py

from baraja import Baraja
from jugador import Jugador
from comodines import activar_comodin


# ============================================================
# FUNCIÓN mano_valida — DETECTA ESCALERAS, GRUPOS Y CHINCHÓN
# ============================================================

def mano_valida(cartas):
    normales = [c for c in cartas if c.tipo != "comodin"]

    # 1. Chinchón
    if len(normales) == 7:
        palo = normales[0].palo
        valores = sorted(c.valor for c in normales)
        if all(valores[i] + 1 == valores[i+1] for i in range(6)) and all(c.palo == palo for c in normales):
            return True

    # 2. Grupos
    def grupos_validos(cartas):
        valores = {}
        for c in cartas:
            valores.setdefault(c.valor, []).append(c)
        return [g for g in valores.values() if len(g) >= 3]

    # 3. Escaleras
    def escaleras_validas(cartas):
        por_palo = {}
        for c in cartas:
            por_palo.setdefault(c.palo, []).append(c)

        escaleras = []
        for palo, lista in por_palo.items():
            lista_ordenada = sorted(lista, key=lambda x: x.valor)
            temp = [lista_ordenada[0]]
            for i in range(1, len(lista_ordenada)):
                if lista_ordenada[i].valor == lista_ordenada[i-1].valor + 1:
                    temp.append(lista_ordenada[i])
                else:
                    if len(temp) >= 3:
                        escaleras.append(temp)
                    temp = [lista_ordenada[i]]
            if len(temp) >= 3:
                escaleras.append(temp)
        return escaleras

    # 4. Quitar una carta y validar
    for i in range(len(normales)):
        mano_sin = normales[:i] + normales[i+1:]
        grupos = grupos_validos(mano_sin)
        escaleras = escaleras_validas(mano_sin)
        total = sum(len(g) for g in grupos) + sum(len(e) for e in escaleras)
        if total == len(mano_sin):
            return True

    return False


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
        self.baraja = Baraja()
        self.descarte = []

        manos = self.baraja.repartir(len(self.jugadores), 7)
        for jugador, mano in zip(self.jugadores, manos):
            jugador.recibir_cartas(mano)
            jugador.puntos_ronda = 0

        primera = self.baraja.robar()
        if primera:
            self.descarte.append(primera)

        if self.turno_actual >= len(self.jugadores):
            self.turno_actual = 0

    # ============================================================
    # ROBAR DEL MAZO O DEL DESCARTE
    # ============================================================

    def _robar_carta(self, jugador):
        self.escribir("\nOpciones de robo:", self.colores["amarillo"])
        self.escribir("1. Robar del mazo (boca abajo)")
        self.escribir("2. Robar del descarte (boca arriba)")

        if len(self.descarte) > 0:
            carta_superior = self.descarte[-1]
            self.escribir(f"Carta visible: {self._formatear_carta(carta_superior)}", self.colores["cian"])
        else:
            self.escribir("No hay cartas en el descarte.", self.colores["rojo"])

        while True:
            eleccion = input("Elige opción (1 o 2): ").strip()

            # ============================================================
            # ROBAR DEL MAZO — AHORA MUESTRA LA CARTA ROBADA
            # ============================================================
            if eleccion == "1":
                carta = self.baraja.robar()
                if carta is None:
                    self.escribir("El mazo está vacío.", self.colores["rojo"])
                    continue

                jugador.robar_carta(carta)

                # 🔥 NUEVO: mostrar carta robada del mazo
                self.escribir(
                    f"Has robado del mazo: {self._formatear_carta(carta)}",
                    self.colores["verde"]
                )

                return carta

            # ============================================================
            # ROBAR DEL DESCARTE
            # ============================================================
            elif eleccion == "2":
                if len(self.descarte) == 0:
                    self.escribir("No hay carta en el descarte.", self.colores["rojo"])
                    continue

                carta = self.descarte.pop()
                jugador.robar_carta(carta)

                self.escribir(
                    f"Has robado del descarte: {self._formatear_carta(carta)}",
                    self.colores["verde"]
                )

                return carta

            else:
                self.escribir("Opción inválida.", self.colores["rojo"])

    # ============================================================
    # TURNO COMPLETO
    # ============================================================

    def jugar_turno(self):
        # Si no quedan jugadores, terminar
        if len(self.jugadores) == 0:
            return "fin"

        # Asegurar que turno_actual sea válido
        if self.turno_actual >= len(self.jugadores):
            self.turno_actual = 0

        jugador = self.jugadores[self.turno_actual]

        # Si el jugador está eliminado → saltar turno
        if jugador.eliminado:
            self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
            return "continuar"

        # ROBAR
        carta_robada = self._robar_carta(jugador)

        # COMODÍN — puede ELIMINAR a un jugador
        if carta_robada.tipo == "comodin":
            activar_comodin(jugador, carta_robada, self.limpiar, self.escribir, self.colores)

            # 🔥 Eliminación inmediata si el comodín lo requiere
            self.jugadores = [j for j in self.jugadores if not j.eliminado]

            # Verificar si quedan jugadores
            if len(self.jugadores) == 0:
                return "fin"

            # Ajustar turno
            if self.turno_actual >= len(self.jugadores):
                self.turno_actual = 0

            # Si solo queda uno → fin
            if len(self.jugadores) == 1:
                return "fin"

        # AVISO MANO
        if mano_valida(jugador.mano):
            self.escribir("Tu mano es válida.", self.colores["verde"])
        else:
            self.escribir("Tu mano NO es válida.", self.colores["rojo"])

        # CERRAR
        self.escribir(f"{jugador.nombre}, ¿quieres cerrar la ronda?", self.colores["amarillo"])
        opcion = input("Escribe S para cerrar, o ENTER para seguir: ").strip().lower()

        if opcion == "s":
            return self._cerrar_ronda(jugador)

        # DESCARTAR
        carta_descartada = self._elegir_descartar(jugador)

        if carta_descartada.tipo != "comodin":
            self.descarte.append(carta_descartada)

        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        return "continuar"

    # ============================================================
    # ELEGIR CARTA A DESCARTAR (1–8)
    # ============================================================

    def _elegir_descartar(self, jugador):
        self.escribir("\nElige qué carta descartar:", self.colores["amarillo"])

        for i, carta in enumerate(jugador.mano):
            self.escribir(f"{i+1}. {self._formatear_carta(carta)}")

        while True:
            eleccion = input("Número de carta a descartar: ").strip()

            if eleccion.isdigit():
                idx = int(eleccion) - 1
                if 0 <= idx < len(jugador.mano):
                    carta = jugador.mano[idx]
                    jugador.descartar(carta)
                    return carta

            self.escribir("Opción inválida.", self.colores["rojo"])

    # ============================================================
    # CIERRE DE RONDA
    # ============================================================

    def _cerrar_ronda(self, jugador_cierra):
        self.limpiar()
        self.escribir("=== RESUMEN DE LA RONDA ===", self.colores["cian"])
        self.escribir(f"Jugador que cierra: {jugador_cierra.nombre}\n", self.colores["amarillo"])

        # Mostrar cartas
        self.escribir("Cartas de cada jugador:\n", self.colores["verde"])
        for j in self.jugadores:
            mano_str = ", ".join(self._formatear_carta(c) for c in j.mano)
            self.escribir(f"{j.nombre}: {mano_str}", self.colores["reset"])

        # Puntuaciones
        self.escribir("\nPuntuaciones de la ronda:", self.colores["verde"])

        for jugador in self.jugadores:
            if jugador.eliminado:
                continue  # NO sumar puntos a eliminados

            normales = [c for c in jugador.mano if c.tipo != "comodin"]

            if len(normales) == 7:
                valores = sorted(c.valor for c in normales)
                if all(valores[i] + 1 == valores[i+1] for i in range(6)):
                    puntos = -10
                else:
                    puntos = sum(c.valor for c in normales)
            else:
                puntos = sum(c.valor for c in normales)

            jugador.sumar_puntos_ronda(puntos)

            self.escribir(
                f"{jugador.nombre}: +{jugador.puntos_ronda} puntos (Total: {jugador.puntos})",
                self.colores["reset"]
            )

        # ============================================================
        # DETERMINAR GANADOR O ELIMINACIONES
        # ============================================================

        # Guardar lista completa antes de filtrar
        jugadores_antes = self.jugadores.copy()

        # Eliminar jugadores que superaron 100 puntos
        eliminados = []
        for j in self.jugadores:
            if j.puntos >= 100 and not j.eliminado:
                j.eliminado = True
                eliminados.append(j)

        if eliminados:
            self.escribir("\n=== JUGADORES ELIMINADOS ===", self.colores["rojo"])
            for e in eliminados:
                self.escribir(f"{e.nombre} ha sido eliminado con {e.puntos} puntos.", self.colores["rojo"])

        # Filtrar jugadores vivos
        self.jugadores = [j for j in self.jugadores if not j.eliminado]

        # ============================================================
        # CASO ESPECIAL: TODOS LOS JUGADORES ELIMINADOS
        # ============================================================
        if len(self.jugadores) == 0:
            # Todos fueron eliminados, gana el que tenga MENOS puntos
            ganador = min(jugadores_antes, key=lambda x: x.puntos)
            self.escribir("\n⚠️ TODOS LOS JUGADORES SUPERARON 100 PUNTOS", self.colores["amarillo"])
            self.escribir(f"🏆 GANADOR POR MENOR PUNTUACIÓN: {ganador.nombre}", self.colores["verde"])
            return "fin"

        # Ajustar turno si es necesario
        if self.turno_actual >= len(self.jugadores):
            self.turno_actual = 0

        # SI SOLO QUEDA 1 → GANADOR REAL
        if len(self.jugadores) == 1:
            ganador = self.jugadores[0]
            self.escribir(f"\n🏆 GANADOR DE LA PARTIDA: {ganador.nombre}", self.colores["verde"])
            return "fin"

        input("\nPulsa ENTER para continuar...")
        return "cerrado"

    # ============================================================
    # FORMATEAR CARTA
    # ============================================================

    def _formatear_carta(self, carta):
        if carta.tipo == "comodin":
            # Mostrar nombre legible del comodín
            nombres_legibles = {
                "estrella_galicia": "🍺 Estrella Galicia",
                "alhambra_verde": "🍀 Alhambra Verde",
                "estrella_1906": "⭐ Estrella 1906",
                "sin_cerveza": "☠️ SIN CERVEZA"
            }
            return nombres_legibles.get(carta.nombre, "🃏 JOKER")

        if carta.valor == 10:
            letra = "S"
        elif carta.valor == 11:
            letra = "C"
        elif carta.valor == 12:
            letra = "R"
        else:
            letra = str(carta.valor)

        emojis = {
            "oros": "🪙",
            "copas": "🍷",
            "espadas": "⚔️",
            "bastos": "🪵"
        }

        emoji = emojis.get(carta.palo, "?")

        return f"{letra} {emoji}"

    # ============================================================
    # GANADOR REAL
    # ============================================================

    def detectar_ganador(self):
        activos = [j for j in self.jugadores if not j.eliminado]

        if len(activos) == 1:
            return activos[0]

        return None
