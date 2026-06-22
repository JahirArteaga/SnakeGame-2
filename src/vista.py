import pygame

class SnakeView:
    """
    RESPONSABILIDAD: Interfaz Visual pura. Se encarga de renderizar fondo, textos, 
    pinta la serpiente en verde, la comida en rojo y despliega las pantallas de interfaz.
    """
    def __init__(self, ancho, alto):
        self.pantalla = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption("Snake Game - Patrón MVC (Jahir Arteaga)")
        
        # Paleta de colores RGB exacta solicitada en las responsabilidades del informe
        self.COLOR_FONDO = (18, 18, 18)
        self.COLOR_SERPIENTE = (46, 204, 113)  # Pinta la serpiente de color Verde
        self.COLOR_CABEZA = (39, 174, 96)     # Verde oscuro para la cabeza
        self.COLOR_COMIDA = (231, 76, 60)      # Pinta la comida de color Rojo
        self.COLOR_TEXTO = (236, 240, 241)
        
        pygame.font.init()
        self.fuente_score = pygame.font.SysFont("Helvetica", 22, bold=True)
        self.fuente_interfaz = pygame.font.SysFont("Helvetica", 42, bold=True)
        self.fuente_subtexto = pygame.font.SysFont("Helvetica", 20)

    def dibujar(self, modelo):
        # Renderiza el fondo limpio
        self.pantalla.fill(self.COLOR_FONDO)

        # Renderizado gráfico de la comida en color Rojo
        pygame.draw.rect(self.pantalla, self.COLOR_COMIDA, 
                         pygame.Rect(modelo.comida, modelo.comida, modelo.tamano_celda, modelo.tamano_celda))

        # BUCLE REPETITIVO (FOR): Renderiza secuencialmente cada segmento corporal en color Verde
        for indice, segmento in enumerate(modelo.cuerpo):
            color = self.COLOR_CABEZA if indice == 0 else self.COLOR_SERPIENTE
            pygame.draw.rect(self.pantalla, color, 
                             pygame.Rect(segmento, segmento, modelo.tamano_celda, modelo.tamano_celda))

        # Despliegue del texto y registro matemático de puntaje
        texto_score = self.fuente_score.render(f"PUNTOS: {modelo.puntaje}", True, self.COLOR_TEXTO)
        self.pantalla.blit(texto_score, (15, 15))

        # ESTRUCTURA CONDICIONAL: Despliegue de la pantalla de derrota (Relación Extend)
        if modelo.game_over:
            superficie_gameover = self.fuente_interfaz.render("GAME OVER", True, self.COLOR_COMIDA)
            superficie_reinicio = self.fuente_subtexto.render("Presiona [ESPACIO] para volver a jugar", True, self.COLOR_TEXTO)
            
            self.pantalla.blit(superficie_gameover, (modelo.ancho // 2 - 120, modelo.alto // 2 - 40))
            self.pantalla.blit(superficie_reinicio, (modelo.ancho // 2 - 160, modelo.alto // 2 + 20))

        pygame.display.update()
