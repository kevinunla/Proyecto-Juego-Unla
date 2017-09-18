import pygame

from pygame.display import *

#constantes
WINSIZE = [640, 480]
NOMBREVENTANA = 'juego v0.01'




def main ():
    pygame.init()
    pantalla = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption(NOMBREVENTANA)


    salir = False
    reloj1 = pygame.time.Clock() 
    gris = (51,51,51)
    rojo = (255,0,0)


    opcion1 = pygame.Rect(WINSIZE[0]/2-75,100,150,50)
    opcion2 = pygame.Rect(WINSIZE[0]/2-75,180,150,50)
    opcion3 = pygame.Rect(WINSIZE[0]/2-75,260,150,50)
    opcion4 = pygame.Rect(WINSIZE[0]/2-75,340,150,50)



    while salir!=True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: #si clickeo en la X se cierra la ventana
                salir = True
            if event.type == pygame.MOUSEBUTTONUP: #al soltar click...
                if ( WINSIZE[0]/2-75 < pygame.mouse.get_pos()[0] <  WINSIZE[0]/2+75 ):
                    if ( 100< pygame.mouse.get_pos()[1] < 150):     #opcion Start del menu
                        print "opcion 1"
                        #aca va la funcion Start
                    elif ( 180< pygame.mouse.get_pos()[1] < 220):     #opcion 2 del menu
                        #aca va la funcion 2
                        print "opcion 2"
                    elif ( 260< pygame.mouse.get_pos()[1] < 310):     #opcion 3 del menu
                        #aca va la funcion 3
                        print "opcion 3"
                    elif ( 340< pygame.mouse.get_pos()[1] < 390):     #opcion Salir del menu
                        salir = True
                        
        reloj1.tick(20)                 
        pantalla.fill(gris)
        

        pygame.draw.rect(pantalla,rojo,opcion1)
        pygame.draw.rect(pantalla,rojo,opcion2)
        pygame.draw.rect(pantalla,rojo,opcion3)
        pygame.draw.rect(pantalla,rojo,opcion4)

        
        pygame.display.update()

    pygame.quit()

#__________________________________________________________________________


main()
