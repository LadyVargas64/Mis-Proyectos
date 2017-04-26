#Lady Yohana Vargas Gonzalez
print('Muestra una matriz de tamano dado por el usuario')

n = input('Ingrese tamano de matriz')

try:
    k = int(n)
    while k >100:
        n = input('Numero mayor a 100. Ingrese tamano de matriz')
        k = int(n)
        
    matriz = []

    for i in range(k):
        matriz.append([])
        for j in range(k):
            matriz[i].append(1)
        print(matriz[i])
        
    print('---------------------')
    print('---------------------')
    print('Muestra con el contenido diagonal')
    

    for x in range(k):
        print(matriz[x][x])
    print('---------------------')
    print('---------------------')
    print('Muestra la matriz comenzando desde la ultima posicion')
    
    for t in range(k-1,-1,-1):
        print('-> Fila '+str(t))
        for v in range(k-1,-1,-1):
            print(matriz[t][v])
    c = ''
except:
    c = 'No es un Numero'
print(c)
