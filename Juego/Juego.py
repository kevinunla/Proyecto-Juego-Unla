import pygame

from pygame.display import *

#constantes
WINSIZE = [640, 480]
NOMBREVENTANA = 'juego v0.01'



def main ():
    pygame.init()
    pygame.font.init()


    pantalla = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption(NOMBREVENTANA)


    salirJuego = False
    reloj1 = pygame.time.Clock()
    gris = (51,51,51)
    gris2 = (20,20,20)
    #azul2 = (25,25,112)
    azul2 = (70,130,180)

    rojo = (255,0,0)
    verde = (0,255,0)
    azul = (0,0,255)


    def drawMenuText():
        fuenteMenu = pygame.font.Font("Demofont.otf", 40)

        textoStart = fuenteMenu.render("Iniciar",1,gris2)
        textoPuntuaciones = fuenteMenu.render("Puntuaciones",1,gris2)
        textoAyuda = fuenteMenu.render("Ayuda",1,gris2)
        textoExit = fuenteMenu.render("Salir",1,gris2)


        opcion1 = pygame.Rect(WINSIZE[0]/2-150,100,300,50)
        opcion2 = pygame.Rect(WINSIZE[0]/2-150,180,300,50)
        opcion3 = pygame.Rect(WINSIZE[0]/2-150,260,300,50)
        opcion4 = pygame.Rect(WINSIZE[0]/2-150,340,300,50)


        pygame.draw.rect(pantalla,azul2,opcion1)
        pantalla.blit(textoStart,(255,105))

        pygame.draw.rect(pantalla,azul2,opcion2)
        pantalla.blit(textoPuntuaciones,(185,185))

        pygame.draw.rect(pantalla,azul2,opcion3)
        pantalla.blit(textoAyuda,(263,265))

        pygame.draw.rect(pantalla,azul2,opcion4)
        pantalla.blit(textoExit,(270,345))


##    fuenteMenu = pygame.font.Font("Demofont.otf", 40)
##
##    textoStart = fuenteMenu.render("Iniciar",1,gris2)
##    textoPuntuaciones = fuenteMenu.render("Puntuaciones",1,gris2)
##    textoAyuda = fuenteMenu.render("Ayuda",1,gris2)
##    textoExit = fuenteMenu.render("Salir",1,gris2)
##
##
##    opcion1 = pygame.Rect(WINSIZE[0]/2-150,100,300,50)
##    opcion2 = pygame.Rect(WINSIZE[0]/2-150,180,300,50)
##    opcion3 = pygame.Rect(WINSIZE[0]/2-150,260,300,50)
##    opcion4 = pygame.Rect(WINSIZE[0]/2-150,340,300,50)
##
##



    while salirJuego !=True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT: #si clickeo en la X se cierra la ventana
                salirJuego = True

            if event.type == pygame.MOUSEBUTTONUP: #al soltar click...
                if ( WINSIZE[0]/2-150 < pygame.mouse.get_pos()[0] <  WINSIZE[0]/2+150 ):
                    if ( 100< pygame.mouse.get_pos()[1] < 150):     #opcion Start del menu
                        print ("opcion 1")
                        #aca va la funcion Start
                    elif ( 180< pygame.mouse.get_pos()[1] < 230):     #opcion 2 del menu
                        #aca va la funcion 2
                        print ("opcion 2")
                    elif ( 260< pygame.mouse.get_pos()[1] < 310):     #opcion 3 del menu
                        #aca va la funcion 3
                        print ("opcion 3")
                    elif ( 340< pygame.mouse.get_pos()[1] < 390):     #opcion Salir del menu
                        salirJuego = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    #meter codigo aca
                    print ("")
                elif event.key == pygame.K_DOWN:
                    #meter codigo aca
                    print ("")





        pantalla.fill(gris)


##        pygame.draw.rect(pantalla,azul2,opcion1)
##        pantalla.blit(textoStart,(255,105))
##
##        pygame.draw.rect(pantalla,azul2,opcion2)
##        pantalla.blit(textoPuntuaciones,(185,185))
##
##        pygame.draw.rect(pantalla,azul2,opcion3)
##        pantalla.blit(textoAyuda,(263,265))
##
##        pygame.draw.rect(pantalla,azul2,opcion4)
##        pantalla.blit(textoExit,(270,345))
##
        drawMenuText()

        pygame.display.update()
        reloj1.tick(30)


    pygame.quit()
    quit()




main()
