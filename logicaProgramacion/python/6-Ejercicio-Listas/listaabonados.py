'''
N personas 4
codigo=[1205,1206,1207,1208]
nombre=['Maria Luna','Pedro Suarez','Juan Ruiz','Sofia Garces']
impulsos=[10,20,30,40]
estrato=[1,2,3,4]
tarifbasica=[10000,15000,20000,25000]
         1->10000
         2->15000
         3->20000
         4->25000
         5->30000 
valorpagar=[10*100+10000,20*100+15000,30*100+20000,40*100+25000]
                0              1           2            4
valototal=valortotal+valorpagar[i]
'''
n=int(input('Ingrese numero de abonados a calcular :'))
codigo=[]
nombre=[]
impulsos=[]
estrato=[]
tarifabasica=[]
valorpagar=[]
valortotal=0
#Operacion de llenado de datos
for i in range(n):
    print('\nIngrese datos del Usuario ',i)
    codigo.append(int(input('Codigo :')))
    nombre.append(input('Nombre :'))
    impulsos.append(float(input('Impulsos :')))
    estrato.append(int(input('Estrato :')))
    print('================================\n')
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

#operacion
for i in range(n):
    valorpagar.append(tarifabasica[i]+impulsos[i]*100)
    valortotal=valortotal+valorpagar[i]

#Ciclo para impresion de datos
for i in range(n):
    print('\nInformacion cliente :',i)
    print('Codigo :',codigo[i])
    print('Nombre :',nombre[i])
    print('Estrato :',estrato[i])
    print('tarifabasica :',tarifabasica[i])
    print('valorpagar :',valorpagar[i])
    print('========================\n')

print('\n================================')
print('Estadistica de Salida')
print('Total abonados :',valortotal)



      
'''
print('--Impresion de las listas---')
print(codigo)
print(nombre)
print(impulsos)
print(estrato)
print(tarifabasica)
print('--tamaño---')
print(len(codigo))
print(len(nombre))
print(len(impulsos))
print(len(estrato))
print(len(tarifabasica))

'''


