notas=[]
promedio=[]
suma=0
for i in range(2):
    notas.append([])
    for j in range(2):
        notas[i].append(float(input('Ingrese nota')))

for i in range(2):
    suma=0
    for j in range(2):
        suma=suma+notas[i][j]
    media=suma/2
    promedio.append(media)
    
for i in range(2):
    for j in range(2):
        print('[',i,'][',j,']',notas[i][j],end=' ') 
    print('\n')
    
print(notas)
print(promedio)
    