#Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
#Type "copyright", "credits" or "license()" for more information.
import sys, pygame
from pygame.locals import *
 
 
# Constantes
WIDTH = 900
HEIGHT = 500
MposX =300
 
 
cont=6
direc=True
i=0
xixf={}
Rxixf={}


 
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
    global cont, direc
   
       
    if teclado[K_RIGHT]:
        MposX+=2
        cont+=1
        direc=True
    elif teclado[K_LEFT]:
        MposX-=2
        cont+=1
        direc=False
    elif teclado[K_q]:
        #SALTO
        MposX-=2
    #else :
    #cont=6
       
    return

def sprite():
 
    global cont
 
    xixf[0]=(0,0,31,50)
    xixf[1]=(33,0,61,50)
    xixf[2]=(64,0,90,50)
    xixf[3]=(91,0,113,50)
    xixf[4]=(115,0,136,50)
    xixf[5]=(139,0,159,50)
    xixf[6]=(161,0,185,50)
    
       
    Rxixf[0]=(185,0,161,50)
    Rxixf[1]=(159,0,139,50)
    Rxixf[2]=(136,0,115,50)
    Rxixf[3]=(113,0,91,50)
    Rxixf[4]=(90,0,64,50)
    Rxixf[5]=(61,0,33,50)
    Rxixf[6]=(31,0,0,50)
   
    p=7
   
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
        cont=0
   
    return
 
 
 
 
 
def main():
    pygame.init()    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("juego")
   
 
    fondouno = imagen("imagenes/fondouno.jpg")
   
         
    blueman = imagen("imagenes/caminar.png",True)  
    blueman_inv=pygame.transform.flip(blueman,True,False);
     
    clock = pygame.time.Clock()
   
     
 
    # el bucle principal del juego
    while True:
        
        time = clock.tick(60)
       
        sprite()
        teclado()
       
       
   
        fondouno = pygame.transform.scale(fondouno, (900, 500))
             
        screen.blit(fondouno, (0, 0))
       
        if direc==True:
            screen.blit(blueman, ( MposX, 318),(xixf[i]))
   
        if direc==False:
            screen.blit(blueman_inv, ( MposX, 318),(Rxixf[i]))
   
        pygame.display.flip()
       
       
       
       
        # Cerrar la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
   
    return 0
 
 
 
 
if __name__ == '__main__':
    main()
