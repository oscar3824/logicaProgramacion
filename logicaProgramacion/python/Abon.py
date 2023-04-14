def validarestrato():
    while True:
        try:
            estrato=int(input("Ingrese el estrato entre(1,2,3,4,5)"))
            if estrato<1 or estrato>5:
                print("Te has salido del rango de estratos")
                continue
            break
        except ValueError:
            print("Debes ingresar un valor numerico entre 1y 5")
    return estrato 
def validarimpulsos():
    while True:
        try:
            impulsos=int(input("Ingrese el numero de impulsos entre(10 a 500)"))
            if impulsos<10 or impulsos>500:
                print("Te has salido del limite de impulsos")
                continue
            break
        except ValueError:
            print("Debes ingresar un dato valido para impulsos")
    return impulsos   
def validarnombre():
    while True:
        nombre=str(input('Ingrese el nombre del usuario: '))
        if not nombre.isalpha():
            print('nombre erroneo, por favor utilizar solo letras')
            continue
        break
    return nombre 
    
def calculoabonados(estrato,impulsos):
    if estrato==1:
        tarifabasica =10000
    elif estrato==2:
        tarifabasica =15000
    elif estrato==3:
        tarifabasica =20000
    elif estrato==4:
        tarifabasica =25000
    else:
        tarifabasica =30000
    consumo=impulsos*100
    valorcobrar=tarifabasica+consumo
    return valorcobrar

totalabonados=0
n=int(input('Ingrese usuarios a leer en el sistema : '))
for indice in range(n):
    nombre=validarnombre()
    estrato=validarestrato()
    impulsos=validarimpulsos()
    valorcobrar=calculoabonados(estrato, impulsos)
    totalabonados=totalabonados+valorcobrar
    print('\nDatos usuario :',indice)
    print('Nombre :',nombre)
    print('Estrato :',estrato)
    print('Valor a cobrar :',valorcobrar)
    print('============================\n')
print('\n===Estadistica total Cobrado ===\n')
print('Total cobrado :',totalabonados)
print('============================\n')