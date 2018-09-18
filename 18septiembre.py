#Edgar Efren Tomay Tiburcio
#18 de septiembre de 2018
#Cuadratura de Gauss - Legendre


import numpy as np

def function(x):
  return x

def integral(n,liminf,limsup):
  xi, weights = np.polynomial.legendre.leggauss(n)
  numericalintegral=0
  for i in range(0,n):
    numericalintegral=numericalintegral+weights[i]+function((limsup-liminf)/2*xi[i]+(limsup+liminf)/2)
  return 2.0*numericalintegral

grado=2
print(integral(grado,1.0,5.0))
