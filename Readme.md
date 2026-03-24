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

---

🚀 Cómo Ejecutar el Juego
1. Asegúrate de tener Python 3.8+ instalado.
2. Navega al directorio del proyecto:
   ```bash
   cd Chinchon
   ```
3. Ejecuta el juego:
   ```bash
   python src/ui.py
   ```
4. Sigue las instrucciones en el menú.

📦 Requisitos
- Python 3.8 o superior
- No se requieren paquetes externos (solo biblioteca estándar)

Para instalar dependencias (si las hubiera):
```bash
pip install -r requirements.txt
```

🧪 Testing
El proyecto incluye tests unitarios con pytest. Para ejecutarlos:

```bash
python -m pytest tests/ -v
```

Tests incluidos:
- `test_ambos_suman100.py`: Casos donde ambos jugadores superan 100 puntos
- `test_comodines.py`: Tests para los 4 comodines especiales

Todos los tests deben pasar ✅

📁 Estructura del Proyecto
```
Chinchon/
├── src/
│   ├── model/           # Entidades de datos (Carta, Baraja, Jugador)
│   ├── game/            # Lógica principal del juego (ChinchonGame)
│   ├── validation/      # Validación de manos y combinaciones
│   ├── effects/         # Comodines y animaciones
│   └── ui.py            # Interfaz de usuario (terminal)
├── tests/               # Tests unitarios
├── docs/                # Documentación adicional
│   ├── reglas.md
│   ├── resumen_basico.md
│   ├── puntuaciones_demo.md
│   └── creditos.md
├── requirements.txt
├── .gitignore
└── Readme.md

🔧 Desarrollo Modular
El proyecto está diseñado con una arquitectura modular:

- **Model**: Clases de datos independientes
- **Game**: Reglas y flujo del juego
- **Validation**: Lógica de combinaciones válidas
- **Effects**: Comodines y efectos visuales
- **UI**: Presentación y entrada de usuario

Esta separación facilita:
- Mantenimiento del código
- Testing unitario
- Futuras extensiones
- Colaboración en equipo

📝 Convenciones de Código
- Seguimos PEP 8 (estilo Python)
- Docstrings en todas las funciones y clases
- Funciones pequeñas y con responsabilidad única
- Nombres en snake_case para funciones/variables
- Nombres en PascalCase para clases

🤝 Contribuciones
¡Bienvenidas! Para contribuir:

1. Haz fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-feature`)
3. Commit tus cambios (`git commit -m 'Add: nueva feature'`)
4. Push a la rama (`git push origin feature/nueva-feature`)
5. Abre un Pull Request describiendo los cambios

Asegúrate de que todos los tests pasan antes de enviar PR.

📜 Licencia
Este proyecto es de código abierto. Siéntete libre de usarlo, modificarlo y compartirlo.

Atribuciones:
- Código creado por Ralfy8 con asistencia de IA
- Idea original por RusGar

📞 Contacto
Para preguntas, sugerencias o colaboraciones, contacta con el autor.

---

**¡Disfruta del juego de Chinchón con Comodines de Cerveza! 🍺🃏** 