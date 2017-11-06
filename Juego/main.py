
import pygame as pg

#importa la libreria de pygame con el nombre de pg
from settings import *

class Juego:
    def __init__(self):
        #inicializa la pantalla del juego,etc
        pg.init()
        pg.font.init()
        self.corriendo = True
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption(TITULO)
        self.reloj = pg.time.Clock()




        pass

    def new (self):
        #reinicializa las variables del juego
        todosLosSprites = pg.sprite.Group()


    def run(self):
        #bucle del juego
        self.jugando = True
        while jugando:
            self.reloj.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #bucle de juego - actualizaciones de la logica del juego
        self.todosLosSprites.update()

    def events(self):
        #bucle de juego - eventos
        for event in pygame.event.get():

            if event.type == pygame.QUIT: #si clickeo en la X se cierra la ventana
                if self.jugando:
                    self.jugando = False
                self.corriendo = False

    def draw(self):
        #bucle de juego - dibuja
        #maneja la parte grafica del juego
        self.pantalla.fill(gris1)
        self.todosLosSprites.draw(self.pantalla)
        pg.pantalla.flip()

    def mostrarPantallaInicio(self):
        #pantalla de incio / menu inicio
        self.pantalla.fill(GRIS1)
        self.drawTexto("Iniciar", 40, GRIS2, ANCHO/2, (ALTO/8)*2)
        self.drawTexto("Puntuaciones", 40, GRIS2, ANCHO/2, (ALTO/8)*4)
        self.drawTexto("Ayuda", 40, GRIS2, ANCHO/2, (ALTO/2)*6)
        self.drawTexto("Salir", 40,  GRIS2, ANCHO/2, (ALTO/2)*8)


    def mostrarPantallaFin(self):
        #pantalla cuando muere el personaje
        pass

    def drawTexto(self, string, tamanio, color, x, y):
        nombreFuente = pg.font.match_font("DemoFont")
        fuenteMenu = pg.font.Font( nombreFuente, tamanio)
        superficieTexto = fuenteMenu.render(string, 1, color)
        textoRect = superficieTexto.get_rect()
        textoRect.midtop = (x, y)
        self.pantalla.blit(superficieTexto, textoRect)

#---------------------------------------------------------------------
#ejecucion.....


g = Juego()
g.mostrarPantallaInicio()

while g.corriendo:
    g.new()
    g.run()
    g.mostrarPantallaFin()

pg.quit()
