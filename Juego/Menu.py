import sys
import pygame as pg
from settings import *

pg.init()

class MenuItem(pg.font.Font):
    def __init__(self, text, font=None, font_size=30,
                 font_color=BLANCO, (pos_x, pos_y)=(0, 0)):

        pg.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)

class GameMenu():
    def __init__(self, screen, items, funcs, bg_color = GRIS1 , font = None, font_size = FONTSIZE,
                 font_color = GRIS2):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        self.bg_color = bg_color
        self.clock = pg.time.Clock()

        self.funcs = funcs
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)

            # t_h:altura total del bloque de texto
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index*2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

        self.mouse_is_visible = True
        self.cur_item = None

    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pg.mouse.set_visible(True)
        else:
            pg.mouse.set_visible(False)

    def set_keyboard_selection(self, key):
        """
        Marca el MenuItem elegido atraves de las flechas.
        """
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(BLANCO)

        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pg.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pg.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pg.K_DOWN and \
                    self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pg.K_DOWN and \
                    self.cur_item == len(self.items) - 1:
                self.cur_item = 0

        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(HIGHGRIS2)

        # Finally check if Enter or Space is pressed
        if key == pg.K_SPACE or key == pg.K_RETURN:
            text = self.items[self.cur_item].text
            self.funcs[text]()

    def set_mouse_selection(self, item, mpos):
        """Marks the MenuItem the mouse cursor hovers on."""
        if item.is_mouse_selection(mpos):
            item.set_font_color(HIGHGRIS2)
            #item.set_italic(True)
        else:
            item.set_font_color(BLANCO)
            #item.set_italic(False)

    def run(self):
        mainloop = True
        while mainloop:
            self.clock.tick(50)

            mpos = pg.mouse.get_pos()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    mainloop = False
                if event.type == pg.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_keyboard_selection(event.key)
                if event.type == pg.MOUSEBUTTONDOWN:
                    for item in self.items:
                        if item.is_mouse_selection(mpos):
                            self.funcs[item.text]()

            if pg.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None

            self.set_mouse_visibility()

            # Redraw the background
            self.screen.fill(self.bg_color)

            for item in self.items:
                if self.mouse_is_visible:
                    self.set_mouse_selection(item, mpos)
                self.screen.blit(item.label, item.position)

            pg.display.flip()

##ejecucion
if __name__ == "__main__":

    def hello_world():
        print "Hello World!"

    def puntuaciones():
        pass

    def ayuda():
        pass

    # Creating the screen
    screen = pg.display.set_mode((ANCHO, ALTO), 0, 32)

    menu_items = ('Iniciar', 'Puntuaciones', 'Ayuda', 'Salir')
    funcs = {'Iniciar': hello_world,
            'Puntuaciones': puntuaciones,
            'Ayuda': ayuda,
             'Salir': sys.exit}

    pg.display.set_caption('Game Menu')
    gm = GameMenu(screen, funcs.keys(), funcs)
    gm.run()
