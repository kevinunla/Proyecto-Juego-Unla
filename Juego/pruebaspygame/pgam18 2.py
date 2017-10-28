
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

        
    def movimientoDerecha(self):
        self.rect.right += self.velocidad
        self.__movimiento()

    def movimientoIzquierda(self):
        self.rect.left -= self.velocidad
        self.__movimiento()


    def __movimiento(self):
        if self.Vida==True:
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>870:
                self.rect.right=840
    
    def disparar(self,x,y):
        miProyectil=Proyectil(x,y)
        self.listaDisparo.append(miProyectil)
        
    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave, self.rect)


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.imageProyectil=pygame.image.load('Imagenes/disparoa.jpg')

        self.rect=self.imageProyectil.get_rect()

        self.velocidadDisparo=5
        self.rect.top=posy
        self.rect.left=posx

    def trayectoria(self):
         self.rect.top=self.rect.top - self.velocidadDisparo                              

    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil, self.rect)



class Invasor(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.imagenA=pygame.image.load('Imagenes/MarcianoA.jpg')

        self.rect=self.imagenA.get_rect()

        self.listaDisparo=[]
        self.velocidad=20
        self.rect.top=posy
        self.rect.left=posx

                              

    def dibujar(self,superficie):
        superficie.blit(self.imagenA, self.rect)

    
def SpaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space invader")
    ImagenFondo=pygame.image.load('Imagenes/Fondo.jpg')

    jugador=naveEspacial()
    enemigo=Invasor(100,100)

    DemoProyectil= Proyectil(ancho/2, alto-30)
    

    enJuego=True

    reloj=pygame.time.Clock()
    
    while True:
        #jugador.movimiento()
        reloj.tick(60)

        
        
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if enJuego==True:
                if evento.type==pygame.KEYDOWN:
                    if evento.key==K_LEFT:
                            #resta velocidad
                        jugador.movimientoIzquierda()

                    elif evento.key==K_RIGHT:
                        jugador.movimientoDerecha()

                    #la "S" es para disparar
                    elif evento.key==K_s:
                        x,y=jugador.rect.center
                        jugador.disparar(x,y)

                
        ventana.blit(ImagenFondo,(0,0))
        
      
        
        jugador.dibujar(ventana)
        enemigo.dibujar(ventana)
        
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top <100:
                    jugador.listaDisparo.remove(x)
                    
                    
        pygame.display.update()

SpaceInvader()
    














































