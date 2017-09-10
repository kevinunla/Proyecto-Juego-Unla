import pygame,sys

from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola Mundo")
"""
No te olvides de poner una imagen en esa carpeta
q debe estan en el mismo directorio q el archivo.py
"""
Mi_imagen = pygame.image.load("Imagenes/Ovni.png")
posX,posY=130,70

"""
posX=130
posY=70
"""

ventana.blit(Mi_imagen,(posX,posY))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
