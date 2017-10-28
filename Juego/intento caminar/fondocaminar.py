#Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
#Type "copyright", "credits" or "license()" for more information.
import sys, pygame
from pygame.locals import *
 
 
# Constantes
WIDTH = 1280
HEIGHT = 720
MposX =0
MposY =330
 
 
cont=8
direc=True
i=0
xixf={}
Rxixf={}

salto = False
bajada=False 
salto_camina= False
bajada_camina=False
 
def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
 
def teclado():
    teclado = pygame.key.get_pressed()
     
    global MposX
    global MposY
    global cont, direc,salto, salto_camina
   
     


    if teclado[K_RIGHT]and salto==False and salto_camina==False:
        MposX+=2
        cont+=1
        direc=True
    elif teclado[K_LEFT]and salto==False and salto_camina==False:
        MposX-=2
        cont+=1
        direc=False
    elif teclado[K_UP] and salto==False and salto_camina==False:
        salto=True          
    elif teclado[K_UP]and teclado[K_RIGHT] and salto_camina==False:
            salto_camina=True
    elif teclado[K_UP]and teclado[K_LEFT] and salto_camina==False:
            salto_camina=True
    else :
         cont=8
         
    return

def sprite():
 
    global cont
 
    xixf[0]=(0,0,163,208)
    xixf[1]=(164,0,162,208)
    xixf[2]=(328,0,160,208)
    xixf[3]=(490,0,159,208)
    xixf[4]=(653,0,155,208)
    xixf[5]=(809,0,158,208)
    xixf[6]=(969,0,160,208)
    xixf[7]=(1133,0,162,208)
       
    Rxixf[0]=(1137,0,163,208)
    Rxixf[1]=(973,0,162,208)
    Rxixf[2]=(811,0,160,208)
    Rxixf[3]=(650,0,159,208)
    Rxixf[4]=(491,0,155,208)
    Rxixf[5]=(332,0,158,208)
    Rxixf[6]=(170,0,160,208)
    Rxixf[7]=(0,0,166,208)
    p=8
   
    global i
       
    if cont==p:
        i=0
   
    if cont==p*2:
        i=1
   
    if cont==p*3:
        i=2
   
    if cont==p*4:
        i=3
   
    if cont==p*5:
        i=4
   
    if cont==p*6:
        i=5
       
    if cont==p*7:
        i=6

    if cont==p*8:
        i=7
        cont=0
   
    return
 
 
 
 
 
def main():
    pygame.init()    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("juego")
   
 
    fondouno = imagen("imagenes/fondouno.jpg")
   
         
    blueman = imagen("imagenes/personaje.png",True)  
    blueman_inv=pygame.transform.flip(blueman,True,False);
     
    clock = pygame.time.Clock()
   

    

 
    # el bucle principal del juego
    while True:
        
        time = clock.tick(60)
       
        sprite()
        teclado()
       
       
   
        fondouno = pygame.transform.scale(fondouno, (1280, 720))
             
        screen.blit(fondouno, (0, 0))
       
        global MposX,MposY,salto,bajada,salto_camina,bajada_camina
       
        if direc==True and salto==False:
            screen.blit(blueman, ( MposX, MposY),(xixf[i]))
   
        if direc==False and salto==False:
            screen.blit(blueman_inv, ( MposX, MposY),(Rxixf[i]))
       
       
       #salto normal
        if salto==True:            
           
            if direc==True:
                screen.blit(blueman, ( MposX, MposY),(xixf[6]))
            if direc==False:
                screen.blit(blueman_inv, ( MposX, MposY),(Rxixf[6]))  
           
            if bajada==False:
                MposY-=5              
               
            if bajada==True:
                MposY+=5              
           
            if MposY==200:
                bajada=True
           
            if MposY==330:
                bajada=False
                salto=False

        if salto_camina==True and direc==True:
               
                screen.blit(blueman, ( MposX, MposY),(xixf[6]))                         
                if bajada_camina==False:
                        MposY-=5
                        MposX+=2
                if bajada_camina==True:
                    MposY+=5
                    MposX+=2
                if MposY==200:
                        bajada_camina=True
                if MposY==330:
                        bajada_camina=False
                        salto_camina=False

        if salto_camina==True and direc==False:
               
                screen.blit(blueman_inv, ( MposX, MposY),(xixf[6]))                         
                if bajada_camina==False:
                        MposY-=5
                        MposX-=2
                if bajada_camina==True:
                    MposY+=5
                    MposX-=2
                if MposY==200:
                        bajada_camina=True
                if MposY==330:
                        bajada_camina=False
                        salto_camina=False
        pygame.display.flip()
       
       
       
       
        # Cerrar la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
   
    return 0
 
 
 
 
if __name__ == '__main__':
    main()
