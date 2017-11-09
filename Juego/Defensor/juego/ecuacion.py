import math



def simplificar(num,deno):
    c=2
    mayor=0
    div=1
    
    if(abs(num)>abs(deno)):
        mayor=abs(num)
    else:
        mayor=abs(deno)
        
    
    while(c<=mayor):
        if(num%c==0 and deno%c==0):
            if(c>div):
                div=c

        c+=1

    return(div)




def hallar_p(a,b):
    n_pendiente=a[1]-b[1]
    d_pendiente=a[0]-b[0]
    
    if(n_pendiente<0 and d_pendiente<0):
	n_pendiente=n_pendiente*-1
	d_pendiente=d_pendiente*-1
	
    div=simplificar(n_pendiente,d_pendiente)
    if div!=1:
	n_pendiente=n_pendiente/div
	d_pendiente=d_pendiente/div
    
    
    pendiente=[n_pendiente,d_pendiente]
    
    return(pendiente)
    
    




def ecuacion(a,b):
    pendiente=hallar_p(a,b)
    y=[pendiente[1],1]#variable y lado izquierdo de la igualdad
    x=[pendiente[0],1]#variable x ladoderecho de la igualdad
    primero=(pendiente[0])*-(a[0])#lado derecho
    segundo=((-a[1])*(-1))*(pendiente[1])#lado izquierdo al lado derecho
    ind=primero+segundo #lado derecho
    #y[0]=y[0]*-1#cambiamos al lado izquierdo
    ind= ind*-1 #cambiamos al lado izquierdo
    
    if x[0]<0:
	x[0]=x[0]*-1
	y[0]=y[0]*-1
	ind=ind*-1
	
    return(x,y,ind)

 
 


def c_puntos(inicio,y,x,ind,a,b):
    ini_y=inicio
    puntos=[a]
    for i in range(0,12):
	ini_y+=10
	y[1]=ini_y
	x_val=(y[0]*y[1])+ind
	x_val=int(math.ceil(float(x_val)/float(x[0])))
	puntos.append([x_val,ini_y])

    puntos.append(b)
    return(puntos)







def es_intervalo(pos,limites):
    res=False
    if (pos>limites[0] and pos<limites[1]):
	res=True
    return(res)
    
    




 
