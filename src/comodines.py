# src/comodines.py

# ============================================================
# ACTIVAR COMODÍN SEGÚN LAS REGLAS OFICIALES DEL CHINCHÓN 🍺
# ============================================================

def activar_comodin(jugador, carta, limpiar, escribir, colores):
    """
    Aplica el efecto del comodín según su nombre.
    Los comodines se usan inmediatamente al robarlos.
    Después de usarse, desaparecen del juego.
    """

    # Si la carta no tiene nombre (comodín del mazo), no fallar
    nombre = getattr(carta, "nombre", None)
    if not nombre:
        return

    nombre = nombre.lower()

    # ============================================================
    # 1. ESTRELLA GALICIA — Salva eliminación (exactamente 100 → baja a 80)
    # ============================================================
    if nombre == "estrella_galicia":
        if jugador.puntos == 100:
            jugador.puntos = 80

        # El comodín desaparece
        if hasattr(jugador, "mano") and carta in jugador.mano:
            jugador.mano.remove(carta)
        return

    # ============================================================
    # 2. ALHAMBRA VERDE — Reduce a 25 si tienes 50 o más
    # ============================================================
    if nombre == "alhambra_verde":
        if jugador.puntos >= 50:
            jugador.puntos = 25

        # El comodín desaparece
        if hasattr(jugador, "mano") and carta in jugador.mano:
            jugador.mano.remove(carta)
        return

    # ============================================================
    # 3. ESTRELLA 1906 — Resta 25 puntos (mínimo 0)
    # ============================================================
    if nombre == "estrella_1906":
        jugador.puntos = max(0, jugador.puntos - 25)

        # El comodín desaparece
        if hasattr(jugador, "mano") and carta in jugador.mano:
            jugador.mano.remove(carta)
        return

    # ============================================================
    # 4. SIN CERVEZA — Eliminación inmediata
    # ============================================================
    if nombre == "sin_cerveza":
        jugador.eliminado = True

        # El comodín desaparece
        if hasattr(jugador, "mano") and carta in jugador.mano:
            jugador.mano.remove(carta)
        return

    # ============================================================
    # Si llega aquí, el comodín no existe o no tiene efecto
    # ============================================================
    if hasattr(jugador, "mano") and carta in jugador.mano:
        jugador.mano.remove(carta)
