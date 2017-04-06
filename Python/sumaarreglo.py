cs = [2,2,5,7,1000,1000]
y = len(cs)



print(cs)
su = 0

for i in range (0,y,1):
    
    if i == y-1:
        if(cs[i-1] == cs[i]):
            cs[i] = cs[i]+1
    else:
        if(cs[i] == cs[i+1]):
            cs[i+1] = cs[i+1]+1

    su = su + cs[i]
    
        
print(cs)
print('La suma es de: '+str(su))
