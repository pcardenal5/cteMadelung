def distancia(u,v):
    import math
    d=0
    for i in range (0,3):
        d=d+(u[i]-v[i])*(u[i]-v[i])
    return math.sqrt(d)

def escalar(u,v):
    return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]

def error(x):
    import math
    return math.erf(x)


def q(u):
    for i in range(0,len(u)):
        if(abs(u[i]%1/2)==0):
            return -1
        else:
            return 1

def cexp(x):
    import cmath
    import math
    return math.cos(x)+math.sin(x)*j

def redo(x,p):
    #Función redondeo, útil para eliminar problemas de punto flotante al hacer divisiones/raices cuadradas.
    return float(math.floor(p*x)/p)
    
import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

cont=2
rr=[]
red=[]
v=[]
p=[0,0,0]
k=[0,0,0]
v.append([1,0,0])
v.append([0,1,0])
v.append([0,0,1])
red.append([0,0,0])

while(len(red)<100):
    for i in range(0, len(red)):
        p[0]=red[i][0]
        p[1]=red[i][1]
        p[2]=red[i][2]
        for n in range(0,2):
            for j in range(0,len(v)):
                k[0]=p[0]+v[j][0]*(-1)**n
                k[1]=p[1]+v[j][1]*(-1)**n
                k[2]=p[2]+v[j][2]*(-1)**n
                if k not in red:
                    red.append(k)
                    k=[0,0,0]
#Aquí genero la red recíproca, que por sus características, es la msima red con un factor de escala que se tendrá en cuenta más adelante.
for i in range(0, len(red)):
    rr.append(red[i])
for i in range(0, len(red)):
    k[0]=red[i][0]+1/2
    k[1]=red[i][1]+1/2
    k[2]=red[i][2]+1/2
    red.append(k)
    k=[0,0,0]
#Ahora tenemos las coordenadas de los puntos de la red en todas las direcciones.
#Buscamos calcular la distancia de cada uno de los puntos de la celda unidad a todos estos puntos de la red.


#Aquí se calculan los primeros vecinos de la red normal.
v.append([1/2,1/2,1/2])
v.append([1,1,0])
v.append([0,1,1])
v.append([1,0,1])
v.append([1,1,1])
d=[]
dmin=10
vecinos=[]
vecinos2=[]
a=0
for i in range(0,len(v[a])):
    v[a][i]=0

for i in range(0,len(red)):
    if(distancia(v[a],red[i]) not in d and distancia(v[a],red[i])!=0):
       d.append(distancia(v[a],red[i]))
d.sort()
for i in range(0,len(red)):
    if(distancia(v[a],red[i])<=d[cont] and distancia(v[a],red[i])!=0):
        vecinos.append(red[i])
vecinos2=[[0,0,0],[1/2,1/2,1/2]]







#Aquí se calculan los vecinos de la red recíproca.
k=[]
kd=[]
k.append([1,0,0])
k.append([0,1,0])
k.append([0,0,1])
k.append([1,1,0])
k.append([0,1,1])
k.append([1,0,1])
k.append([1,1,1])
kvecinos=[]
kvecinos2=[]
dmin=10
b=a

for i in range(0,len(k[b])):
    k[b][i]=0
    
for i in range(0,len(rr)):
    if(distancia(k[b],rr[i]) not in kd and distancia(k[b],rr[i])!=0):
       kd.append(distancia(k[b],rr[i]))
kd.sort()
for i in range(0, len(rr)):
    if (distancia(k[b],rr[i])<=kd[cont] and distancia(k[b],rr[i])!=0):
        kvecinos2.append(rr[i])

vecinos2=[[0,0,0],[1/2,1/2,1/2]]

#La información de los vecinos se guarda en vecinos2 y kvecinos2. Ahora es cuestión de hacer las sumas, teniendo en cuenta las dimensiones.
suma=0
for k in range(0, len(kvecinos2)):
    for i in range(0,len(vecinos2)):
        suma=suma+q(vecinos2[i])*cexp(2*math.pi*escalar(vecinos2[i],kvecinos2[k]))
    suma=suma*math.exp(-3*((math.pi)**2)*escalar(kvecinos2[k],kvecinos2[k])/16)/escalar(kvecinos2[k],kvecinos2[k])
    suma=suma*cexp(-2*math.pi*escalar(kvecinos2[k],v[a]))

suma=suma/(math.pi)+8*q(v[a])/(math.sqrt(3*math.pi))

for i in range(0, len(vecinos)):
    suma=suma+q(vecinos[i])*(1-error(4*distancia(v[a],vecinos[a])/(math.sqrt(3))))/distancia(v[a],vecinos[a])  

print("El potencial en la posición",v[a], "vale", str(redo(suma.real,1000))+"/a","luego la constante de Madelung es",redo(d[0]*suma.real,1000))

#Graficador de puntos
#fig = plt.figure(figsize=(4,4))
#ax = fig.add_subplot(111, projection='3d')
#for i in range(len(red)):
#    if (abs(red[i][0]%1/2)==0 or abs(red[i][1]%1/2)==0 or abs(red[i][2]%1/2)==0):
#        ax.scatter(red[i][0],red[i][1],red[i][2],c="blue")
#    else:
#        ax.scatter(red[i][0],red[i][1],red[i][2],c="red")
#plt.show()


