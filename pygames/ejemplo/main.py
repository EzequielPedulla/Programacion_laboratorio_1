# importa el modulo pygames modulo -> mas chiquito biblioteca -> conjunto de modulos
import pygame

# pygame setup


pygame.init()  # inicia pygame

# definimos tamaño ventana

ANCHO_VENTANA = 800
ALTO_VENTANA = 600

screen = pygame.display.set_mode(
    (ANCHO_VENTANA, ALTO_VENTANA))  # se crea la ventana

# cargamos imagen fondo
img_fondo = pygame.image.load(
    r'pygames\recursos\dddd.jfif')  # carga imagen de fondo

# carga la imagen de la tabla
img_tabla = pygame.image.load(r'pygames\recursos\dddd.jfif')

# posicion tabla
pos_img_tabla_puntajes = ((ANCHO_VENTANA - img_tabla.get_width()) // 2, 20)

# crear texto

# elegir tipo de fuente y tamaño
fuente_titulo = pygame.font.Font('C:\\Windows\\Fonts\\arial.ttf', 50)

# se renderiza el texto y el color
txt_titulo = fuente_titulo.render('Puntajes', True, (255, 255, 255))

pos_txt_titulo = ((ANCHO_VENTANA - txt_titulo.get_width()) // 2, 20)


running = True

while running:
    # se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(img_fondo, (0, 0))  # carga la imagen

    # carga la imagen de la tabla
    # screen.blit(img_tabla - pos_img_tabla_puntajes)

    screen.blit(txt_titulo, pos_txt_titulo)
    # muestra los cambios en pantalla
    pygame.display.flip()


pygame.quit()
