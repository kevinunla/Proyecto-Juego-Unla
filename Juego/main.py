
import pygame as pg     #importa la libreria de pygame con el nombre de pg
from settings import *

class Juego:
    def __init__(self):
        #inicializa la pantalla del juego, etc
        pass

    def new (self):
        #reinicializa las variables del juego
        pass

    def run(self):
        #bucle del juego
        pass

    def update(self):
        #bucle de juego - actualizacion
        #aca van 
        pass

    def events(self):
        #bucle de juego - eventos
        pass

    def draw(self):
        #bucle de juego - dibuja
        #maneja la parte grafica del juego
        pass

    def mostrarPantallaInicio(self):
        #pantalla de incio/presentacion
        pass

    def mostrarPantallaFin(self):
        #pantalla cuando muere el personaje
        pass

g = Juego()
g.mostrarPantallaInicio()

while :
    g.new()
    g.mostrarPantallaFin()

pg.quit()
