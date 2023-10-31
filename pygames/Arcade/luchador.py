
import pygame


class Luchador():
    def __init__(self, x, y) -> None:

        self.rect = pygame.Rect((x, y, 80, 180))

    def mover(self, ancho_pantalla):

        velocidad = 10
        dx = 0
        dy = 0

        # se presiona con el teclado

        key = pygame.key.get_pressed()

        # controles movimiento

        if key[pygame.K_a]:  # comprueba si se toco la tecla a
            dx = -velocidad
        if key[pygame.K_d]:
            dx = velocidad  # comprueba si se toco la tecla a  d

        if self.rect.left + dx < 0:  # comprueba que no se vaya del borde izquierdo

            dx = 0 - self.rect.left

        if self.rect.right + dx > ancho_pantalla:  # cpmprueba que no se vaya del lado derecho

            dx = ancho_pantalla - self.rect.right

        # actualizar posicion del jugador

        self.rect.x += dx
        self.rect.y += dy

    def mostrar_luchador(self, superficie):
        pygame.draw.rect(superficie, (255, 0, 0), self.rect)
