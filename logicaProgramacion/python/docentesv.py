n=int(input("Ingrese numero de docente :"))
totalHonorarios=0
contA=0
contB=0
contC=0
for i in range(n):
    documento=input("Ingrese documento :")
    nombre=input("Ingrese nombre :")
    categoria=input("Ingrese categoria (A,B,C) :")
    horasLaboradas=int(input("Ingrese horas laboradas :"))
    if categoria=="A":
        valorHora=25000
        contA=contA+1
    elif categoria=="B":
         contB=contB+1
         valorHora=35000
    else:
         valorHora=50000
         contC=contC+1
    valorPagar=horasLaboradas*valorHora
    totalHonorarios=totalHonorarios+valorPagar
    print('\n********************************')
    print("Documento del docente :",documento)
    print("Nombre del docente :",nombre)
    print("Valor a pagar al docente :",valorPagar)
print('\n********************************')    
print("Total honorarios:",totalHonorarios)
print("Total docentes categoria A :",contA)
print("Total docentes categoria B :",contB)
print("Total docentes categoria A :",contC)