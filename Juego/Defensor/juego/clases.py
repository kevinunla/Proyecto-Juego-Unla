from c_img import *
import time,random,ecuacion,nivel,sys

	
    

def sonar_malo(tiempo_juego,tiempo_ac,sonido,tiempo):
    if tiempo_ac!=None:
	if difere(tiempo_juego,tiempo_ac)>=tiempo:
	    sonido.play()
	    tiempo_ac=tiempo_juego
    elif tiempo_ac==None:
	sonido.play()
	tiempo_ac=tiempo_juego
	
    return(tiempo_ac)
    

def menu_in(estrellas,estrellas2,resolucion,clock):
    aster=basura(img_basura)
    pos_flecha=[(319,249),(314,307),(319,368)]
    aux=0
    bom=bombardero(bombardero_,3,bm_b)
    fondo=pygame.Surface((913,628))
    ventana=pygame.display.set_mode(resolucion)
    m=True
    ayuda=False
    creditos=False
    son_fondo.play(-1,0,0)
    pantalla=True
    while m:
	
	tiempo=list(time.localtime())
	tiempo=tiempo[3:6]
	estrellas=estrellas.actualizar_estrellas(1)
	estrellas2=estrellas2.actualizar_estrellas(6)    
	aster=aster.actualizar()
	clock.tick(40)
	
	fondo2=pygame.Surface.copy(fondo)
	
	aster.mover()
	aster.imprime(fondo2)
	estrellas.mover()
	estrellas2.mover()
	estrellas.imprime(fondo2)
	estrellas2.imprime(fondo2)
	bom=bom.actualizar(9,tiempo,fondo2,0)
	ventana.blit(fondo2,(0,0))
	
	if creditos:
	    ventana.blit(creditos_,(15,10))
	elif ayuda==False:
	    ventana.blit(menu,(250,50)) 
	    ventana.blit(flecha_menu,pos_flecha[aux])
	elif ayuda:
	    ventana.blit(ayuda_,(12,5))
	
	pygame.display.flip()
		

	
	
	
	for event in pygame.event.get():
	    if event.type==pygame.QUIT:
		pygame.quit()
		sys.exit()
	    elif event.type==KEYDOWN :
		if event.key==K_UP and pantalla:
		    e=[2,0,1]
		    aux=e[aux]
		elif event.key==K_DOWN and pantalla:
		    e=[1,2,0]
		    aux=e[aux]
		    
		elif event.key==K_RETURN and aux==0:
		    m=False
		elif event.key==K_RETURN and aux==1:
		    ayuda=True
		    pantalla=False
		elif event.key==K_RETURN and aux==2:
		    creditos=True
		    pantalla=False
		elif event.key==K_ESCAPE and ayuda:
		    ayuda=False
		    pantalla=True
		elif event.key==K_ESCAPE and creditos:
		    creditos=False
		    pantalla=True
		
	
    son_fondo.stop()
		    
		
    


 
def proximo_nivel(mundo,invasores,fondo2,ventana,tablero,heroe,clock,estrellas,estrellas2,aster,etapa,tiempo_j):
    if len(invasores.activos)==0 and mundo<11:
	mundo+=1
	aux=list(time.localtime())
	tiempo=aux[3:6]
	aux=list(time.localtime())
	tiempo2=aux[3:6]
	while difere(tiempo,tiempo2)<3:
	    clock.tick(40)
	    for event in pygame.event.get():
		if event.type==pygame.QUIT:
		    pygame.quit()
		    sys.exit()
	    fondo2=pygame.Surface.copy(fondo)
	    actualizar_fondo(estrellas,estrellas2,aster,fondo2)
	    ventana.blit(fondo2,(0,0)) 
		    
	    tablero.imprime(ventana,heroe)
	    heroe.actualizar(ventana,ventana,0,invasores,tablero,mundo,tiempo_j)
	    ventana.blit(etapa,(305,280))#285
	    ventana.blit(numeros_nivel[mundo-1],(505,280))
	    pygame.display.flip()
	    aux=list(time.localtime())
	    tiempo2=aux[3:6]
	heroe.ex_misil=False
	tablero.actualizar(heroe.vida,heroe.misiles,heroe.escudos,mundo)
    return(mundo)



	    
def actualizar_fondo(estrellas,estrellas2,basura,fondo):
    basura.mover()
    basura.imprime(fondo)
    estrellas.mover()
    estrellas2.mover()
    basura.mover()
    estrellas.imprime(fondo)
    estrellas2.imprime(fondo)
    

	    
def pausar(pause,imagenes,fondo):
    if pause!=0:
	#if pause==2:
	 #   pygame.time.wait(250)
	#son_fondo.stop()
	posiciones=[None,(300,200),(235,280)]
	fondo.blit(imagenes[pause],posiciones[pause])
    #if pause==0:
	#son_fondo.play()
	    

    
def vig_tiempo(tiempo1,tiempo2,pause,heroe):
    if pause==2 and tiempo2!=None:
	if difere(tiempo1,tiempo2)>4:
	    pause=0
	    heroe.exploto=False
	    heroe.ex_nave=True
	    
    return(pause)
		
	    
		

def difere(a,b):
    t_a=(a[0]*3600)+(a[1]*60)+a[2]
    t_b=(b[0]*3600)+(b[1]*60)+b[2]
    
    return(abs((t_a)-(t_b)))



	
def puntos():
    p=[]
    t=[850,300,450]
    for i in range(0,random.randint(10,40)):
	p.append([random.randint(1,950),random.randint(1,t[random.randint(0,2)])])
    return(p)
    
	


def indices(longitud):
    acumulado=longitud*(-4)
    miembros=[acumulado]
    for i in range(0,longitud):
	    acumulado+=4
	    miembros.append(acumulado)
    return(miembros)









class cometa:
   
    def __init__(self,tiempo,velocidad):
	self.pos=[random.randint(20,780),-20]
	self.ex=True
	self.velocidad=velocidad
	self.rec=pygame.Rect((self.pos[0]-20,self.pos[1]-20),(40,40))
	self.rec.top=self.pos[1]-20
	self.rec.left=self.pos[0]-20
	self.rec_cola=pygame.Rect((self.pos[0]-21,self.pos[1]+3),(42,80))
	self.rec_cola.top=self.pos[1]-100
	self.rec_cola.left=self.pos[0]-21
	self.tiempo_ext=None
	self.tiempo_pro=tiempo
	
	
    def actualizar_cometa(self,fondo,tiempo_j,mundo,pause):
	if self.ex:
	    if pause==0:
		self.mover()
	    self.imprime(fondo)
	if self.ex==False and difere(self.tiempo_ext,tiempo_j)>=self.tiempo_pro:
	    self=cometa(nivel.cometa_n[mundo-1][0],nivel.cometa_n[mundo-1][1])
	return(self)
	    
	
	
    def mover(self):
	if self.pos[1]>700:
	    self.ex=False
	    aux=list(time.localtime())
	    self.tiempo_ext=aux[3:6]
	else:
	    self.pos[1]+=self.velocidad
	    self.rec.move_ip(0,+self.velocidad)
	    self.rec_cola.move_ip(0,+self.velocidad)
	    

    def imprime(self,fondo):
	color=[(240,11,45),(242,237,49)]
	if self.ex==True:
	    x=self.pos[0]-21
	    x1=self.pos[0]+21
	    y=self.pos[1]+3
	    y1=self.pos[1]-100
	    pygame.draw.circle(fondo,(255,162,117),(self.pos[0],self.pos[1]),20,0)
	    #pygame.draw.rect(fondo,(255,0,0),self.rec,1 )
	    #pygame.draw.rect(fondo,(255,0,0),self.rec_cola,1)
	    for i in range(0,50):#35
		pygame.draw.circle(fondo,color[random.randint(0,1)],(random.randint(x,x1),random.randint(y1,y)),1,0)
	    
	






class items:
    
    def __init__(self,bomba_img,escudo_img,misil_img,vida_img,linea_img,espera):
	
	self.img_=[
	
			bomba_img,#0
			escudo_img,#1
			misil_img,#2
			vida_img,#3
			linea_img#4
			
			]
	self.img_item=None
	self.rec=None
	self.pos=[None,None]
	self.item=None
	self.activo=False
	self.retraso=2
	self.inicio=[[-10,20],[820,20],[-10,450],[820,450]]
	self.dire=None
	self.incremento=2
	self.acumulado=0
	self.p_img=0
	self.l=0
	self.tiempo=None
	self.espera=espera
	
	

    def prod(self):
	self.item=random.randint(1,4)
	self.dire=random.randint(0,3)
	self.pos=self.inicio[self.dire]
	self.img_item=self.img_[self.item]
	self.rec=self.img_[self.item][0].get_rect()
	self.rec.move_ip(self.pos[0],self.pos[1])
	self.activo=True
	
	self.l=len(self.img_item)-1
	
	
    def mover(self):
	if self.activo:
	    if self.acumulado==self.retraso:
		self.acumulado=0
		op=[1,-1,1,-1]
		self.pos[0]=self.pos[0]+(self.incremento*op[self.dire])
		self.rec.move_ip(+(self.incremento*op[self.dire]),0)
		if self.p_img==self.l:
		    self.p_img=0
		else:
		    self.p_img+=1
	    else:
		self.acumulado+=1
		
    def validar(self):
	op=[1,-1,1,-1]
	if self.dire==0 or self.dire==2:
	    if self.pos[0]+(self.incremento*op[self.dire])>820:
		self.activo=False
		aux=list(time.localtime())
		self.tiempo=aux[3:6]
	elif self.dire==1 or self.dire==3:
	    if self.pos[0]+(self.incremento*op[self.dire])< -50:
		self.activo=False
		aux=list(time.localtime())
		self.tiempo=aux[3:6]
	
   
   
    def actualizar(self,fondo,pause,tiempo_j,mundo):
	if self.activo:
	    if pause==0:
		self.validar()
		self.mover()
	    fondo.blit(self.img_item[self.p_img],self.pos)
	if self.activo==False and self.tiempo!=None:
	    if difere(self.tiempo,tiempo_j)>self.espera:
		self=items(self.img_[0],self.img_[1],self.img_[2],self.img_[3],self.img_[4],nivel.item_t[mundo-1])
		self.prod()
		
	return(self)
	    
	    
	    
	    
	
		
	



class nave:#clase del vehiculo espacial
    
    
    def __init__(self,imagen,img_bala,velocidad,posx,posy):
	self.imagen=imagen
	self.vida=3
	self.bala=img_bala
	self.incremento=velocidad
	self.limites=[9,719]
	self.pos=[posx,posy] 
	self.retraso=1
	self.cuadro=0
	self.misiles=1
	self.escudos=3
	self.ayuda=0 
	self.ex_misil=False
	self.ex_nave=True
	self.limite_misil=-20
	self.velocidad_msil=30 
	self.pos_m=[]
	self.rec_misil=[]
	self.rec_nave=self.imagen[0].get_rect()
	self.rec_nave.move_ip(posx,posy)
	self.explosiones=[]
	self.muerto=False
	self.exploto=False
	self.tiempo_escudo=None
	self.cero=pygame.image.load("imagenes/let_num/numeros/0.png")
	self.pos_escudo=self.pos
	self.img_prox=0
	self.escudo_act=False
	self.acumulado=0
	self.prox_barra=0
	self.prox_estado=2
	
    def cambiar_imagen(self,tiempo_j):
	if self.escudo_act:
	    if difere(self.tiempo_escudo,tiempo_j)>=8:
		self.escudo_act=False
		self.tiempo_escudo=None
		self.prox_barra=0
		self.prox_estado=2
	    
	if self.escudo_act:
	    self.img_prox=1
	else:
	    self.img_prox=0
	    
	
	
    def lanzar_misil(self):
	self.ex_misil=True
	if self.misiles==1:
	    self.pos_m=[[self.pos[0]+36,self.pos[1]-10]]
	elif self.misiles==2:
	    self.pos_m=[ [self.pos[0]+17,self.pos[1]+35] , [self.pos[0]+53,self.pos[1]+35] ]
	elif self.misiles==4:
	    self.pos_m=[[self.pos[0]+17,self.pos[1]-5],[self.pos[0]+53,self.pos[1]-5],[self.pos[0]+17,self.pos[1]+35],[self.pos[0]+53,self.pos[1]+35]]	    
	
	self.actualizar_rec_misil()
	
	
    def actualizar_rec_misil(self):
	if len(self.pos_m)>0 and self.ex_misil:
	    self.rec_misil=[]
	    for i in self.pos_m:
		aux=self.bala.get_rect()
		aux.move_ip(i[0],i[1])
		self.rec_misil.append(aux)
	else:
	    self.ex_misil=False
	    
    
    
    
   
    def actualizar_misil(self):
	if self.ex_misil:
	    if self.cuadro==self.retraso:
		self.cuadro=0
		for i in self.pos_m:
		    i[1]-=self.velocidad_msil
		self.rec_misi=[]
		for i in self.rec_misil:
		    i.move_ip(0,-self.velocidad_msil)
	    else:
		self.cuadro+=1
	    
	    d=[i[1]<self.limite_misil for i in self.pos_m]
	    if d.count(True)==len(self.pos_m):
		self.ex_misil=False
		self.rec_misil=[]
		
    
      
      
    def imprime_misil(self,fondo):
	if self.ex_misil:
	    for i in self.pos_m:
		fondo.blit(self.bala,i)
		
		
    def autorizado(self,dire):
	r=False
	if dire==0 and (self.pos[0]-self.incremento)>self.limites[0]:
	    r=True
	elif dire==1 and (self.pos[0]+self.incremento)<self.limites[1]:
	    r=True
	return(r)
	
	
    def imprime(self,fondo,tiempo_j):
	if self.ex_nave:
	    self.cambiar_imagen(tiempo_j)
	    fondo.blit(self.imagen[self.img_prox],self.pos)
	  
    
    
    def turb_misil(self,fondo):#
	if self.ex_misil:
	    color=[(240,11,45),(242,237,49)]
	    for i in self.pos_m:
		for e in range(0,2):
		    pygame.draw.circle(fondo,color[random.randint(0,1)],(random.randint(i[0],i[0]+3),random.randint(i[1]+20,i[1]+23)),1,0)
	    
    
    
    def imprime_turbina(self,fondo):
	if self.ex_nave:
	    color=[(240,11,45),(242,237,49)]
	    for i in range(0,10):
		pygame.draw.circle(fondo,color[random.randint(0,1)],(random.randint(self.pos[0]+29,self.pos[0]+47),random.randint(self.pos[1]+50,self.pos[1]+100)),1,0)
	

    
    
    def mover(self,dire):
	aux=[-1,1]
	self.pos[0]=self.pos[0]+(self.incremento*aux[dire])
	self.rec_nave.move_ip(self.incremento*aux[dire],0)
	
    
    
    def actualizar(self,fondo,ventana,pausa,invasores,tablero,mundo,tiempo_j):
	if pausa==0:
	    tecla=pygame.key.get_pressed()
	
	    if tecla[K_LEFT] and self.autorizado(0):
		self.mover(0)
	    if tecla[K_RIGHT] and self.autorizado(1):
		self.mover(1)
	
	    if tecla[K_z] and self.ex_misil==False:
		disparo.play()
		self.lanzar_misil()
	    
		
	    
	    
	    if tecla[K_SPACE] and self.ayuda!=0:
		if self.ayuda==1 and invasores.tiempo_par==None:
		    self.ayuda=0
		    invasores.paralisis=True
		    invasores.tiempo_par=tiempo_j
		elif self.ayuda==2:
		    self.ayuda=0
	    
	
	if self.ex_misil:
	    if pausa==0:
		self.actualizar_misil()
	    self.imprime_misil(fondo)
	    self.turb_misil(fondo)    
	        
    
	   
	self.imprime(ventana,tiempo_j)
	self.imprime_turbina(ventana)
	tablero.actualizar(self.vida,self.misiles,self.escudos,mundo)
	 
	#return(invasores)
    
    
    def act_barra_estado(self,fondo,tiempo_j):
	if self.escudo_act:
	    fondo.blit(barra_estado[self.prox_barra],(819,310))
	    if difere(self.tiempo_escudo,tiempo_j)==self.prox_estado:
		self.prox_barra+=1
		self.prox_estado+=2
              
    
    def buscar_colision_inv(self,otro,tablero,mundo,pausa,tiempo_p,tiempo_j,poder,bomb):
	pausa=self.colision_invasores(otro,tablero,mundo,pausa,tiempo_p)
	self.colision_invasores_misil(otro,tablero,mundo)
	self.colision_item(tiempo_j,poder,mundo,tablero)
	self.colision_bombardero_misil(bomb,tablero,mundo,tiempo_j)
	return(pausa)
	
    
    def colision_bombas(self,bomb,tablero,pausa,tiempo_p,mundo,tiempo_j):
	if bomb.b_activa:
	    misiles=[None,1,1,None,2]
	    indice=self.rec_nave.collidelist(bomb.rec_bombas)
	    if indice!=-1 and self.escudo_act==False:
		if self.vida>0:
		    del bomb.bombas_ac[indice]
		    del bomb.rec_bombas[indice]
		    if bomb.ac==False and bomb.bombas_ac==[]:
			bomb.desactivado=True
			bomb.tiempo_m=tiempo_j
		    self.explosiones.append(self.pos)
		    pausa=2
		    self.vida-=1
		    self.misiles=misiles[self.misiles]
		    aux=list(time.localtime())
		    tiempo_p=aux[3:6]
		    self.exploto=True
		    tablero.actualizar(self.vida,self.misiles,self.escudos,mundo)
		else:
		    self.muerto=True
		     
	
	return(pausa,tiempo_p)
	    
	    
	
	
    
    def colision_item(self,tiempo_j,poder,mundo,tablero):
	if self.ex_misil and poder.activo:
	    indice=poder.rec.collidelist(self.rec_misil)
	    
	    if indice!=-1 :
		self.explosiones.append(poder.pos)
	        poder.activo=False
		poder.tiempo=tiempo_j
		del self.pos_m[indice]
		if poder.item==3 and self.vida<5:
		    self.vida+=1
		elif poder.item==2 and self.misiles<4:
		    self.misiles=self.misiles*2
		elif poder.item==1 and self.escudos<5:
		    self.escudos+=1
		elif poder.item==4 and self.ayuda!=1:
		    self.ayuda=1
		elif poder.item==0 and self.ayuda!=2:
		    self.ayuda=2
		if len(self.rec_misil)==0:
		    self.ex_misil=False
		else: 
		    self.actualizar_rec_misil()
		    
	    tablero.actualizar(self.vida,self.misiles,self.escudos,mundo)
	    
	    
	    
	
    
    def colision_cometa(self,cometa,tablero,mundo,tiempo_p,pausa,tiempo_j,fondo):
	if cometa.ex:
	    misiles=[None,1,1,None,2]
	    lista=[cometa.rec,cometa.rec_cola]
	    indice=self.rec_nave.collidelist(lista)
	    if indice!=-1 and self.escudo_act==False:
		if self.vida>0:
		    cometa.ex=False
		    aux=list(time.localtime())
		    cometa.tiempo_ext=aux[3:6]
		    cometa
		    self.explosiones.append(self.pos)
		    pausa=2
		    self.vida-=1
		    self.misiles=misiles[self.misiles]
		    aux=list(time.localtime())
		    tiempo_p=aux[3:6]
		    self.exploto=True
		    tablero.actualizar(self.vida,self.misiles,self.escudos,mundo)
		else:
		    self.muerto=True
	
	return(pausa,tiempo_p)
	    
    def colision_minero_misil(self,minero,tiempo_j):
	if self.ex_misil and minero.ex:
	    if minero.canon_ex:
		lista=[minero.rec,minero.rec_canon]
	    else:
		lista=[minero.rec]
	    for i in self.rec_misil:
		indice=i.collidelist(lista)
		if indice!=-1:
		    minero.impactos+=1
		    self.explosiones.append([i.left,i.top])
		    if minero.impactos>=50:
			minero.ex=False
			minero.muerto=tiempo_j
			minero.rec=[]
			minero.rec_minas=[]
			minero.rec_balas=[]
			minero.canon_ex=False
			minero.rec_canon=[]
		    del self.pos_m[self.rec_misil.index(i)]
		    if len(self.rec_misil)==0:
			self.ex_misil=False
		    else:
			self.actualizar_rec_misil()
		    indice=-1
		
		    
		
		    
    
    def colision_bombardero_misil(self,otro,tablero,mundo,tiempo_j):
	if self.ex_misil and otro.ac:
	    indice=otro.rec.collidelist(self.rec_misil)
	    if indice!=-1:
		self.explosiones.append(self.pos_m[indice])
		direcciones=[1065,-55]
		otro.pos[0]=direcciones[otro.direccion]
		otro.ac=False
		if otro.bombas==3:
		    otro.desactivado=True
		    otro.tiempo_m=tiempo_j
		else:
		    otro.bombas=0
		del self.pos_m[indice]
		if len(self.rec_misil)==0:
		    self.ex_misil=False
		else:
		    self.actualizar_rec_misil()
		
	    
	
    def colision_invasores_misil(self,otro,tablero,mundo):
	if self.ex_misil and otro.existen:
	    for i in self.rec_misil:
		indice_c=i.collidelist(otro.lista)
		if indice_c!=-1:
		    self.explosiones.append(otro.activos[indice_c])
		    indice=self.rec_misil.index(i)
		    del self.pos_m[indice]
		    del otro.activos[indice_c]
		    if len(self.rec_misil)==0:
			self.ex_misil=False
		    else:
			self.actualizar_rec_misil()
		    otro.act_rec()
		    otro.ultimo=otro.ult()
		    tablero.actualizar(self.vida,self.misiles,self.escudos,mundo)
		    
    
    def colision_kamikazes_misil(self,kamikaze,tiempo_j,tablero,mundo):
	if self.ex_misil and kamikaze.activo:
	    for i in self.rec_misil:
		indice_c=i.collidelist(kamikaze.lista_r)
		if indice_c!=-1:
		    aux=[kamikaze.lista_r[indice_c].left,kamikaze.lista_r[indice_c].top]
		    self.explosiones.append(aux)
		    indice=self.rec_misil.index(i)
		    del self.pos_m[indice]
		    del kamikaze.lista_r[indice_c]
		    del kamikaze.indices[indice_c]
		    
		    if kamikaze.indices==[]:
			kamikaze.tiempo_m=tiempo_j
			kamikaze.activo=False
		    if len(self.rec_misil)==0:
			self.ex_misil=False
		    else:
			self.actualizar_rec_misil()
		tablero.actualizar(self.vida,self.misiles,self.escudos,mundo)
    
    def colision_balas_minero(self,minero,tiempo_j,tablero,mundo,pausa,tiempo_p):
	misiles=[None,1,1,None,2]
	indice=self.rec_nave.collidelist(minero.rec_balas)
	if indice!=-1 and self.escudo_act==False:
	    if self.vida>0:
		self.explosiones.append(self.pos)
		del minero.balas[indice]
		del minero.rec_balas[indice]
		pausa=2
		tiempo_p=tiempo_j
		self.exploto=True
		self.vida-=1
		self.misiles=misiles[self.misiles]
		tablero.actualizar(self.vida,self.misiles,self.escudos,mundo)
	    else:
		self.muerto=True
	return(pausa,tiempo_p)
    
    def colision_minas(self,minero,tablero,mundo,tiempo_j,pausa,tiempo_p):
	misiles=[None,1,1,None,2]
	indice=self.rec_nave.collidelist(minero.rec_minas)
	if indice!=-1 and self.escudo_act==False:
	    if self.vida>0:
		self.explosiones.append([minero.rec_minas[indice].left,minero.rec_minas[indice].top])
		del minero.minas[indice]
		del minero.rec_minas[indice]
		pausa=2
		tiempo_p=tiempo_j
		self.exploto=True
		self.vida-=1
		self.misiles=misiles[self.misiles]
		tablero.actualizar(self.vida,self.misiles,self.escudos,mundo)
	    else:
		self.muerto=True
	return(pausa,tiempo_p)
    
    def colision_kamikazes(self,kamikaze,tiempo_j,mundo,tablero,pausa,tiempo_p):
	misiles=[None,1,1,None,2]
	indice=self.rec_nave.collidelist(kamikaze.lista_r)
	if indice!=-1 and self.escudo_act==False:
	    if self.vida>0:
		kamikaze.activo=False
		kamikaze.tiempo_m=tiempo_j
		for i in kamikaze.lista_r:
		    aux=[0,0]
		    aux[0]=i.left
		    aux[1]=i.top
		    self.explosiones.append(aux)
		kamikaze.lista_r=[]
		pausa=2
		tiempo_p=tiempo_j
		self.exploto=True
		self.vida-=1
		self.misiles=misiles[self.misiles]
		tablero.actualizar(self.vida,self.misiles,self.escudos,mundo)
	    
	    elif self.vida==0:
		self.muerto=True
	    
	return(pausa,tiempo_p)
    
	
    
    def colision_invasores(self,otro,tablero,mundo,pausa,tiempo_p):
	misiles=[None,1,1,None,2]
	indice=self.rec_nave.collidelist(otro.lista)
	
        if indice!=-1 and self.escudo_act==False:
	
	    tiempo_p=None
	    self.explosiones.append(self.pos)
	    if self.vida>0:
		pausa=2
		aux=list(time.localtime())
		tiempo_p=aux[3:6]
		self.exploto=True
		self.vida-=1
		self.misiles=misiles[self.misiles]
		self.explosiones.append(otro.activos[indice])
		del otro.activos[indice]
		otro.act_rec()
		otro.ultimo=otro.ult()
		tablero.actualizar(self.vida,self.misiles,self.escudos,mundo)
	    elif self.vida==0:
		self.muerto=True
	return(pausa,tiempo_p)
	

	
	
	


class malos:#clase de malos principales
    
    
    
    def __init__(self,nivel,imagenes,velocidad,retraso):
	self.puntos=[
			[ [250,50],[320,50],[390,50],[460,50],[530,50],[600,50] ],
			[ [250,90],[320,90],[390,90],[460,90],[530,90],[600,90] ],
			[ [250,130],[320,130],[390,130],[460,130],[530,130],[600,130] ],
			[ [250,170],[320,170],[390,170],[460,170],[530,170],[600,170] ],
			[ [250,210],[320,210],[390,210],[460,210],[530,210],[600,210] ],
			[ [250,250],[320,250],[390,250],[460,250],[530,250],[600,250] ],
			[ [250,290],[320,290],[390,290],[460,290],[530,290],[600,290] ]
			
			
	
		    ]
	
	self.lista=[]
	self.nivel=nivel
	self.existen=True
	self.limites=[11,750]
	self.imagenes=imagenes
	self.incremento_y=30
	self.incremento_x=velocidad
	self.cuadros=0
	self.velocidad=retraso
	self.p_img=0
	self.activos=self.tomar_p()
	self.act_rec()
	self.dire=random.randint(0,1)
	self.ultimo=self.ult()
	self.tiempo=False
	self.act_inc=False
	self.paralisis=False
	self.limite_paralisis=8
	self.tiempo_par=None
	self.prox_barra=0
	self.prox_estado=2
	self.llegaron=False
	
	
    
    def act_nivel_invasores(self,mundo,imagenes,velocidad):
	if self.activos==0 or self.activos==[]:
	    self=malos(nivel.c_villanos[mundo-1][0],imagenes,nivel.c_villanos[mundo-1][1],velocidad)
	    if mundo-1>=5:
		self.incremento_x=10
	return(self)
	
	
    
    def tomar_p(self):
	lista=[]
	for i in range(0,self.nivel):
	    for e in self.puntos[i]:
		lista.append(e)
	return(lista)
	
	
	
    	
    def act_rec(self):
	if len(self.activos)>0 and self.existen:
	    self.lista=[]
	    for i in self.activos:
		aux=self.imagenes[self.p_img].get_rect()
		aux.move_ip(i[0],i[1])
		self.lista.append(aux)
	else:
	    self.existen=False
	    self.lista=[]
	    self.activos=[]
	    
	    
     
    def imprime(self,fondo):
	if len(self.activos)>0 and self.existen:
	    for i in self.activos:
		fondo.blit(self.imagenes[self.p_img],i)	
	 
	else:
	    self.existen=False
	    
    def vig_llegada(self):
	if self.existen:
	    for i in self.activos:
		if i[1]>628:
		    self.llegaron=True
    

    def vig_paralisis(self,tiempo_j):
	if (self.paralisis) and (difere(tiempo_j,self.tiempo_par)>=self.limite_paralisis):
	    self.paralisis=False
	    self.tiempo_par=None
	    self.prox_barra=0
	    self.prox_estado=2
  
    def act_barra_estado(self,fondo,tiempo_j):
	if self.paralisis:
	    fondo.blit(barra_estado[self.prox_barra],(819,460))
	    if difere(self.tiempo_par,tiempo_j)==self.prox_estado:
		self.prox_barra+=1
		self.prox_estado+=2
	    
    def mover(self,pausa,tiempo_j):
	self.vig_paralisis(tiempo_j)
	if pausa==0 and self.paralisis==False:
	    if self.existen:
		if len(self.activos)==1 and self.act_inc==False:
		    self.incremento_x=self.incremento_x*2
		    self.act_inc=True
		if self.cuadros==self.velocidad:
		    self.cuadros=0
		    autorizado=False
		    dire=[1,0]
		    if self.dire==0:
			if self.activos[self.ultimo[0]][0]-self.incremento_x>self.limites[0]:
			    inc=self.incremento_x*(-1)
			    autorizado=True
		    elif self.dire==1:
			if self.activos[self.ultimo[1]][0]+self.incremento_x<self.limites[1]:#799
			    inc=self.incremento_x
			    autorizado=True
		    
		    if autorizado:
			for i in self.activos:
			    i[0]+=inc
		    else:
			for i in self.activos:
			    i[1]+=self.incremento_y
			self.dire=dire[self.dire]
		    if self.p_img<3:
			self.p_img+=1
		    else:
			self.p_img=0
		    self.act_rec()
		else:
		    self.cuadros+=1
		self.vig_llegada()
		
	
		
    def ult(self):
	dif_1=1000
	dif_2=1000
	in_p=None
	in_u=None
	for i in self.activos:
	    if dif_1>(i[0]-self.limites[0]):
		dif_1=i[0]-self.limites[0]
		in_p=self.activos.index(i)
	    if dif_2>(self.limites[1]-i[0]):
		dif_2=self.limites[1]-i[0]
		in_u=self.activos.index(i)
		
	ultimo=[in_p,in_u]
	return(ultimo)

	     

class basura:
    
    def __init__(self,img_basura):
	self.imagenes=img_basura
	self.acumulado=0
	self.direccion=random.randint(0,2)
	self.incremento=1
	self.puntos=self.prod()
	self.acumulado=0
	self.existe=True
	self.cuadro=3
	
    
    
    def mover(self):
	if self.acumulado==self.cuadro:
	    self.acumulado=0
	    op=[1,0,0]
	    ope=[1,1,-1]
	
	    for i in self.puntos: 
		inc=self.incremento*ope[self.direccion]
		i[op[self.direccion]]=i[op[self.direccion]]+inc
	else:
	    self.acumulado+=1
	    
	    
	    
    def imprime(self,fondo):
	if self.existe==True:
	    for i in self.puntos:
		fondo.blit(i[2],(i[0],i[1]))
	self.validar()
	
    
    def validar(self):
	limites=[638,728,-10]
	direcciones=[1,0,0]
	
	condicion=[True,True,False]
	
	d=[i[direcciones[self.direccion]]>limites[self.direccion] for i in (self.puntos) ]
	if d.count(condicion[self.direccion])==len(self.puntos):
	    self.existe=False 
	
	
    
    def prod(self):
	self.existe=True
	puntos=[]
	f=random.randint(1,10)
	x=[(0,700),(-400,0),(800,1200)]
	y=[(-400,0),(0,450),(0,450)]
	
	for i in range(0,f):
	    pos_x=random.randint(x[self.direccion][0],x[self.direccion][1])
	    pos_y=random.randint(y[self.direccion][0],y[self.direccion][1])
	    img=random.randint(0,1)
	    puntos.append([pos_x,pos_y,self.imagenes[img]])
	
	return(puntos)
    
    def actualizar(self):
	if self.existe==False:
	    self=basura(img_basura)
	return(self)
    


	
	


class tab:
    
    def __init__(self,vida,misil,escudo,nivel,imagenes,img_tablero):
	self.tablero=img_tablero
	self.imagenes=imagenes
	self.c_vida=imagenes[vida]
	self.c_misil=imagenes[misil]
	self.c_escudo=imagenes[escudo]
	self.c_nivel=imagenes[nivel]
	self.combo=[[self.c_vida,(868,69),vida],[self.c_misil,(868,166),misil],[self.c_escudo,(871,261),escudo],[self.c_nivel,(849,557),nivel]]
	
	
    
   
    def actualizar(self,vida,misil,escudo,nivel):
	aux=[vida,misil,escudo,nivel]
	posicion=((829,400),(None))
	
	for i in range(0,4):
	    self.combo[i][2]=aux[i]
	    self.combo[i][0]=self.imagenes[aux[i]]
	
	
	
   
   
    def imprime(self,fondo,heroe):
	fondo.blit(self.tablero,(796,-3))
	for i in self.combo:
	    fondo.blit(i[0],i[1])
	
	
	if heroe.ayuda!=0:
	    posiciones=[(None),(829,400),(839,400)]
	    imagenes=[None,paralisis,bon]
	    fondo.blit(imagenes[heroe.ayuda],posiciones[heroe.ayuda])

	    
	
	
	













class grupo_es:
    
    
    def __init__(self,incremento=1):
	self.puntos=puntos()
	self.fin=False
	self.color=[(0,0,0),(2,166,162),(0,0,0),(235,244,53),(0,0,0),(255,255,255),(255,160,66),(0,0,0),(255,159,255),(254,47,41),(0,0,0)]
	self.incremento=incremento
    
    def mover(self):
	for i in self.puntos:
	    i[1]+=self.incremento
	    if i[1]>850:
		self.fin=True
		
    def imprime(self,fondo):
	for i in self.puntos:
	    pygame.draw.circle(fondo,self.color[random.randint(0,10)],(i[0],i[1]),1,0)
	    
    
    def actualizar_estrellas(self,incremento):
	
	if self.fin==True:
	    self=grupo_es(incremento)
	return(self)
	    
	
	
	
	




class minero:
    
    def  __init__(self,retraso=3,limite=400,horizontal=False):
	self.barra_estado=barra_minero
	self.prox_barra=0
	self.acumulado=0
	self.imagen=mine
	self.img_mina=mina
	self.pos_mine=[random.randint(0,679),-70]
	self.pos_min=[self.pos_mine[0]+43,self.pos_mine[1]+24]
	self.pos_barra=[self.pos_mine[0]+38,self.pos_mine[1]-6]
	self.pos_canon=None
	self.canon=img_canon
	self.bala=img_bala
	self.rec_canon=self.canon.get_rect()
	self.canon_ex=False
	self.prox_mine=0
	self.prox_mina=0
	self.vel_mine=10
	self.vel_mina=50
	self.dire_mine=random.randint(0,1)
	self.li_vertical=562
	self.mov_horizontal=horizontal
	self.retraso=retraso
	self.acumulado=0
	self.ex=True
	self.ope=[self.vel_mine*-1,self.vel_mine]
	self.limites_lad=[-1,679]
	self.mine_limit_vertical=limite
	self.prox_dir=[1,0]
	self.min_activa=False
	self.impactos=0
	self.destruccion=30
	self.primer=True
	self.huida=False
	self.rec=self.imagen[2].get_rect()
	self.rec.move_ip(self.pos_mine)
	self.balas=[]
	self.rec_balas=[]
	self.minas=[]#
	self.rec_minas=[]
	self.tiempo=None
	self.muerto=None
	self.t_limite=1
	self.m_retraso=4
	self.c_m=0

	
    def mover_pos_barra(self):
	limites=[[10,20],[20,30],[30,40],[40,50]]
	valor=[1,2,3,4]
	self.pos_barra[0]=self.pos_mine[0]+38
	self.pos_barra[1]=self.pos_mine[1]-6
	for i in limites:
	    if self.impactos>=i[0] and self.impactos<i[1]:
		self.prox_barra=valor[limites.index(i)]
	
	    
	
	
	
    def prox_imagen(self):
	if self.prox_mine==3:
	    self.prox_mine=0
	else:
	    self.prox_mine+=1
	
    def disparar(self):
	pos=[self.pos_canon[0]+21,self.pos_canon[1]+5]
	aux=self.bala.get_rect()
	aux.move_ip(pos)
	self.rec_balas.append(aux)
	self.balas.append(pos)
	
    
    def mover_bala(self):
	if self.balas!=[]:
	    for i in self.balas:
		i[1]+=10
		self.rec_balas[self.balas.index(i)].move_ip(0,+10)
	    
	    for i in self.balas:
		if i[1]>628:
		    indice=self.balas.index(i)
		    del self.balas[indice]
		    del self.rec_balas[indice]
    
    def imprime_balas(self,fondo):
	if self.balas!=[]:
	    for i in self.balas:
		fondo.blit(self.bala,i)
    
    
    def lanzar_mina(self):
	pos=[self.pos_mine[0]+53,self.pos_mine[1]+40]
	aux=self.img_mina[0].get_rect()
	aux.move_ip(pos)
	self.rec_minas.append(aux)
	self.minas.append(pos)
	aux=None
	
    
    def actualizar_minas(self):
	if self.minas!=[]:
	    for i in range(0,len(self.minas)):
		if self.minas[i][1]<560:
		    self.minas[i][1]+=10
		    self.rec_minas[i].move_ip(0,+10)
	
	    
	    if self.c_m==self.m_retraso:
		self.c_m=0
		prox_img=[1,2,0]
		self.prox_mina=prox_img[self.prox_mina]
	    else:
		self.c_m+=1
		
    def imprime_minas(self,fondo):
	if self.minas!=[]:
	    for i in self.minas:
		fondo.blit(self.img_mina[self.prox_mina],i)
		
	
    
    
	
	
	
	
	
    def mover_minero(self,pause,tiempo_j):
	if pause==0:
	    self.actualizar_minas()
	    if self.ex and self.acumulado==self.retraso:
		self.mover_bala()
		if self.impactos>=20 and self.huida==False:
		    self.mov_horizontal=False
		    
		self.acumulado=0
		if  (self.mov_horizontal==False)and(self.primer) :
		    self.pos_mine[1]+=self.vel_mine*2
		    self.rec.move_ip(0,+self.vel_mine*2)
		    if self.pos_mine[1]>=self.mine_limit_vertical:
			self.mov_horizontal=True
			self.primer=False
			self.tiempo=tiempo_j
		elif self.impactos>=20 and self.mov_horizontal==False:
		    self.pos_mine[1]-=(self.vel_mine)*3
		    self.rec.move_ip(0,-(self.vel_mine)*3)
		    if self.pos_mine[1]<=40:
			self.mov_horizontal=True
			self.huida=True
			self.canon_ex=True
			self.pos_canon=[self.pos_mine[0]+42,self.pos_mine[1]+35]
			self.rec_canon.move_ip(self.pos_canon)
			self.retraso=2
			self.vel_mine=self.vel_mine*3
			self.tiempo=None
			#self.transcurrido=None
		     
		else:
		    if ecuacion.es_intervalo(self.pos_mine[0]+self.ope[self.dire_mine],self.limites_lad):
			
			self.pos_mine[0]+=self.ope[self.dire_mine]
			self.rec.move_ip(+self.ope[self.dire_mine],0)
			if self.canon_ex:
			    self.pos_canon[0]+=self.ope[self.dire_mine]
			    self.rec_canon.move_ip(+self.ope[self.dire_mine],0)
			    if random.randint(1,25)==10:
				self.disparar()
				lazer.play()
			if self.tiempo!=None:
			    tiempo=tiempo_j
			    if difere(self.tiempo,tiempo)>=self.t_limite:
				self.lanzar_mina()
				self.tiempo=tiempo_j
				self.t_limite=5 
			
			    
		    else:
			self.dire_mine=self.prox_dir[self.dire_mine]
		self.prox_imagen()
	    elif self.ex and self.acumulado!=self.retraso:
		if self.impactos>=20 and self.huida==False:
		    self.mov_horizontal=False
		self.acumulado+=1
	    self.mover_pos_barra()
	    
    
    def imprime(self,fondo):
	if self.ex:
	    fondo.blit(self.imagen[self.prox_mine],self.pos_mine)
	    fondo.blit(self.barra_estado[self.prox_barra],self.pos_barra)

	    if self.canon_ex:
		fondo.blit(self.canon,self.pos_canon)
	    if self.balas!=[]:
		self.imprime_balas(fondo)
	    if self.minas!=[]:
		self.imprime_minas(fondo)
	    
	    
    






class bombardero:
    
    def __init__(self,imagenes,tiempo,bm_b):
	self.direccion=random.randint(0 ,1)
	self.limites=[1065,-55]
	
	self.opciones=[[0,10],[900,10]]
	self.pos=self.opciones[self.direccion]
	self.prox=0
	self.ac=True
	self.imagenes=imagenes
	self.incremento=1
	self.img_bomba=bm_b#[pygame.image.load(img) for  img in ("bomb.png","b_ab.png")]
	self.pos_b=[[self.pos[0]-10,self.pos[1]+31],[self.pos[0]+21,self.pos[1]+31],[self.pos[0]+52,self.pos[1]+31]]
	self.rec_b=None
	self.inc=[-10,21,52]
	self.bombas=3
	self.bombas_ac=[]
	self.rec_bombas=[]
	self.p_b=0
	self.dir_b=0
	self.control=pygame.time.Clock()
	self.c=False
	self.tiempo=0
	self.tiempo_m=0
	self.tiempo_prod=tiempo
	self.tiempo_bom=0
	self.b_activa=True
	self.desactivado=False
	self.rec=self.imagenes[0].get_rect()
	self.rec.move_ip(self.pos)
    
    
    def mov_bom(self,pause):
	if self.bombas!=0:
	    for i in range(0,self.bombas):
		self.pos_b[i][0]=self.pos[0]+self.inc[i]
		self.pos_b[i][1]=self.pos[1]+31
    
	if self.bombas_ac!=[]:
	    self.mov_lanzadas(pause)
	 
	 
    def aut_lanzar(self):
	a=random.randint(1,200)
	l=len(self.inc)
	if (self.bombas!=0 and a==1) and ((self.direccion==0 and self.pos[0]>=40)or(self.direccion==1 and self.pos[0]<=680)):
	    n=random.randint(0,l-1)
	    del self.inc[n]
	    self.bombas_ac.append(self.pos_b[n])
	    self.rec_b=self.img_bomba[1].get_rect()
	    self.rec_b.move_ip(self.pos_b[n])
	    self.rec_bombas.append(self.rec_b)
	    del self.pos_b[n]
	    self.bombas-=1
	    
	
	     
    def mov_lanzadas(self,pause):
	op=[50,-50]
	d=[1,0]
	o=[1,-1]
	if self.b_activa and pause==0:
	    if self.tiempo_bom==2:
		self.b_activa=True
		for i in range(0,len(self.bombas_ac)):
		    self.bombas_ac[i][0]+=op[self.dir_b]
		    self.rec_bombas[i].move_ip(+op[self.dir_b],0)
		    
		self.tiempo_bom=0
		
		self.p_b+=o[self.dir_b]
	    
		if self.p_b==3:
		    self.dir_b=d[self.dir_b]
		    for i in range(0,len(self.bombas_ac)):
			self.bombas_ac[i][1]+=15
			self.rec_bombas[i].move_ip(0,+15)
			
		elif self.p_b==0:
		    self.dir_b=d[self.dir_b]
		    for i in range(0,len(self.bombas_ac)):
			self.bombas_ac[i][1]+=15
			self.rec_bombas[i].move_ip(0,+15)
		
	    
		
	    else:
		self.tiempo_bom+=1
		
	     
    def imprime_lanzadas(self,fondo):
	for i in self.bombas_ac:
	    fondo.blit(self.img_bomba[1],i)
	    
	    
    
    def aprobar(self):
	if (self.direccion==0 and self.pos[0]<1065):
	    self.ac=True
	elif (self.direccion==1 and self.pos[0]>-55):
	    self.ac=True
	else:
	    self.ac=False
	    
	if self.bombas_ac!=[]:
	    aux=self.bombas_ac
	    for i in self.bombas_ac:
		if i[1]>=630:
		    del aux[aux.index(i)]
		    
	    self.bombas_ac=aux
	
	    
	
	if self.bombas_ac==[] and self.bombas==0:
	    self.b_activa=False
	
	
    def cambio_img(self):
	if self.prox<3:#4
	    self.prox+=1
	else:
	    self.prox=0
	
    def mover(self,pause,tiempo_j):
	self.aprobar()
	if self.ac and pause==0:
	    self.aut_lanzar()
	    if self.direccion==0:
		self.pos[0]+=self.incremento
		self.rec.move_ip(self.incremento,0)
	    elif self.direccion==1:
		self.pos[0]-=self.incremento
		self.rec.move_ip(-self.incremento,0)
	if self.b_activa and pause==0:
	    self.mov_bom(pause)
	
	#if self.sound==False and (self.direccion==0 and self.pos[0]>=40)or(self.direccion==1 and self.pos[0]<=680):
	#	self.sound=True
	#	son_bombardero.play()
	
	if self.ac==False and self.b_activa==False:
	    if self.desactivado==False:
		self.tiempo_m=tiempo_j
		self.desactivado=True
	
    def imprime(self,fondo):
	if self.ac:
	    fondo.blit(self.imagenes[self.prox],self.pos)
	    for i in range(0,self.bombas):
		fondo.blit(self.img_bomba[0],self.pos_b[i])
	    if self.tiempo==5:#8
		self.cambio_img()
		self.tiempo=0
	    else:
		self.tiempo+=1
	if self.b_activa:
	    self.imprime_lanzadas(fondo)
    
    
    def actualizar(self,mundo,tiempo_j,fondo,pause):
	if self.desactivado==False:
	    self.mover(pause,tiempo_j)
	    self.imprime(fondo)
	else:
	    if difere(self.tiempo_m,tiempo_j)>=self.tiempo_prod:
		self=bombardero(bombardero_,nivel.bombardero_status[mundo-1],bm_b)
	return(self)
	



class batallon:
    def __init__(self,cantidad,tiempo_prod):
	self.img=img_kamikazes#[pygame.image.load(img) for img in ("inv2.png","inv3.png","inv4.png","inv5.png")]
	self.p_finales=[130,260,390]
	self.prox_img=0
	self.indices=indices(cantidad)#[-4,0]#[-6,-4,-2,0]#
	self.acumulado=0
	self.fin=None
	self.definido=False
	#self.rec=self.img[0].get_rect()
	self.x1_rec1=random.randint(10,660)#recta 1 x1#980
	self.x2_rec1=self.def_final(self.x1_rec1)#recta2 x2
	
	self.x1_rec2=self.x2_rec1#recta2 x1
	self.x2_rec2=self.def_final(self.x1_rec2)#recta2 x2
	
	self.rec1=self.recta(self.x1_rec1,self.x2_rec1,0,130,0)#puntos primera recta(14 puntos) #cir 13 puntos 13+14x2=41 puntos trayectoria total
	self.cir=[  [self.x2_rec1-46,130+19]  ,  [self.x2_rec1-65,130+65]  ,  [self.x2_rec1-46,130+111]  , [self.x2_rec1,130+130] ,  [self.x2_rec1+46,130+111]  ,[self.x2_rec1+65,130+65]  ,  [self.x2_rec1+46,130+19]  ,  [self.x2_rec1,130],      [self.x2_rec1-46,130+19]  ,  [self.x2_rec1-65,130+65]  ,  [self.x2_rec1-46,130+111]  , [self.x2_rec1,130+130]      ]
	
	self.rec2=self.recta(self.x1_rec2,self.x2_rec2,260,420,260)#puntos segunda recta (14 puntos) 390
	
	self.rec3=None #recta final
	
	self.camino=self.trayectoria()
	self.lista_r=self.lista_rec()
	self.activo=True
	self.tiempo_limite=tiempo_prod
	self.sound=False
	
	
	
    
    
    def lista_rec(self):
	lista=[]
	for i in self.indices:
	    aux=self.img[0].get_rect()
	    lista.append(aux)
	
	return(lista)
	
    
    def imprime(self,fondo):
	if self.activo:
	    for i in self.indices:
		if i>=0 and i<len(self.camino):
		    fondo.blit(self.img[self.prox_img],self.camino[i])
	     
	    
		
    
    def actualizar_bat(self,mundo,tiempo_j,fondo,pause):
	if self.sound==False:
	    son_kamikaze.play()
	    self.sound=True
	if self.activo:
	    if pause==0:
		if self.acumulado==2:
		    for i in self.indices:
			self.indices[self.indices.index(i)]+=1
	      
		    for i in self.indices:
			if i>=0 and i<len(self.camino):
			    self.lista_r[self.indices.index(i)].left=(self.camino[i][0])
			    self.lista_r[self.indices.index(i)].top=(self.camino[i][1])
			    
		    self.acumulado=0
		    
		    if self.prox_img==3:
			self.prox_img=0
		    else:
			self.prox_img+=1 
		    
		else:
		    self.acumulado+=1
		    
		if self.fin!=None and self.definido==False:
		    punto_in=self.camino[len(self.camino)-1]
		    punto_fin=self.fin
		    self.rec3=self.recta(punto_in[0],punto_fin[0],punto_in[1],punto_fin[1],420)
		    for i in self.rec3:
			self.camino.append(i)
		    self.definido=True
		
	    aux=[i.top==575 for i in self.lista_r]
	    if aux.count(True)==len(self.lista_r):
		self.activo=False
		self.tiempo_m=tiempo_j
		self.lista_r=[]
	    self.imprime(fondo)
	else:
	    if difere(self.tiempo_m,tiempo_j)>=self.tiempo_limite:
		self=batallon(nivel.kamikazes_status[mundo-1],nivel.kamikazes_tiempo[mundo-1])
	return(self)






    
    def trayectoria(self):
	puntos=[]
	for i in self.rec1:
	    puntos.append(i)
	for i in self.cir:
	    puntos.append(i)
	for i in self.rec2:
	    puntos.append(i)
	return(puntos)
	
	
	

    def def_final(self,inicio):
	if inicio+200<=660 and inicio-200>=10:
	    fin=random.randint(inicio-200,inicio+200)
	else:
	    if inicio+200<=660:
		fin=random.randint(inicio,inicio+200)
	    elif inicio-200>=10:
		fin=random.randint(inicio-200,inicio)
		
	return(fin)
		

    def recta(self,x1,x2,y1,y2,inicio):
	p_inicio=[x1,y1]
	p_fin=[x2,y2]
	x,y,ind=ecuacion.ecuacion(p_inicio,p_fin)
	recta=ecuacion.c_puntos(inicio,y,x,ind,p_inicio,p_fin)
	return(recta)		
	
