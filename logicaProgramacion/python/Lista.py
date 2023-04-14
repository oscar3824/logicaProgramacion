def contarpalabras(nombre):
    cantpalabras=len(nombre.split())
    return cantpalabras
listanombres=[]
listapalabras=[]
nombre=input("Ingrese palabra: ")
while (nombre!="FIN"):
    listanombres.append(nombre)
    nombre=input("Ingrese palabras: ")
for x in listanombres:
    cantpalabras=contarpalabras(x)
    listapalabras.append(cantpalabras)
print (listanombres)
print(listapalabras)