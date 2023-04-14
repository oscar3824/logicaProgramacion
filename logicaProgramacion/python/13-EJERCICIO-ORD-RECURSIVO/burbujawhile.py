def ordenamiento(lista):
    num=len(lista)
    i=0
    while i<num:
        j=i
        while j<num:
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
            j+=1
        i+=1
    return lista
lista=[]
for i in range (5):
    numeros=int(input("Ingrese un dato a la lista: "))
    lista.append(numeros)
print('Lista original ',lista)
listaordenada=ordenamiento(lista)
print('Lista ordenada ',listaordenada)


#estado1='manzana' in ['manzana', 'pera','uva']
#variable=17.8
#print('El resultado es '+str(estado1)+' valores')