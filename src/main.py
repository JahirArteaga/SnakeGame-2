import pygame
from modelo import SnakeModel
from vista import SnakeView
from controlador import SnakeController

def main():
    """Punto de entrada único de la aplicación estructurada."""
    pygame.init()
    
    ANCHO_VENTANA = 600
    ALTO_VENTANA = 600
    MEDIDA_CELDA = 20

    # Instanciación y acoplamiento limpio de las capas del software (POO)
    modelo = SnakeModel(ANCHO_VENTANA, ALTO_VENTANA, MEDIDA_CELDA)
    vista = SnakeView(ANCHO_VENTANA, ALTO_VENTANA)
    controlador = SnakeController(modelo, vista)

    # Inicializar el flujo operacional continuo
    controlador.ejecutar()

if __name__ == "__main__":
    main()
