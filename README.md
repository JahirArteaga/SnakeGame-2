# SnakeGame-2
# Proyecto: Juego de la Serpiente - Paso 2 Functional

Este repositorio contiene el código actualizado y completo del videojuego Snake, estructurado bajo el patrón arquitectónico Modelo-Vista-Controlador (MVC) y Programación Orientada a Objetos.

*   **Estudiante:** Jahir Arteaga
*   **Institución:** Universidad Internacional del Ecuador (UIDE)
*   **Carrera:** Ingeniería en Inteligencia Artificial

## Estructura de Responsabilidades Implementadas (MVC)
*   **Modelo (`src/modelo.py`)**: Almacena y procesa la estructura matemática pura (coordenadas del cuerpo, posición de la comida y puntaje). No posee componentes gráficos.
*   **Vista (`src/vista.py`)**: Renderiza los elementos visuales en pantalla: pinta el fondo, la serpiente en color verde, la comida en color rojo y despliega los textos de Game Over.
*   **Controlador (`src/controlador.py`)**: Detecta las teclas físicas (Inputs), gobierna el Game Loop continuo y ordena actualizar las coordenadas físicas al modelo.

## Pensamiento Innovador y Transformación Basada en Conocimiento
*   **Pensamiento Innovador**: Se implementó una abstracción de entrada dinámica agnóstica exponiendo públicamente el método de dirección. Esto supera los límites tradicionales del juego permitiendo acoplar hilos concurrentes o agentes autónomos de Inteligencia Artificial en el mismo entorno cerrado.
*   **Vinculación y Transformación**: Este software logra vincular y transformar teorías abstractas del álgebra lineal, estructuras de datos (pilas y listas indexadas para el crecimiento) y patrones de diseño en un producto interactivo unificado.
