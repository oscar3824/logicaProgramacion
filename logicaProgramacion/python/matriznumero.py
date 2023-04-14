def validardato(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except ValueError:
            print(etiqueta,'Debes ingresar un numero entero')
    return dato
filas=int(input('De cuantas filas es la matriz :'))
columnas=int(input('De cuantas columnas :'))
numeros=[]
listapares=[]
listaimpares=[]
edadmedia=[]
edadmenor=[]
edadmayor=[]
contP=0
contI=0
contmayor=0
contmenor=0
contmedia=0
#Ciclo de Lectura de la matriz
for i in range(filas):
    numeros.append([])
    for j in range(columnas):
        numero=validardato('Ingrese un numero :')
        numeros[i].append(numero)
for i in range(filas):
    for j in range(columnas):
        if numeros[i][j]>60:
            contmayor+=1
            edadmayor.append(numeros[i][j])
        elif numeros[i][j]<=18:
            contmenor+=1
            edadmenor.append(numeros[i][j])
        else:
            contmedia+=1
            edadmedia.append(numeros[i][j])
#Ciclos de operacion
for i in range(filas):
    for j in range(columnas):
        if numeros[i][j]%2==0:
            contP=contP+1
            listapares.append(numeros[i][j])
            #print('Es par :',numeros[i][j])
        else:
            contI+=1
            listaimpares.append(numeros[i][j])
            #print('Es Impar :',numeros[i][j])
#Ciclo de impresión
print('\n**********************')
print("Matriz")
for i in range(filas):
    for j in range(columnas):
        print(numeros[i][j],end=' ')
        #'[',i,'][',j,']:',
    print('\n*****')
print('Estadistica ')
print('Total de Pares ',contP)            
print('Total de Impares ',contI)  
print('Lista de pares ',listapares)  
print('Lista de Impares ',listaimpares) 
print('\n**********************')
print('Lista de menor o igual a 18 ',edadmenor)  
print('Lista de mayor a 60 ',edadmayor)  
print('Lista entre 18 y 60',edadmedia)   
print("Menores de 18:",contmenor) 
print("Mayores de 60:",contmayor) 
print("Entre 18 y 60:",contmedia) 

""""" print('\nLista pares / Impares por ciclo ')
for i in range(len(listapares)):
    print('[',i,']:',listapares[i],end=' ')
print('\n')
for i in range(len(listaimpares)):
    print('[',i,']:',listaimpares[i],end=' ')"""