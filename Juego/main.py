
import pygame as pg

#importa la libreria de pygame con el nombre de pg
from settings import *

class Juego:
    def __init__(self):
        #inicializa la pantalla del juego,etc
        pg.init()
        pg.font.init()
        pg.display.set_caption(TITULO)

        self.corriendo = True
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        self.reloj = pg.time.Clock()

    def new (self):
        #reinicializa las variables del juego
        self.todosLosSprites = pg.sprite.Group()


    def run(self):
        #bucle del juego
        self.jugando = True
        while self.jugando:
            self.reloj.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #bucle de juego - actualizaciones de la logica del juego
        self.todosLosSprites.update()

    def events(self):
        #bucle de juego - eventos
        for event in pg.event.get():

            if event.type == pg.QUIT: #si clickeo en la X se cierra la ventana
                if self.jugando:
                    self.jugando = False
                self.corriendo = False

    def draw(self):
        #bucle de juego - dibuja
        #maneja la parte grafica del juego
        self.pantalla.fill(GRIS1)
        self.todosLosSprites.draw(self.pantalla)
        pg.display.flip()

    def mostrarPantallaInicio(self):
        #pantalla de incio / menu inicio
        self.pantalla.fill(GRIS1)
        self.drawTexto("Iniciar", 40, GRIS2, ANCHO/2, ALTO/18*6)
        self.drawTexto("Puntuaciones", 40, GRIS2, ANCHO/2, ALTO/18*9)
        self.drawTexto("Ayuda", 40, GRIS2, ANCHO/2, ALTO/18*12)
        self.drawTexto("Salir", 40,  GRIS2, ANCHO/2, ALTO/18*15)
        pg.display.flip()
        self.esperarATeclado()

    def esperarATeclado(self):
        esperando = True
        while esperando:
            self.reloj.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    esperando = False
                    self.corriendo = False
                if event.type == pg.KEYUP:
                    esperando = False

    def mostrarPantallaFin(self):
        #pantalla cuando muere el personaje
        if self.corriendo :
            self.pantalla.fill(GRIS1)
            self.drawTexto("Fin Partida", 60, ROJO, ANCHO/2, ALTO/2)
            pg.display.flip()
            self.esperarATeclado()

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
