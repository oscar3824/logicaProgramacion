def factorialrecursivo(numero):
    if numero == 0 or numero == 1:
        print('numero se cumple ',numero)
        return 1
    else:
       print('numero ',numero)
       return numero*factorialrecursivo(numero-1)
def validarentero(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except ValueError:
            print('Debe ingresar un numero entero ')
    return dato
numero=validarentero('Ingrese numero :')
fact=factorialrecursivo(numero)
print('El factorial de ',numero, ' es ',fact)