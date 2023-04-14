def validarentero(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except ValueError:
            print('Debe ingresar un numero entero')
    return dato

def busquedabinaria(vector,buscar):
    posiciones=[]
    izq=0
    der=len(vector)-1
    while izq<=der:
        med=(izq+der)//2
        if vector[med]==buscar:
            posiciones.append(med)
            return med
        elif vector[med]>buscar:
            der=med-1
        else:
            izq=med+1
    return -1

vector=[1,2,3,4,5,6,6,7,8,9,10]
#       0 1 2 3 4 5 6 7 8 9 10 11  
buscar=validarentero('Ingrese numero a buscar :')
while buscar!=0:
    if busquedabinaria(vector,buscar)==-1:
        print('El elmento ',buscar,' No fue localizado en la lista')
    else:
        print('El elemento ',buscar,' se encuentra en la posicion',busquedabinaria(vector,buscar))
    buscar=validarentero('Ingrese numero a buscar :')
