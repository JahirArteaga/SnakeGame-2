import random

class SnakeModel:
    """
    RESPONSABILIDAD: Almacena la estructura matemática cruda, coordenadas del 
    cuerpo, comida, registro de puntaje y el estado binario del juego. Cero componentes gráficos.
    """
    def __init__(self, ancho, alto, tamano_celda=20):
        self.ancho = ancho
        self.alto = alto
        self.tamano_celda = tamano_celda
        self.reiniciar_juego()

    def reiniciar_juego(self):
        # Gestión de estado dinámico: Inicialización matemática de posiciones
        self.cuerpo = [(self.ancho // 2, self.alto // 2)]
        self.direccion = (0, -self.tamano_celda)  # Inicia moviéndose hacia arriba
        self.puntaje = 0
        self.game_over = False
        self.generar_comida()

    def generar_comida(self):
        while True:
            # Generación aleatoria de consumibles alineada a la cuadrícula cartográfica
            x = random.randint(0, (self.ancho - self.tamano_celda) // self.tamano_celda) * self.tamano_celda
            y = random.randint(0, (self.alto - self.tamano_celda) // self.tamano_celda) * self.tamano_celda
            self.comida = (x, y)
            # Condicional: Evitar colisión de aparición sobre el cuerpo de la serpiente
            if self.comida not in self.cuerpo:
                break

    def cambiar_direccion(self, nueva_direccion):
        """ REGLA DE NEGOCIO EXPLÍCITA: Bloquea giros inversos de 180 grados """
        if (nueva_direccion + self.direccion != 0) or (nueva_direccion + self.direccion != 0):
            self.direccion = nueva_direccion

    def actualizar(self):
        if self.game_over:
            return

        # Aritmética vectorial manual para calcular la trayectoria de la cabeza
        cabeza_actual = self.cuerpo
        nueva_cabeza = (cabeza_actual + self.direccion, cabeza_actual + self.direccion)

        # ESTRUCTURA CONDICIONAL 1: Algoritmia de detección de colisión con los bordes (Paredes)
        if (nueva_cabeza < 0 or nueva_cabeza >= self.ancho or 
            nueva_cabeza < 0 or nueva_cabeza >= self.alto):
            self.game_over = True
            return

        # ESTRUCTURA CONDICIONAL 2: Algoritmia de detección de colisión con su propio cuerpo
        if nueva_cabeza in self.cuerpo:
            self.game_over = True
            return

        # Transformación estructural: Insertar nuevo segmento en la cabeza de la lista
        self.cuerpo.insert(0, nueva_cabeza)

        # ESTRUCTURA CONDICIONAL 3: Intersección con el consumible comida (Relación Include)
        if nueva_cabeza == self.comida:
            self.puntaje += 1  # Incrementar puntaje matemático
            self.generar_comida()
        else:
            # Si no come, remueve el último elemento para simular desplazamiento cinemático continuo
            self.cuerpo.pop()
