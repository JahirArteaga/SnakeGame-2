import pygame
import sys

class SnakeController:
    """
    RESPONSABILIDAD: Cerebro y Puente. Detecta teclas (Inputs), gobierna el Game Loop 
    regulado por tics y ordena al modelo actualizar la posición lógica.
    """
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.reloj = pygame.time.Clock()
        self.fps = 10  # Velocidad o frecuencia constante de los tics temporales

    def ejecutar(self):
        ejecutando = True
        
        # BUCLE REPETITIVO (WHILE PRINCIPAL): Bucle de juego activo (Game Loop)
        while ejecutando:
            # Captura y detección de teclas físicas (Inputs del Jugador)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    ejecutando = False
                    
                elif evento.type == pygame.KEYDOWN:
                    # Estructuras condicionales para procesar comandos discretos de entrada
                    if not self.modelo.game_over:
                        if evento.key == pygame.K_UP:
                            self.modelo.cambiar_direccion((0, -self.modelo.tamano_celda))
                        elif evento.key == pygame.K_DOWN:
                            self.modelo.cambiar_direccion((0, self.modelo.tamano_celda))
                        elif evento.key == pygame.K_LEFT:
                            self.modelo.cambiar_direccion((-self.modelo.tamano_celda, 0))
                        elif evento.key == pygame.K_RIGHT:
                            self.modelo.cambiar_direccion((self.modelo.tamano_celda, 0))
                    else:
                        # Control secuencial de reinicio desde la interfaz de derrota
                        if evento.key == pygame.K_SPACE:
                            self.modelo.reiniciar_juego()

            # Conexión e instrucciones jerárquicas del patrón arquitectónico
            self.modelo.actualizar()  # Ordena actualizar coordenadas al Modelo
            self.vista.dibujar(self.modelo)  # Instruye a la vista refrescar el lienzo visual
            
            # Sincronización regulada por tics de tiempo
            self.reloj.tick(self.fps)

        pygame.quit()
        sys.exit()
