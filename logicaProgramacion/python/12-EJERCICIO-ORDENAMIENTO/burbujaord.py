def validar_entero(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except ValueError:
            print('has ingresado un dato que no es entero ')
    return dato

def ordenarburbuja(numeros):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if numeros[i]>numeros[j]:
                temp=numeros[i]
                numeros[i]=numeros[j]
                numeros[j]=temp
    return numeros       

n=validar_entero('Ingrese los elmentos de la lista ')
numeros=[]
for i in range(n):
    num=validar_entero('Ingrese numero entero :')
    numeros.append(num)

numeros=ordenarburbuja(numeros)
print(numeros)    