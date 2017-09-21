
import pygame,sys

from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola Mundo")



miFuente=pygame.font.Font(None,30)
miTexto=miFuente.render("prueba fuente",0,(200,60,80))




while True:
   
  
        
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

   
       
    ventana.blit(miTexto,(100,100))    
    pygame.display.update()
    











