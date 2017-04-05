class nodo:
    def __init__(self,p,s):
        self.p = p
        self.s = s
        
class lista: 
    def __init__(self,nodo):
        self.nodo = nodo
    def add(self,nodo):
        nd = nodo('s','a')
        
nodo = nodo("a","b")
lista = lista(nodo)


v = 'casjbduiabscoabcabc'

print(str.find(v, 'bd'))
print(str.upper(v))
print(str.capitalize(v))
print(str.count(v, "ca"))
