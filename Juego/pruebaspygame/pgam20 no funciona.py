
import pygame,sys


from pygame.locals import *


from random import randit

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
        miProyectil=Proyectil(x,y,"Imagenes/disparoa.jpg", True)
        self.listaDisparo.append(miProyectil)
        
    def dibujar(self,superficie):
        superficie.blit(self.ImagenNave, self.rect)


class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy, ruta, personaje):
        pygame.sprite.Sprite.__init__(self)

        self.imageProyectil=pygame.image.load(ruta)

        self.rect=self.imageProyectil.get_rect()

        self.velocidadDisparo=5
        self.rect.top=posy
        self.rect.left=posx

        self.disparoPersonaje=personaje
        
    def trayectoria(self):
        if self.disparoPersonaje==True:
             self.rect.top=self.rect.top - self.velocidadDisparo                              
        else:
            self.rect.top=self.rect.top + self.velocidadDisparo

            
    def dibujar(self,superficie):
        superficie.blit(self.imageProyectil, self.rect)



class Invasor(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.imagenA=pygame.image.load('Imagenes/MarcianoA.jpg')
        self.imagenB=pygame.image.load('Imagenes/MarcianoB.jpg')

        self.listaImagenes=[self.imagenA,self.imagenB]
        self.posImagen=0


        self.imagenInvasor=self.listaImagenes[self.posImagen]                              
        self.rect=self.imagenInvasor.get_rect()

        self.listaDisparo=[]
        self.velocidad=20
        self.rect.top=posy
        self.rect.left=posx


        self.rangoDisparo=5                     
        self.tiempoCambio=1
                                       
    def dibujar(self,superficie):
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor, self.rect)

    def comportamiento(self,tiempo):
         self.__ataque()   
        if (self.tiempoCambio==tiempo):
            self.posImagen+=1
            self.tiempoCambio+=1
                                       
            if self.posImagen > len(self.listaImagenes)-1:
                self.posImagen=0


    def __ataque(self):
        if(randit(0,100)<self.rangoDisparo):
            self.__disparo()
            
    def __disparo(self):
        x,y=self.rect.center
        miProyectil=Proyectil(x,y,"Imagenes/disparob.jpg", False)
        self.listaDisparo.append(miProyectil)


                                       
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

        
        tiempo=pygame.time.get_ticks()/1000
        
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
        
        enemigo.comportamiento(tiempo)
        
        jugador.dibujar(ventana)
        enemigo.dibujar(ventana)
        
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top <-10:
                    jugador.listaDisparo.remove(x)

         if len(enemigo.listaDisparo)>0:
            for x in enemigo.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top >900:
                    enemigo.listaDisparo.remove(x)    

                    
        pygame.display.update()

SpaceInvader()
    



















