def particion(lista):
    pivote=lista[0]
    print('Lista llegada ', lista,' pivote', pivote)
    menores=[]
    mayores=[]
    for i in range(1,len(lista),1):
        if lista[i]<pivote:
            menores.append(lista[i])
            print('menores ',menores)
        else:
            mayores.append(lista[i])
            print('mayores ',mayores)
    print('Envia ',menores,pivote,mayores)
    return menores,pivote,mayores

def quicksort(lista):
    if len(lista)<2:
        return lista
    else:
        menores,pivote,mayores=particion(lista)
        #print(menores,pivote,mayores)
        return quicksort(menores)+[pivote]+quicksort(mayores)

lista=[8,1,5,14,4,15,12,6,2,11,10,7,9]
#      * !!!!!!!!!!!!!!!!!!!!!!!!!!!!
print('Lista original ', lista)
lista=quicksort(lista)
print('Lista ordenada ',lista)