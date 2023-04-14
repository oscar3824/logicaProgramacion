nombre=input("Ingrese nombre")
while True:
    try:
        estrato=int(input("Ingrese estrato entre(1,2,3,4,5)"))
        if estrato<1 or estrato>5:
            print("Te has salido del rango de los estratos")
            continue
        break
    except ValueError:
        print("ojo error en el tipo de dato de estratos")

if (estrato==1):
    tarifaBasica=1000
elif(estrato==2):
    tarifaBasica=15000
elif(estrato==3):
    tarifaBasica=30000
elif(estrato==4):
    tarifaBasica=50000
else:
    tarifaBasica=65000
print('\n********************************')
print('Nombre del usuario:',nombre) 
print('Estrato:',estrato) 
print('Tarifa basica:',tarifaBasica)    