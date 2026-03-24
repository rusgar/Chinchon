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

    # Asegurar ancho fijo de 9 caracteres entre los bordes
    # Línea 1: valor a la izquierda (3 chars) + 6 espacios
    # Línea 2: 4 espacios + palo (1-2 chars) + 4-3 espacios (para centrar)
    # Línea 3: 7 espacios + valor a la derecha (3 chars)

    # Para emojis que ocupan 2 caracteres, necesitamos ajustar el centrado
    palo_str = str(palo)
    palo_len = len(palo_str.encode('utf-8'))  # Considerar ancho en bytes para emojis

    # Estrategia: usar ancho fijo de 9 caracteres entre bordes
    # Posiciones: [0] borde, [1-9] contenido, [10] borde
    # Queremos:
    # - valor izq en pos 1-3 (3 chars)
    # - palo centrado en pos 4-6 (3 chars de ancho visual)
    # - valor der en pos 7-9 (3 chars)

    # Para emojis de 2 chars de ancho, los centramos con 3 espacios total (2+1=3)
    # Para símbolos de 1 char, los centramos con 4 espacios total (1+3=4)

    # Calcular espacios para centrar el palo en 9 caracteres
    palo_ancho = 2 if carta.tipo == "comodin" else 1
    espacios_izq = (9 - palo_ancho) // 2
    espacios_der = 9 - palo_ancho - espacios_izq

    return [
        "┌─────────┐",
        f"│{valor.ljust(3)}       │",           # valor izq (3) + 6 espacios = 9
        f"│{' ' * espacios_izq}{palo_str}{' ' * espacios_der}│",  # palo centrado
        f"│      {valor.rjust(3)}│",            # 6 espacios + valor der (3) = 9
        "└─────────┘",
    ]


def mostrar_mano(jugador):
    """Muestra las cartas del jugador en formato ASCII."""
    ascii_cartas = [carta_a_ascii(c) for c in jugador.mano]
    for i in range(5):
        print("  ".join(c[i] for c in ascii_cartas))
    print()


def _recoger_nombres_jugadores():
    """Recoge los nombres de los jugadores desde la consola."""
    print("Introduce los nombres de los jugadores.\n")
    nombres = []

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
        return None

    return nombres


def _bucle_partida(juego):
    """Ejecuta el bucle principal de la partida y devuelve (ganador, orden_eliminacion)."""
    orden_eliminacion = []  # [(nombre, puntos), ...]

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

        # Detectar jugadores eliminados en este turno y registrarlos
        for j in juego.todos_jugadores:
            if j.eliminado and j.nombre not in [e[0] for e in orden_eliminacion]:
                orden_eliminacion.append((j.nombre, j.puntos))

        if resultado == "cerrado":
            ganador = juego.detectar_ganador()
            if ganador:
                return ganador, orden_eliminacion
            juego._iniciar_nueva_ronda()
            continue

        ganador = juego.detectar_ganador()
        if ganador:
            return ganador, orden_eliminacion

    return None, orden_eliminacion


def _mostrar_resumen_final(ganador, orden_eliminacion):
    """Muestra el resumen final de la partida."""
    limpiar_pantalla()
    imprimir_titulo()
    escribir("\n" + "=" * 40, COLORES["cian"])
    escribir("      🏆 FIN DE LA PARTIDA 🏆", COLORES["amarillo"])
    print("=" * 40 + "\n")

    if ganador:
        escribir(f"🏅 GANADOR: {ganador.nombre} con {ganador.puntos} puntos", COLORES["verde"])
    else:
        escribir("❌ La partida ha terminado sin un ganador claro.", COLORES["rojo"])

    if orden_eliminacion:
        escribir("\n📋 ORDEN DE ELIMINACIÓN:", COLORES["cian"])
        for i, (nombre, puntos) in enumerate(orden_eliminacion, 1):
            escribir(f"  {i}º. {nombre} - {puntos} puntos", COLORES["reset"])

    input("\nPresiona ENTER para continuar...")


def iniciar_partida():
    """Función principal para iniciar y ejecutar una partida completa."""
    from game.chinchon import ChinchonGame

    limpiar_pantalla()
    imprimir_titulo()

    nombres = _recoger_nombres_jugadores()
    if nombres is None:
        return None, None

    juego = ChinchonGame(nombres, limpiar_pantalla, escribir, COLORES)
    ganador, orden_eliminacion = _bucle_partida(juego)
    _mostrar_resumen_final(ganador, orden_eliminacion)

    return ganador, juego.todos_jugadores


def _mostrar_estadisticas(partidas_jugadas, victorias):
    """Muestra las estadísticas actuales en el menú."""
    print("📊 ESTADÍSTICAS:")
    print(f"   Partidas jugadas: {partidas_jugadas}")
    for nombre, wins in sorted(victorias.items(), key=lambda x: x[1], reverse=True):
        print(f"   {nombre}: {wins} victorias")
    print()


def _mostrar_resumen_final_partidas(partidas_jugadas, victorias, puntuaciones_totales):
    """Muestra el resumen final de todas las partidas jugadas."""
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


def _mostrar_archivo_documentacion(ruta_archivo):
    """Muestra el contenido de un archivo de documentación."""
    limpiar_pantalla()
    imprimir_titulo()
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        print(contenido)
    except FileNotFoundError:
        escribir(f"❌ No se encontró el archivo: {ruta_archivo}", COLORES["rojo"])
    input("\nPresiona ENTER para volver al menú principal...")


def _preguntar_jugar_otra_partida():
    """Pregunta al usuario si quiere jugar otra partida. Devuelve True si sí."""
    limpiar_pantalla()
    print("¿Jugar otra partida?")
    print("1. Sí")
    print("2. No (ver resumen y salir)")
    opcion = input("Selecciona: ").strip()
    return opcion == "1"


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
            _mostrar_estadisticas(partidas_jugadas, victorias)

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
            if _preguntar_jugar_otra_partida():
                continue
            else:
                # Mostrar resumen completo
                _mostrar_resumen_final_partidas(partidas_jugadas, victorias, puntuaciones_totales)
                break

        elif opcion == "2":
            _mostrar_archivo_documentacion("docs/resumen_basico.md")
        elif opcion == "3":
            _mostrar_archivo_documentacion("docs/creditos.md")
        elif opcion == "4":
            _mostrar_archivo_documentacion("docs/puntuaciones_demo.md")
        elif opcion == "5":
            # Mostrar resumen antes de salir
            if partidas_jugadas > 0:
                _mostrar_resumen_final_partidas(partidas_jugadas, victorias, puntuaciones_totales)
            break
        else:
            print("Opción no válida.")
            input("ENTER...")


if __name__ == "__main__":
    menu_principal_loop()
