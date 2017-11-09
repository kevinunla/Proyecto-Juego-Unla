import pygame

import pygame
from pygame.locals import*



pygame.init()
resolucion=(1000,628)#896,628
ventana=pygame.display.set_mode(resolucion)
fondo=pygame.Surface(resolucion)



aux="imagenes/"
ext=".png"


#icono=pygame.image.load("ico.png")
villanos=[pygame.image.load(aux+"villanos/"+str(i)+ext) for i in range(1,5)]# 
mina=[pygame.image.load(aux+"mina/"+str(i)+ext) for i in range(1,4)]# 
img_kamikazes=[pygame.image.load(aux+"inv/"+str(i)+ext) for i in range(1,5)]#
mine=[pygame.image.load(aux+"minero/"+str(i)+ext) for i in range(1,5)]#
bombardero_=[pygame.image.load(aux+"bombardero/"+str(i)+ext) for i in range(1,5)]#
i_bomba=[pygame.image.load(aux+"bomba/"+str(i)+ext) for i in range(1,4)]#
i_linea=[pygame.image.load(aux+"linea/"+str(i)+ext) for i in range(1,4)]#
i_misil=[pygame.image.load(aux+"misil/"+str(i)+ext) for i in range(1,4)]#
i_escudo=[pygame.image.load(aux+"escudo/"+str(i)+ext) for i in range(1,5)]#
i_vida=[pygame.image.load(aux+"vida/"+str(i)+ext) for i in range(1,4)]#
m_plateado=[pygame.image.load(aux+"m_plateado/"+str(i)+ext) for i in range(1,13 )]#
esc_nave=[pygame.image.load(aux+"esc/"+str(i)+ext) for i in range(1,4)]#
bm_b=[pygame.image.load(aux+"bomb/"+str(i)+ext) for i in range(1,3)]#
numeros=[pygame.image.load(aux+"let_num/numeros/"+str(i)+ext) for i in range(0,12)]#
numeros_nivel=[pygame.image.load(aux+"let_num/numeros_nivel/"+str(i)+ext) for i in range(1,12)]#
nave_=[pygame.image.load(aux+"nave/"+str(i)+ext) for i in range(1,3)]#
misil=pygame.image.load(aux+"bala"+ext)#
m_fin=pygame.image.load(aux+"esm"+ext)#
paralisis=pygame.image.load(aux+"linea"+ext)#
bon=pygame.image.load(aux+"bon"+ext)
barra_estado=[pygame.image.load(aux+"barra/"+str(i)+ext) for i in range(1,5)]
img_basura=[pygame.image.load(aux+"basura/"+str(i)+ext) for i in range(1,3)]
barra_minero=[pygame.image.load(aux+"minero/"+str(i)+ext) for i in range(5,10)]


img_tablero=pygame.image.load(aux+"tab3.png")
img_p=pygame.image.load(aux+"pausa.png")
img_e=pygame.image.load(aux+"exp3.png")
img_per=pygame.image.load(aux+"perdiste.png")
img_n=pygame.image.load(aux+"nivel2.png")
img_pre=pygame.image.load(aux+"preparate.png")
img_canon=pygame.image.load(aux+"minero/canon_mal2.png")
img_bala=pygame.image.load(aux+"minero/bala_mal.png")
ayuda_=pygame.image.load(aux+"ayuda.png")

disparo= pygame.mixer.Sound('disparo.wav')
son_explosion=pygame.mixer.Sound('explosion.wav')
lazer=pygame.mixer.Sound('Lazer.wav')
son_fondo=pygame.mixer.Sound('fondo.wav')
son_malo=pygame.mixer.Sound('malo.wav')
son_kamikaze=pygame.mixer.Sound('scifi072.wav')
son_marcianos=pygame.mixer.Sound('marcianos.wav')
menu=pygame.image.load(aux+"menu.png")
flecha_menu=pygame.image.load(aux+"flecha.png")
confirma=pygame.image.load(aux+"conf.png")
apuntador=pygame.image.load(aux+"apuntador.png")
creditos_=pygame.image.load(aux+"creditos.png")
felicidades=pygame.image.load(aux+"felicidades.png")
