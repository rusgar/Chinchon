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
    valor = "JOK" if carta.tipo == "comodin" else str(carta.valor)
    palo = "★" if carta.tipo == "comodin" else SIMBOLOS_PALOS[carta.palo]

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
        return

    # Crear partida
    juego = ChinchonGame(nombres, limpiar_pantalla, escribir, COLORES)

    # Bucle de toda la partida
    while True:
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
                print(f"\n¡{ganador.nombre} ha ganado la partida!")
                input("ENTER...")
                return

            # Reiniciar ronda SIN perder puntos
            juego._iniciar_nueva_ronda()
            continue

        ganador = juego.detectar_ganador()
        if ganador:
            print(f"\n¡{ganador.nombre} ha ganado la partida!")
            input("ENTER...")
            return


def menu_principal_loop():
    while True:
        limpiar_pantalla()
        imprimir_menu_principal()
        opcion = leer_opcion()

        if opcion == "1":
            iniciar_partida()
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
            break
        else:
            print("Opción no válida.")
            input("ENTER...")


if __name__ == "__main__":
    menu_principal_loop()
