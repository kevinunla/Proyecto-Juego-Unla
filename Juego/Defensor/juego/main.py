import time,random,ecuacion,pygame,sys,nivel

from clases import*
from c_img import*
from pygame.locals import*




def main():
    con=False
    sonido_malo=False
    tiempo_ac=None
    tiempo_ac_mar=None
    pygame.init()
    resolucion=(913,628)
    pausa=img_p
    explosion=img_e
    etapa=img_n
    preparado=img_pre
    perdiste=img_per
    ventana=pygame.display.set_mode(resolucion)
    pygame.display.set_caption("DEFENSOR")
    fondo=pygame.Surface((896,628))
    clock = pygame.time.Clock()
    p=[1,0]
    pause=0
    mundo=1
    
    velocidad=1
    tiempo_p=None
    k=1
    

    
    
    co=cometa(nivel.cometa_n[mundo-1][0],nivel.cometa_n[mundo-1][1])
    estrellas=grupo_es(1)
    estrellas2=grupo_es(6)
    aster=basura(img_basura)
    menu_in(estrellas,estrellas2,resolucion,clock)
    invasores=malos(nivel.c_villanos[mundo-1][0],villanos,nivel.c_villanos[mundo-1][1],1)
    heroe=nave(nave_,misil,8,370,550)
    tablero=tab(heroe.vida,heroe.misiles,heroe.escudos,mundo,numeros,img_tablero)
    poder=items(i_bomba,i_escudo,i_misil,i_vida,i_linea,nivel.item_t[mundo-1])
    poder.prod()
    bomb=bombardero(bombardero_,nivel.bombardero_status[mundo-1],bm_b)
    kamikaze=batallon(nivel.kamikazes_status[5],nivel.kamikazes_tiempo[5])
    malo_final=minero()
    
   # menu_in(estrellas,estrellas2,resolucion,clock)
    
    while True:
        aux=list(time.localtime())
        tiempo_juego=aux[3:6]
        heroe.explosiones=[]
        clock.tick(40)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN and event.key==K_RETURN and( pause==0 or pause==1):
                pause=p[pause]
            elif (event.type==pygame.KEYDOWN and event.key==K_x):
                if heroe.escudos>=1 and heroe.escudo_act==False:
                    heroe.escudo_act=True
                    heroe.escudos=heroe.escudos-1
                    heroe.tiempo_escudo=tiempo_juego
                    tablero.actualizar(heroe.vida,heroe.misiles,heroe.escudos,mundo)
            elif (event.type==pygame.KEYDOWN and event.key==K_ESCAPE):
                menu_confirmar(ventana)
		    
	
        fondo2=pygame.Surface.copy(fondo)
	estrellas=estrellas.actualizar_estrellas(1)
	estrellas2=estrellas2.actualizar_estrellas(6)    
	aster=aster.actualizar()
	actualizar_fondo(estrellas,estrellas2,aster,fondo2)
	co=co.actualizar_cometa(fondo2,tiempo_juego,mundo,pause)
	
	poder=poder.actualizar(fondo2,pause,tiempo_juego,mundo)	
	pause=vig_tiempo(tiempo_juego,tiempo_p,pause,heroe)
	if heroe.muerto==False and mundo<11:
	    tiempo_ac_mar=sonar_malo(tiempo_juego,tiempo_ac_mar,son_marcianos,20)
	    invasores=invasores.act_nivel_invasores(mundo,villanos,velocidad)
	    pause,tiempo_p=heroe.buscar_colision_inv(invasores,tablero,mundo,pause,tiempo_p,tiempo_juego,poder,bomb)
	    pause,tiempo_p=heroe.colision_cometa(co,tablero,mundo,tiempo_p,pause,tiempo_juego,fondo)
	    pause,tiempo_p=heroe.colision_bombas(bomb,tablero,pause,tiempo_p,mundo,tiempo_juego)
	    invasores.mover(pause,tiempo_juego)
	    if invasores.llegaron:
		heroe.muerto=True
	    invasores.imprime(fondo2)
	    bomb=bomb.actualizar(mundo,tiempo_juego,fondo2,pause)
	    if mundo>=6:
		kamikaze=kamikaze.actualizar_bat(mundo,tiempo_juego,fondo2,pause)
		if kamikaze.indices!=[]:
		    if kamikaze.indices[len(kamikaze.indices)-1]==40:
			kamikaze.fin=[heroe.pos[0]+30,heroe.pos[1]+25]
			
		pause,tiempo_p=heroe.colision_kamikazes(kamikaze,tiempo_juego,mundo,tablero,pause,tiempo_p)
		heroe.colision_kamikazes_misil(kamikaze,tiempo_juego,tablero,mundo)
	  
	   
	    
	    
	    
		
	elif heroe.muerto==False and mundo==11:
	    tiempo_ac=sonar_malo(tiempo_juego,tiempo_ac,son_malo,5)
	    malo_final.mover_minero(pause,tiempo_juego)
            malo_final.imprime(fondo2)
	    heroe.colision_item(tiempo_juego,poder,mundo,tablero)
	    heroe.colision_minero_misil(malo_final,tiempo_juego)
	    pause,tiempo_p=heroe.colision_minas(malo_final,tablero,mundo,tiempo_juego,pause,tiempo_p)
	    pause,tiempo_p=heroe.colision_balas_minero(malo_final,tiempo_juego,tablero,mundo,pause,tiempo_p)
	    if malo_final.ex==False:
		heroe.escudo_act=True
		heroe.tiempo_escudo=tiempo_juego
		fondo2.blit(felicidades,(139,220))
		if difere(tiempo_juego,malo_final.muerto)>=8:
		    main()
	else:
		tiempo=tiempo_juego
		tiempo2=tiempo_juego
		while difere(tiempo,tiempo2)<3:
		    clock.tick(40)
		    for event in pygame.event.get():
			if event.type==pygame.QUIT:
			    pygame.quit()
			    sys.exit()
		    fondo2=pygame.Surface.copy(fondo)
		    aster.mover()
		    aster.imprime(fondo2)
		    estrellas.mover()
		    estrellas2.mover()
		    estrellas.imprime(fondo2)
		    estrellas2.imprime(fondo2)
		    ventana.blit(fondo2,(0,0)) 
		    
		    tablero.imprime(ventana,heroe)
		    heroe.actualizar(ventana,ventana,0,invasores,tablero,mundo,tiempo_juego)
		    ventana.blit(perdiste,(260,280))#285
		    pygame.display.flip()
		    tiempo2=list(time.localtime())
		    tiempo2=tiempo2[3:6]
		
		main()
	    

	pause,tiempo_p=heroe.colision_cometa(co,tablero,mundo,tiempo_p,pause,tiempo_juego,fondo)
	ventana.blit(fondo2,(0,0)) 
	if heroe.explosiones!=[]:
	    for i in heroe.explosiones:
		son_explosion.play()
		ventana.blit(explosion,i)
		
	heroe.actualizar(ventana,ventana,pause,invasores,tablero,mundo,tiempo_juego)
	tablero.imprime(ventana,heroe)
	if mundo<11:
	    invasores.act_barra_estado(ventana,tiempo_juego)
	heroe.act_barra_estado(ventana,tiempo_juego)    
	pausar(pause,[None,pausa,preparado],ventana)
	pygame.display.flip()	
	mundo=proximo_nivel(mundo,invasores,fondo2,ventana,tablero,heroe,clock,estrellas,estrellas2,aster,etapa,tiempo_juego)
	



def menu_confirmar(ventana):
    pos=[(250,305),(460,305)]
    e=1
 
    activo=True
	
    while activo:
	for event in pygame.event.get():
	    if event.type==pygame.QUIT:
		pygame.quit()
		sys.exit()
	    elif event.type==KEYDOWN:
		if event.key==K_ESCAPE:
		    activo=False
		elif event.key==K_RETURN and e==1:
		    activo=False
		elif event.key==K_RETURN and e==0:
		    main()
		elif event.key==K_RIGHT or event.key==K_LEFT:
		    aux=[1,0]
		    e=aux[e]
	   
	ventana.blit(confirma,(209,203))
	ventana.blit(apuntador,pos[e])
	pygame.display.flip()
		
		    




if __name__=='__main__':
    main()

	

		
	
	    
    
    
