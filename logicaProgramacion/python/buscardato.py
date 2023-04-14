def validarentero(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except ValueError:
            print('Has ingresado un dato no valido')
    return dato
def buscardato(numeros,buscar):  #[25,31,32,33,45,32,28,32] , 32
    posiciones=[] 
    bandera=-1 
    for i in range(n):
        if numeros[i]==buscar:
           posiciones.append(i)
           bandera=1     
    if bandera==1:
        return posiciones
    return-1
n=validarentero('Ingrese cantidad de elementos de la lista ')
numeros=[]
for i in range(n):
    numero=validarentero('Ingrese un valor de la lista :')
    numeros.append(numero)
buscar=validarentero('Ingrese elemento a buscar en la lista :')
posicion=buscardato(numeros,buscar)
if posicion==-1:
    print('El numero ',buscar,' No se encuentra en la lista ')
else:
    print('El numero ',buscar,' se encuentra en la posicion ',posicion)
    print('El numero ',buscar," se encuentra", len(posicion),"veces en la lista")
print(numeros)
