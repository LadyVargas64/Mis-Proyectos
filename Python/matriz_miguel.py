print('Primer Punto')

a = input('Asignar el valor de la matriz')
b = int(a)
     
matriz = []

for i in range(b):
    matriz.append([])
    for j in range(b):
        matriz[i].append(1)
    print(matriz[i])

print('---------------------------------------------------')

print('Segundo Punto')

for x in range(b):
    print(matriz[x][x])

print('---------------------------------------------------')

print('Tercer Punto')

for t in range(b-1,-1,-1):
    print('-> Fila '+str(t))
    for v in range(b-1,-1,-1):
        print(matriz[t][v])
