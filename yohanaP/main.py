from cont import Generador

listaItems = ["uno", "dos", "tres"]
miGenerador = Generador()

print(miGenerador.generaTitPar("Hola", "Mundo"))

n = open("item.csv", "r")
print(miGenerador.generaLista(n))

m = open("item.csv", "r")
print(miGenerador.generaTable(m))