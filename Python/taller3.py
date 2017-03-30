import math
#Pasar Centimetros cubicos a litros
print('Pasamos 50 cn3 a litros')
cm3 = 50.0
r = cm3 / 1000

print(str(cm3)+' cm3 equivalen a '+str(r)+' litros')
print('------------------------------------------------')
print('------------------------------------------------')
#Volumen de un cilindro
print('El volumen de un cilindro')
r = 12
h = 6
p = math.pi

print(p * r**2 * h)
print('------------------------------------------------')
print('------------------------------------------------')
#Prestar el servicio militar
print('Servicio Militar')
e = 18
c = 1
pt = 1
g = 1
u = 1

if(e >= 18):
    if(c == 1):
        if(pt == 1):
            if(g == 1):
                if(u == 1):
                    r = 1
if(r == 1):
    print('Tiene que prestar servicio militar')
else:
    print('No tiene que prestar servicio militar')
print('------------------------------------------------')
print('------------------------------------------------')
#Clima
print('Clima')
p = 's'
f = 'n'

if(p == 'll' or p == 't' ):
    print('Tienes que llevar paraguas')
elif(p == 's' or p == 'n'):
    if(f == 't' or f == 'll'):
        print('Tienes que llevar paraguas')
    else:
        print('No te preocupes no va llover')




