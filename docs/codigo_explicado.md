# Explicación del Código del Proyecto Chinchón

Este documento explica de manera simple el código de todos los archivos `.py` del proyecto Chinchón. El proyecto está organizado de forma modular, con cada función en su propio archivo para facilitar el mantenimiento.

## Estructura General

El proyecto está dividido en carpetas:
- `src/`: Código fuente principal
- `docs/`: Documentación
- `tests/`: Pruebas

## Módulos Principales

### 1. `src/ui.py`
Este archivo maneja la interfaz de usuario del juego.
- **Funciones principales**:
  - `menu_principal_loop()`: Bucle principal del menú
  - `iniciar_partida()`: Inicia una nueva partida
  - `imprimir_titulo()`, `imprimir_menu_principal()`: Funciones de visualización
  - `_bucle_partida()`: Maneja el flujo de una partida completa
- **Propósito**: Gestiona la interacción con el usuario, muestra menús y controla el flujo del juego.

### 2. `src/game/chinchon.py`
Contiene la clase principal del juego Chinchón.
- **Clase `ChinchonGame`**:
  - `__init__()`: Inicializa el juego con jugadores
  - `jugar_turno()`: Ejecuta un turno completo
  - `_robar_carta()`, `_procesar_comodin()`: Lógica de robo y comodines
  - `_cerrar_ronda()`, `detectar_ganador()`: Fin de ronda y victoria
- **Propósito**: Implementa la lógica central del juego, turnos y reglas.

### 3. `src/model/carta.py`
Define las clases para cartas y baraja.
- **Clase `Carta`**:
  - `__init__()`: Crea una carta con palo, valor y tipo
  - `__repr__()`: Representación en texto de la carta
- **Clase `Baraja`**:
  - `__init__()`: Crea la baraja española con 40 cartas + 4 comodines
  - `barajar()`, `robar()`, `repartir()`: Operaciones con la baraja
- **Propósito**: Modela las cartas y la baraja del juego.

### 4. `src/model/jugador.py`
Define la clase Jugador.
- **Clase `Jugador`**:
  - `__init__()`: Inicializa con nombre y atributos
  - `recibir_cartas()`, `robar_carta()`, `descartar()`: Gestión de mano
  - `sumar_puntos_ronda()`, `fijar_puntos()`, `restar_puntos()`: Gestión de puntuación
- **Propósito**: Representa a un jugador con su mano, puntos y estado.

### 5. `src/validation/validador.py`
Contiene funciones para validar manos de cartas.
- **Funciones principales**:
  - `detectar_escaleras()`: Encuentra escaleras (secuencias consecutivas)
  - `detectar_grupos()`: Encuentra grupos (mismo valor)
  - `es_chinchon()`: Verifica si es Chinchón (escalera completa)
  - `_filtrar_normales()`: Separa cartas normales de comodines
- **Propósito**: Valida si una mano cumple las reglas del juego.

### 6. `src/effects/comodines.py`
Maneja los efectos de los comodines especiales.
- **Función principal**:
  - `activar_comodin()`: Aplica el efecto del comodín según su tipo
- **Propósito**: Implementa las reglas especiales de los comodines (Estrella Galicia, Alhambra Verde, etc.).

### 7. `src/animaciones.py` (en effects/)
Funciones para animaciones visuales.
- **Funciones principales**:
  - `animar_texto()`: Muestra texto con efecto de animación
- **Propósito**: Mejora la experiencia visual del usuario.

## Módulos Funcionales (Carpetas `_funcs/`)

Para mantener el código ultra-modular, cada función de los módulos principales ha sido extraída a su propio archivo en carpetas `_funcs/`. Esto permite modificar o probar cada función individualmente.

### `src/game/chinchon_funcs/`
Contiene funciones del juego Chinchón (17 archivos):
- `jugar_turno.py`: Lógica completa de un turno
- `iniciar_nueva_ronda.py`: Configuración inicial de ronda
- `robar_carta.py`: Proceso de robo de cartas
- `procesar_comodin.py`: Manejo de comodines
- `avisar_mano_valida.py`: Notificación de validez de mano
- `preguntar_cierre.py`: Pregunta para cerrar ronda (solo acepta ENTER o S/s)
- `procesar_descarte.py`: Gestión de descartes
- `avanzar_turno.py`: Cambio de turno
- `elegir_descartar.py`: Selección de carta a descartar
- `mostrar_resumen_ronda.py`: Visualización de resumen
- `calcular_y_mostrar_puntuaciones.py`: Cálculo de puntos
- `cerrar_ronda.py`: Proceso de cierre de ronda, incluyendo penalización por comodines no usados
- `mano_valida.py`: Validación de mano
- `formatear_carta.py`: Formateo de representación de carta
- `calcular_puntos_jugador.py`: Cálculo de puntos por jugador
- `procesar_eliminaciones_y_ganador.py`: Eliminación y detección de ganador
- `detectar_ganador.py`: Verificación de ganador
- `aplicar_penalizacion_comodines_no_usados.py`: Penalización por comodines no usados al ganador

### `src/model/carta_funcs/`
Funciones de cartas y baraja (6 archivos):
- `asignar_nombre_comodin.py`: Asigna nombre a comodines
- `formatear_carta_repr.py`: Formatea representación de carta
- `crear_baraja.py`: Crea la baraja
- `barajar.py`: Baraja las cartas
- `robar.py`: Roba una carta
- `repartir.py`: Reparte cartas a jugadores

### `src/model/jugador_funcs/`
Funciones de jugador (7 archivos):
- `inicializar_jugador.py`: Inicializa atributos
- `recibir_cartas.py`: Asigna cartas a mano
- `robar_carta.py`: Añade carta a mano
- `descartar.py`: Remueve carta de mano
- `sumar_puntos_ronda.py`: Suma puntos y verifica eliminación
- `fijar_puntos.py`: Fija puntos y verifica eliminación
- `restar_puntos.py`: Resta puntos

### `src/validation/validador_funcs/`
Funciones de validación (4 archivos):
- `filtrar_normales.py`: Filtra cartas normales
- `detectar_escaleras.py`: Detecta escaleras
- `detectar_grupos.py`: Detecta grupos
- `es_chinchon.py`: Verifica Chinchón

## Archivos de Pruebas (`tests/`)

- `test_ambos_suman100.py`: Pruebas de eliminación cuando ambos superan 100 puntos
- `test_partida_edge.py`: Pruebas de casos edge (mazo vacío, un solo jugador)
- `test_comodines.py`: Pruebas de efectos de comodines

## Conclusión

El proyecto Chinchón está diseñado con una arquitectura modular extrema, donde cada función tiene su propio archivo. Esto facilita:
- **Mantenimiento**: Cambios localizados
- **Pruebas**: Cada función se puede probar individualmente
- **Legibilidad**: Código simple y enfocado
- **Reutilización**: Funciones independientes

Todos los módulos principales actúan como "orquestadores" que llaman a las funciones modulares, manteniendo la compatibilidad con el resto del código.