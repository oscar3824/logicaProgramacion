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

n=int(input('Ingrese el numero de abonados :'))
totalpagar=0
codigo=[]
nombre=[]
estrato=[]
tarifabasica=[]
impulsos=[]
valorpagar=[]
for i in range(n):
    print('\n Ingrese datos usuario :',i)
    codigo.append(input('Codigo :'))
    nombre=validarnombre()
    estrato=validarestrato()
    impulsos=validarimpulsos()
    if estrato[i]==1:
        tarifabasica.append(10000)
    elif estrato[i]==2:
        tarifabasica.append(15000)
    elif estrato[i]==3:
        tarifabasica.append(20000)
    elif estrato[i]==4:
        tarifabasica.append(25000)
    else:
        tarifabasica.append(30000)
#Calculos
for i in range(n):
    valorpagar.append(tarifabasica[i]+impulsos[i]*100)
    totalpagar=totalpagar+valorpagar[i]
#Impresion
for i in range(n):
    print('***Salida de datos ***')
    print('Informacion usuario :',i)
    print('Codigo :',codigo[i])
    print('Nombre :',nombre[i])
    print('Estrato :',estrato[i])
    print('Impulsos :',impulsos[i])
    print('Tarifa Basica :',tarifabasica[i])
    print('Total a Pagar $',valorpagar[i])
    print('**********************\n')
print('\n***Estadistica Total Cobrado ***')
print('Total cobrado :',totalpagar)