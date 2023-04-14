def funContarpalabras(valor):
    cant_palabras=len(valor.split())
    return cant_palabras

listanombres=[]
contarpalabras=[]
nombre=input('Escriba la primera palabra/s :')
#Llenar la lista
while nombre!='FIN': #bandera
    listanombres.append(nombre)
    nombre=input('Escriba la primera palabra/s :')

#Proceso
for valor in listanombres:
    contapalabra=funContarpalabras(valor)
    contarpalabras.append(contapalabra)
    
#Imprimir 
print(listanombres)
print(contarpalabras)

