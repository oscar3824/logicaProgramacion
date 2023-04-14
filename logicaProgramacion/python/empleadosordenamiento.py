def ordenamiento(n,codigo,empleados,salariobasico,horastrabajadas,categoria,pagohoras):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if empleados[i]>empleados[j]:    #10 luis   20 Adriana
                t=codigo[i]
                codigo[i]=codigo[j]
                codigo[j]=t
                t=empleados[i]
                empleados[i]=empleados[j]
                empleados[j]=t
                t=salariobasico[i]
                salariobasico[i]=salariobasico[j]
                salariobasico[j]=t
                t=horastrabajadas[i]
                horastrabajadas[i]=horastrabajadas[j]
                horastrabajadas[j]=t
                t=categoria[i]
                categoria[i]=categoria[j]
                categoria[j]=t
                t=pagohoras[i]
                pagohoras[i]=pagohoras[j]
                pagohoras[j]=t
    return codigo,empleados,salariobasico,horastrabajadas,categoria,pagohoras
n=int(input('Ingrese numero de empleados :'))
codigo=[]
empleados=[]
salariobasico=[]
horastrabajadas=[]
categoria=[]
pagohoras=[]   # De acuerdo a la categoria horastrabajadas*valorhora
netopagar=[]   #Salario basico + pagohoras
totalnomina=0
#Ciclo de lectura
for i in range(n):
    print('Empleado nro :',i)
    codigo.append(int(input('Codigo :')))
    empleados.append(input('Nombre :'))
    salariobasico.append(float(input('Salario basico :')))
    horastrabajadas.append(int(input('horas trabajadas :')))
    categoria.append(int(input('Categoria :')))
    
#Ciclo operacion
#1:40000 2:60000 3:50000 4:0
for i in range(n):
    if categoria[i] ==1:
        valorhora=40000
    elif categoria[i] ==2:
        valorhora=60000
    elif categoria[i] ==3:
        valorhora=50000
    else:
        valorhora=0
    pagohoras.append(horastrabajadas[i]*valorhora)
    totalnomina=totalnomina+salariobasico[i]+pagohoras[i]

codigo,empleados,salariobasico,horastrabajadas,categoria,pagohoras=ordenamiento(n,codigo,empleados,salariobasico,horastrabajadas,categoria,pagohoras)

for i in range(n):
    print('Codigo :',codigo[i])
    print('Nombre :',empleados[i])
    print('Salario basico :',salariobasico[i])
    print('horas trabajadas :',horastrabajadas[i])
    print('categoria :',categoria[i])
    print('Pago Horas :',pagohoras[i])

print('\n Estadistica Final ')
print('Total nomina :',totalnomina)