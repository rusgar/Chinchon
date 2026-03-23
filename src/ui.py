# src/ui.py

import os
import sys
import time

RESET = "\033[0m"
BOLD = "\033[1m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"

COLORES = {
    "rojo": ROJO,
    "verde": VERDE,
    "amarillo": AMARILLO,
    "cian": CIAN,
    "magenta": MAGENTA,
    "reset": RESET,
    "cyan": CIAN,
}


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def escribir(texto, color=RESET):
    print(color + texto + RESET)


def animar_texto(texto, color=RESET, delay=0.05):
    for char in texto:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def imprimir_titulo():
    escribir("=" * 40, CIAN)
    escribir("        JUEGO DE CHINCHÓN 🍺        ", AMARILLO)
    escribir("=" * 40, CIAN)
    print()


def imprimir_menu_principal():
    imprimir_titulo()
    print("1. Iniciar nueva partida")
    print("2. Ver reglas básicas")
    print("3. Créditos")
    print("4. Tabla de puntuaciones (demo)")
    print("5. Salir")
    print()


def leer_opcion(msg="Selecciona una opción: "):
    return input(msg).strip()


SIMBOLOS_PALOS = {
    "oros": "♦",
    "copas": "♥",
    "espadas": "♠",
    "bastos": "♣",
}


def carta_a_ascii(carta):
    if carta.tipo == "comodin":
        # Emojis específicos para cada comodín
        emojis_comodines = {
            "estrella_galicia": "🍺",
            "alhambra_verde": "🍀",
            "estrella_1906": "⭐",
            "sin_cerveza": "☠️"
        }
        # Mostrar emoji del comodín en el centro
        emoji = emojis_comodines.get(carta.nombre, "🃏")
        # Iniciales para las esquinas
        nombres_cortos = {
            "estrella_galicia": "EG",
            "alhambra_verde": "AV",
            "estrella_1906": "E6",
            "sin_cerveza": "SC"
        }
        valor = nombres_cortos.get(carta.nombre, "JK")
        palo = emoji  # El emoji va en el centro
    else:
        valor = str(carta.valor)
        palo = SIMBOLOS_PALOS[carta.palo]

    return [
        "┌─────────┐",
        f"│{valor.ljust(3)}       │",
        f"│    {palo}    │",
        f"│       {valor.rjust(3)}│",
        "└─────────┘",
    ]


def mostrar_mano(jugador):
    ascii_cartas = [carta_a_ascii(c) for c in jugador.mano]
    for i in range(5):
        print("  ".join(c[i] for c in ascii_cartas))
    print()


def iniciar_partida():
    from chinchon import ChinchonGame

    limpiar_pantalla()
    imprimir_titulo()

    print("Introduce los nombres de los jugadores.\n")
    nombres = []

    # ============================================================
    # VALIDACIÓN DE JUGADORES (MÍNIMO 2, MÁXIMO 4)
    # ============================================================

    while True:
        nombre = input("Nombre: ").strip()

        if nombre == "":
            break

        nombres.append(nombre)

        if len(nombres) == 4:
            print("\n⚠️ Máximo de 4 jugadores alcanzado.")
            break

    if len(nombres) < 2:
        print("❌ Se necesitan al menos 2 jugadores.")
        input("ENTER...")
        return None, None

    # Crear partida
    juego = ChinchonGame(nombres, limpiar_pantalla, escribir, COLORES)

    # Bucle de toda la partida
    while True:
        # Verificar si quedan jugadores
        if len(juego.jugadores) == 0:
            escribir("\n❌ NO QUEDAN JUGADORES EN LA PARTIDA", COLORES["rojo"])
            break

        # Asegurar que turno_actual sea válido
        if juego.turno_actual >= len(juego.jugadores):
            juego.turno_actual = 0

        limpiar_pantalla()
        jugador = juego.jugadores[juego.turno_actual]

        imprimir_titulo()
        print(f"Turno de {jugador.nombre}\n")
        mostrar_mano(jugador)

        input("Pulsa ENTER para robar carta...")

        resultado = juego.jugar_turno()

        if resultado == "cerrado":
            ganador = juego.detectar_ganador()
            if ganador:
                break

            # Reiniciar ronda SIN perder puntos
            juego._iniciar_nueva_ronda()
            continue

        ganador = juego.detectar_ganador()
        if ganador:
            break

    # La partida ha terminado
    ganador = juego.jugadores[0] if juego.jugadores else None
    # Devolver todos los jugadores originales con sus puntos acumulados
    return ganador, juego.todos_jugadores


def menu_principal_loop():
    # Estadísticas globales
    partidas_jugadas = 0
    victorias = {}  # {nombre_jugador: partidas_ganadas}
    puntuaciones_totales = {}  # {nombre_jugador: puntos_acumulados}

    while True:
        limpiar_pantalla()
        imprimir_menu_principal()

        # Mostrar estadísticas en el menú
        if partidas_jugadas > 0:
            print("📊 ESTADÍSTICAS:")
            print(f"   Partidas jugadas: {partidas_jugadas}")
            for nombre, wins in sorted(victorias.items(), key=lambda x: x[1], reverse=True):
                print(f"   {nombre}: {wins} victorias")
            print()

        opcion = leer_opcion()

        if opcion == "1":
            ganador, jugadores_finales = iniciar_partida()

            # Incrementar partidas jugadas
            partidas_jugadas += 1

            # Registrar victoria y puntuaciones
            if jugadores_finales:
                for jugador in jugadores_finales:
                    # Acumular puntos totales
                    puntuaciones_totales[jugador.nombre] = puntuaciones_totales.get(jugador.nombre, 0) + jugador.puntos

            if ganador:
                victorias[ganador.nombre] = victorias.get(ganador.nombre, 0) + 1

            # Preguntar si quiere jugar otra partida
            limpiar_pantalla()
            print("¿Jugar otra partida?")
            print("1. Sí")
            print("2. No (ver resumen y salir)")
            opcion = input("Selecciona: ").strip()

            if opcion != "1":
                # Mostrar resumen completo
                limpiar_pantalla()
                imprimir_titulo()
                print("\n" + "=" * 40)
                print("      📈 RESUMEN FINAL DE PARTIDAS")
                print("=" * 40 + "\n")

                print(f"🎮 Total de partidas jugadas: {partidas_jugadas}\n")

                if victorias:
                    print("🏆 VICTORIAS POR JUGADOR:")
                    for nombre, wins in sorted(victorias.items(), key=lambda x: x[1], reverse=True):
                        print(f"   {nombre}: {wins} victorias")
                    print()

                if puntuaciones_totales:
                    print("💰 PUNTUACIONES TOTALES ACUMULADAS:")
                    for nombre, puntos in sorted(puntuaciones_totales.items(), key=lambda x: x[1], reverse=True):
                        print(f"   {nombre}: {puntos} puntos")
                    print()

                input("Presiona ENTER para volver al menú principal...")
                continue

        elif opcion == "2":
            print("Reglas próximamente.")
            input("ENTER...")
        elif opcion == "3":
            print("Créditos próximamente.")
            input("ENTER...")
        elif opcion == "4":
            print("Demo próximamente.")
            input("ENTER...")
        elif opcion == "5":
            # Mostrar resumen antes de salir
            if partidas_jugadas > 0:
                limpiar_pantalla()
                imprimir_titulo()
                print("\n" + "=" * 40)
                print("      📈 RESUMEN FINAL DE PARTIDAS")
                print("=" * 40 + "\n")

                print(f"🎮 Total de partidas jugadas: {partidas_jugadas}\n")

                if victorias:
                    print("🏆 VICTORIAS POR JUGADOR:")
                    for nombre, wins in sorted(victorias.items(), key=lambda x: x[1], reverse=True):
                        print(f"   {nombre}: {wins} victorias")
                    print()

                if puntuaciones_totales:
                    print("💰 PUNTUACIONES TOTALES ACUMULADAS:")
                    for nombre, puntos in sorted(puntuaciones_totales.items(), key=lambda x: x[1], reverse=True):
                        print(f"   {nombre}: {puntos} puntos")
                    print()

                input("Presiona ENTER para salir...")
            break
        else:
            print("Opción no válida.")
            input("ENTER...")


if __name__ == "__main__":
    menu_principal_loop()
