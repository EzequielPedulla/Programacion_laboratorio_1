import pygame
from luchador import Luchador

pygame.init()

ancho_pantalla = 1200

alto_pantalla = 800

pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

pygame.display.set_caption('Arcade')

clock = pygame.time.Clock()

# imagen del fondo

imagen_fondo = pygame.image.load(
    'arcade/assets/img/fondo.png').convert_alpha()


# para mostrar el fondo
def muestra_fondo():

    agrandar_imagen = pygame.transform.scale(
        imagen_fondo, (ancho_pantalla, alto_pantalla))
    pantalla.blit(agrandar_imagen, (0, 0))

# crea dos intancias de guerreros


luchador_1 = Luchador(400, 310)
luchador_2 = Luchador(700, 310)

# game loop

run = True

while run:

    clock.tick(60)
    # muestra el fondo
    muestra_fondo()

    # mover jugadores

    luchador_1.mover(ancho_pantalla)
    # luchador_2.mover()

    # muestra los jugadores
    luchador_1.mostrar_luchador(pantalla)
    luchador_2.mostrar_luchador(pantalla)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # actualizada la pantalla

    pygame.display.update()
# cerramos pygame
pygame.quit()
