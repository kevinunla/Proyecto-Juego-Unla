import pygame,sys

from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((600,300))
pygame.display.set_caption("Hola Mundo")

"""
No te olvides de poner una imagen en esa carpeta
q debe estan en el mismo directorio q el archivo.py
"""

Mi_imagen = pygame.image.load("Imagenes/Ovni.png")
posX=200
posY=100





velocidad=5
Blanco=(255,255,255)
derecha=True

while True:
    ventana.fill(Blanco)
    ventana.blit(Mi_imagen,(posX,posY))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key==K_LEFT:
                posX-=velocidad
            elif event.key==K_RIGHT:
                posX+=velocidad
        elif event.type == pygame.KEYUP:
            if event.key==K_LEFT:
                print ("Tecla Izquierda Liberada")
            elif event.key==K_RIGHT:
                print ("Tecla Derecha Liberada")
    
       
    posX,posY= pygame.mouse.get_pos()
    posX= posX-100
    posY= posY-50
    pygame.display.update()
    















