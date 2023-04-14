def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        fact=1
        for i in range(numero,1,-1):
            print(fact,'*',i,' :',fact*i)
            fact=fact*i  #4 #12
        return fact
def validarentero(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except ValueError:
            print('Debe ingresar un numero entero ')
    return dato
numero=validarentero('Ingrese numero :')
fact=factorial(numero)
print('El factorial de ',numero, ' es ',fact)