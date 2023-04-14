def ordenamiento (lista):
    num=len(lista)
    i=0
    while i<num:
        j=i
        while j<num:
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
                print(lista)
        j+=1
    i+=1
    return lista
lista=[]
n=int(input("Numero de datos"))
for i in range (n):
    lista.appendint(int(input("Ingrese numero")))
print('Lista original ',lista)
listaordenada=ordenamiento(lista)
print('Lista ordenada ',listaordenada)