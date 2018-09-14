#Edgar Efren Tomay Tiburcio
#14 de septiembre de 2018
#Polinomio de Legendre

def PolinomioLegendre(n,x):
  if n==0:
     return 0
  elif n==1:
     return x
  else:
     return(((2*n-1)/n*PolinomioLegendre(n-1,x))-(((n-1)/n)*PolinomioLegendre(n-2,x)))

n =int(input("ingresa el valor de n: "))
x=float(input("ingresa el valor de x: "))


if (x > -1 and x < 1):
  print('El polinomio para P(n) es:', PolinomioLegendre(n,x))
else:
  print('Favor de ingresar un valor entre [-1, 1]')
