# src/animaciones.py

def animacion_comodin_estrella_galicia(jugador, limpiar, escribir, colores):
    limpiar()
    escribir("🍺 COMODÍN #1: ESTRELLA GALICIA 🍺", colores["amarillo"])
    escribir(f"Una luz dorada envuelve a {jugador.nombre}...", colores["amarillo"])
    escribir("¡Sus puntos se fijan en 80!", colores["verde"])

def animacion_comodin_alhambra(jugador, limpiar, escribir, colores):
    limpiar()
    escribir("🍺 COMODÍN #2: ALHAMBRA VERDE 🍺", colores["verde"])
    escribir("Un aroma fresco a lúpulo aparece...", colores["verde"])
    escribir("¡Los puntos bajan a 25!", colores["cian"])

def animacion_comodin_1906(jugador, limpiar, escribir, colores):
    limpiar()
    escribir("🍺 COMODÍN #3: ESTRELLA 1906 🍺", colores["rojo"])
    escribir("La cerveza tostada libera su poder...", colores["rojo"])
    escribir("¡Se restan 25 puntos!", colores["amarillo"])

def animacion_comodin_muerte(jugador, limpiar, escribir, colores):
    limpiar()
    escribir("💀 COMODÍN #4: SIN CERVEZA 💀", colores["rojo"])
    escribir("El vaso está vacío...", colores["rojo"])
    escribir("La tristeza invade la mesa...", colores["magenta"])
    escribir(f">>> {jugador.nombre} ha sido ELIMINADO", colores["rojo"])

def mostrar_animacion_comodin(jugador, numero, limpiar, escribir, colores):
    if numero == 1:
        animacion_comodin_estrella_galicia(jugador, limpiar, escribir, colores)
    elif numero == 2:
        animacion_comodin_alhambra(jugador, limpiar, escribir, colores)
    elif numero == 3:
        animacion_comodin_1906(jugador, limpiar, escribir, colores)
    elif numero == 4:
        animacion_comodin_muerte(jugador, limpiar, escribir, colores)
