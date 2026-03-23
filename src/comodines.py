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
        escribir(f"¡COMODÍN ACTIVADO: Estrella Galicia! 🍺", colores["verde"])
        if jugador.puntos == 100:
            jugador.puntos = 80
            escribir(f"{jugador.nombre} tenía 100 puntos y baja a 80. ¡Salvado!", colores["amarillo"])
        else:
            escribir(f"{jugador.nombre} no tenía 100 puntos. El comodín no tiene efecto.", colores["cian"])

        # El comodín desaparece
        if hasattr(jugador, "mano") and carta in jugador.mano:
            jugador.mano.remove(carta)
        return

    # ============================================================
    # 2. ALHAMBRA VERDE — Reduce a 25 si tienes 50 o más
    # ============================================================
    if nombre == "alhambra_verde":
        escribir(f"¡COMODÍN ACTIVADO: Alhambra Verde! 🍀", colores["verde"])
        if jugador.puntos >= 50:
            jugador.puntos = 25
            escribir(f"{jugador.nombre} tenía {jugador.puntos + 25 if jugador.puntos == 25 else '50 o más'} puntos y baja a 25.", colores["amarillo"])
        else:
            escribir(f"{jugador.nombre} tenía menos de 50 puntos. El comodín no tiene efecto.", colores["cian"])

        # El comodín desaparece
        if hasattr(jugador, "mano") and carta in jugador.mano:
            jugador.mano.remove(carta)
        return

    # ============================================================
    # 3. ESTRELLA 1906 — Resta 25 puntos (mínimo 0)
    # ============================================================
    if nombre == "estrella_1906":
        escribir(f"¡COMODÍN ACTIVADO: Estrella 1906! ⭐", colores["verde"])
        puntos_antes = jugador.puntos
        jugador.puntos = max(0, jugador.puntos - 25)
        puntos_despues = jugador.puntos
        if puntos_antes > 0:
            escribir(f"{jugador.nombre} pierde 25 puntos: {puntos_antes} → {puntos_despues}", colores["amarillo"])
        else:
            escribir(f"{jugador.nombre} ya tenía 0 puntos. No se puede restar más.", colores["cian"])

        # El comodín desaparece
        if hasattr(jugador, "mano") and carta in jugador.mano:
            jugador.mano.remove(carta)
        return

    # ============================================================
    # 4. SIN CERVEZA — Eliminación inmediata
    # ============================================================
    if nombre == "sin_cerveza":
        escribir(f"¡COMODÍN ACTIVADO: SIN CERVEZA! ☠️", colores["verde"])
        jugador.eliminado = True
        escribir(f"{jugador.nombre} ha sido ELIMINADO del juego!", colores["rojo"])

        # El comodín desaparece
        if hasattr(jugador, "mano") and carta in jugador.mano:
            jugador.mano.remove(carta)
        return

    # ============================================================
    # Si llega aquí, el comodín no existe o no tiene efecto
    # ============================================================
    if hasattr(jugador, "mano") and carta in jugador.mano:
        jugador.mano.remove(carta)
