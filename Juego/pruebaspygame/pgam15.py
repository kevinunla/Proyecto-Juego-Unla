
import pygame,sys

from pygame.locals import *

#variables globales
ancho=900
alto=480


class naveEspacial(pygame.sprite.Sprite):
    """Clase para las naves"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave=pygame.image.load('Imagenes/nave.jpg')

        self.rect=self.ImagenNave.get_rect()
        self.rect.centerx=ancho/2
        self.rect.centery=alto-30
        self.listaDisparo=[]
        self.Vida=True

        self.velocidad=20

    def movimiento(self):
        if self.Vida==True:
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>870:
                self.rect.right=840
    
    def disparar(self):
        pass
    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave, self.rect)
                
def SpaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space invader")
    ImagenFondo=pygame.image.load('Imagenes/Fondo.jpg')

    jugador=naveEspacial()

    enJuego=True
    while True:
        jugador.movimiento()
        
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if enJuego==True:
                if evento.type==pygame.KEYDOWN:
                    if evento.key==K_LEFT:
                            #resta velocidad
                        jugador.rect.left-=jugador.velocidad

                    if evento.key==K_RIGHT:
                        jugador.rect.right+=jugador.velocidad
                        
                
        ventana.blit(ImagenFondo,(0,0))
        jugador.dibujar(ventana)
        pygame.display.update()

SpaceInvader()
    














































