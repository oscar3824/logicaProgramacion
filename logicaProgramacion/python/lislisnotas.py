listanotas=[]
definitiva=[]
notaApro=[]
notaRepro=[]
contA=0
contR=0
promedio=0
n=int(input("Ingrese numero de estudiantes: "))
for i in range (n):
    listanotas.append([])
    for j in range (3):
        if j==0:
            codigo=float(input("Ingrese codigo: "))
            listanotas[i].append(codigo)
        else:
            notas=float(input("Ingrese nota: "))
            listanotas[i].append(notas)
for i in range (n):
    suma=0
    contnotas=0
    for j in range (3):
        if j>0:
            suma=suma+listanotas[i][j]
            contnotas=contnotas+1
    suma=suma/contnotas
    definitiva.append(suma)
    promedio+=suma
for i in range (n):
    if definitiva[i]>3:
        contA+=1
        notaApro.append(definitiva[i])
    else:
        contR+=1
        notaRepro.append(definitiva[i])
print("\n")
print("Resultados")        
for i in range (n):
    print("Estuadiante",i)
    for j in range (n):
        if j==0:
            print("Codigo",listanotas[i][j], "Definitiva","{:,.1f}".format(definitiva[i]))
promedio=promedio/5
print('\n********************************')
print("Total aprobados:",contA)
print("Total Reprobados:",contR)
print("Promedio:","{:,.2f}".format(promedio))
print("Notas Aprobados:",notaApro)
print("Notas Reprobados:",notaRepro)