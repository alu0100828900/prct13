#!/usr/bin/python
#!encoding:UTF-8
PI = 3.1415926535897931159979634685441852
def aproximacion (nn):
  n =int(nn)
  sumatorio = 0.0
  for i in range (1, n+1):
    xi = (i-0.5)/float(n)
    fxi = 4/(1 + (xi**2))
    sumatorio += fxi
  c = sumatorio/float(n)
  return c
if __name__=="__main__":
   import sys
   if (len(sys.argv)==3):
    e1=int(sys.argv[1])
    e2=int(sys.argv[2])
   else:
    print "Debe escribir dos valores, como no lo ha hecho, ahora se ejecutará con los valores 10 10"
    e1=6
    e2=6
   l=[]
   for i in range(1,e2+1):
     e1=e1*i
     pi=aproximacion(e1)
     print "El valor aproximado de PI es: %.35f" % pi
     print PI
     l=l+[pi]
   print l 