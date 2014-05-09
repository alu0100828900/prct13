#! encoding: UTF-8
import time
import timeit
import moduloPI
import matplotlib.pyplot as pl
start=time.time()
t=[]  
e=[]
y=[]
def error(n, k, umbral):
   contador=0
   for j in range (k):
     diferencia=moduloPI.aproximacion(n*(j+1))-moduloPI.PI
     if (abs(diferencia) < umbral):
       contador += 1
       
   return contador / float(k) * 100.0
t_upla=(10,50,100,150, 500, 550, 1000)
for v in t_upla:
  a=error(v,10,0.00001)
  e=e+[a]
  print "El porcentaje de error es de: %11.10f" %a
  finish=time.time()-start
  t=t+[finish]
print ('Los tiempos son:')
print t
for i in t_upla:
  y=y+[i]
print y
grafica2=pl.subplot(211)
pl.plot(t,y,'m',marker='h')
pl.xlabel('Tiempo')
pl.ylabel('Intervalos')
pl.title('Tiempo segun los intervalos')
pl.xlim(0.0, 0.5)
pl.ylim(0.0, 1500.0)
pl.legend(['Tiempos'], loc=4, numpoints=2)
grafica2=pl.subplot(212)
pl.plot(e,y,'c',marker='h')
pl.xlabel('Porcentaje de error')
pl.ylabel('Intervalos')
pl.title('Porcentaje de error segun los intervalos')
pl.xlim(0.0,110)
pl.ylim(-0.5,1500.0)
pl.legend(['Porcentajes'], loc=4, numpoints=2)
pl.savefig('figura.png',dpi=50)
pl.show()