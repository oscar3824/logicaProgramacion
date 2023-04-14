#lista=[25,42,3,-8,44,15,55]
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
n=int(input('Ingrese numero de datos:'))
for i in range(n):
    lista.append(int(input('ingrese un numero entero:')))
print('Lista original ',lista)
listaordenada=ordenamiento(lista)
print('\nLista ordenadas ',listaordenada)