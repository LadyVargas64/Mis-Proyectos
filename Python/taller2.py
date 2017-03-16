import math
#Primer Punto
print('~Problema en donde se tienen 3 numeros flotantes y los suma')
a = 1.2
b = 3.2
c = 4.5
print(a + b + c)
#Segundo Punto
print('----------------------------------------------------------')
print('')
print('~Imprime si un numero es mayor a 1000, menor a 500 o un numero entre 500 a 1000')
a = 654
if(a > 1000):
    print('Numero mayor a 1000')
elif(a > 500):
    print('Numero mayor a 500 y menor a 1000')
elif(a < 500):
    print('Numero menor a 500') 
#Tercer Punto
print('----------------------------------------------------------')
print('')
print('~Saber el area de un triangulo')
a=5
b=6
r=(a*b)/2
print ("El area del Triangulo es" +str (r))
#Cuarto Punto
print('----------------------------------------------------------')
print('')
print('~La hipotenusa de un triangulo con b = 2 y h = 2')
a = 2
b = (a**2) + (a**2)

raiz=math.sqrt(b)
print(raiz)
