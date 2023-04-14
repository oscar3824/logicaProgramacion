def cuentaregresiva(num):
    num=num-1
    if num>0:
        print(num)
        cuentaregresiva(num)
    else:
        print('!Booooommmmmm!')
    print(' Fin de la funcion ',num)

cuentaregresiva(10)