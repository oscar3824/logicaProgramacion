
def busq_bin_recursive(vector,elemento,izq,der):
    if izq>der:
        return -1
    med=(izq+der)//2
    if vector[med]==elemento:
        return med
    elif vector[med]>elemento:
        return busq_bin_recursive(vector,elemento,izq,med-1)
    else:
        return busq_bin_recursive(vector,elemento,med+1,der)
def validarentero(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except ValueError:
            print('Debe ingresar un valor entero ')
    return dato
vector=[]
izq=0
der=len(vector)-1
n=validarentero("Ingrese nuemero de datos en la lista:")
for i in range (n):
    numero=validarentero("Ingrese numero:")
    vector.append(numero)
elemento=validarentero('Ingrese numero a buscar :')
while elemento!=99:
    if busq_bin_recursive(vector,elemento,izq,der)==-1:
        print('El numero ',elemento,' No fue localizado en la lista')
    else:
        print('El numero ',elemento,' se encuentra en la posicion ',busq_bin_recursive(vector,elemento,izq,der))
    elemento=validarentero('Ingrese numero a buscar :')