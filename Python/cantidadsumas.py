x = '999577'
lon = len(x)
y = 0
s = 0
n = 0
c = 0
if(lon == 1):
    print('El numero es solo de un digito')
    c = 0
elif(lon > 7):
    print('El numero supera los 7 digitos')
else:
    while lon > 1:
        for i in x:
            z = int(i)
            
            if y != 0:
                s = s + 1
            
            y = y + z 
            lon = len(str(y))
            
            x = str(y)
        n = n + 1
        print 'Cifra numero '+str(n)+' : '+str(y) 
        y = 0
        
print('El numero de sumas que realiza es de: '+str(s+c))
