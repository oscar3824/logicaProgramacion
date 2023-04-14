#from calendar import c
#from cmath import e
#import contextlib

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
    cont=0
    for i in range(n):
        if numeros[i]==buscar:    
            posiciones.append(i)
            bandera=1
            cont+=1        
    if bandera==1:
        return posiciones,cont
    else:
        return bandera,cont
  
n=validarentero('Ingrese cantidad de elementos de la lista ')
numeros=[]

for i in range(n):
    numero=validarentero('Ingrese un valor de la lista :')
    numeros.append(numero)

buscar=validarentero('Ingrese elemento a buscar en la lista :')
posicion,contador=buscardato(numeros,buscar)

if posicion==-1:
    print('El numero ',buscar,' No se encuentra en la lista ')
    print('El contador equivale a: ',contador)
else:
    print('El numero ',buscar,' se encuentra en la posicion ',posicion)
    print('Cantidad de veces encontrado el número',buscar,': ',contador)

print(numeros)