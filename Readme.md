🃏 Chinchón Python — Versión Extendida con Comodines de Cerveza 🍺
Bienvenido al proyecto Chinchón Python, una implementación completa del clásico juego de cartas español, ampliado con una mecánica original y divertida: los 4 Comodines de Cerveza.
El objetivo es recrear el juego con fidelidad, añadir nuevas dinámicas estratégicas y practicar buenas prácticas de desarrollo con Python, Git y asistencia de IA.

🎯 Objetivos del Proyecto
Modelar un juego de cartas usando estructuras de datos en Python.

Implementar la lógica completa del Chinchón: turnos, combinaciones, cierre y puntuación.

Añadir una mecánica original de comodines con efectos especiales.

Practicar Git con commits incrementales y desarrollo modular.

Aprender a usar IA para generar, analizar y mejorar código.

Crear una interfaz de usuario clara en terminal.

Documentar el proceso de asistencia de IA de forma profesional.

🎴 Reglas del Chinchón
🂠 Baraja
Baraja española de 40 cartas (1–7 y 10–12 en 4 palos).

Se añaden 4 comodines especiales.

👥 Jugadores
De 2 a 4 jugadores.

🃏 Mano inicial
Cada jugador recibe 7 cartas.

🔄 Turno
Robar una carta del mazo o del descarte.

Añadirla a la mano.

Descartar una carta.

Opcionalmente, cerrar si se tienen combinaciones válidas.

🧩 Combinaciones válidas
Escalera: 3+ cartas consecutivas del mismo palo.

Grupo: 3+ cartas del mismo valor.

Los comodines pueden completar combinaciones.

🃓 Chinchón
Cerrar con las 7 cartas formando una única combinación.

Otorga –10 puntos.

🧮 Puntuación
Al cerrar, cada jugador suma el valor de las cartas que no pudo combinar.

Valores:

1–7 → su valor

10–12 → 10 puntos

Comodín → 25 puntos (si no se usa como comodín especial)

💀 Eliminación
Un jugador queda eliminado al alcanzar 100 puntos o más.

El último jugador no eliminado gana.

🍺 Mecánica Especial: Los 4 Comodines de Cerveza
Cuando un jugador roba un comodín, se activa un evento especial.
Cada comodín solo puede usarse una vez por partida.
Si se descarta sin usar, desaparece del juego.

Nº	Cerveza	Efecto	Condición	Resultado
1	Estrella Galicia	Salva la eliminación	Exactamente 100 pts	Baja a 80 pts
2	Alhambra Verde	Reduce puntos a la mitad	50 pts o más	Baja a 25 pts
3	Estrella 1906	Borra los últimos 25 puntos	25 pts o más	–25 pts (mín. 0)
4	SIN CERVEZA	Eliminación inmediata	Siempre	ELIMINADO
📝 Regla adicional
Al final de la partida:

Por cada comodín no usado, el ganador recibe –5 puntos. 