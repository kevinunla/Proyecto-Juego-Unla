import pygame,sys

from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((700,500))
pygame.display.set_caption("Hola Mundo")

"""
No te olvides de poner una imagen en esa carpeta
q debe estan en el mismo directorio q el archivo.py
"""

Mi_imagen = pygame.image.load("Imagenes/Ovni.png")
posX=200
posY=100





velocidad=2
Blanco=(255,255,255)
while True:
    ventana.fill(Blanco)
    ventana.blit(Mi_imagen,(posX,posY))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    if posX<400:
        posX+=velocidad
    else:
        posX-=velocidad
        
    pygame.display.update()
    















