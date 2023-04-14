lista=[23,35,-8,45,74,1,25,45]
lista2=['lunes','martes','miercoles','jueves','viernes','sabado','domingo','marcos']
lista3=sorted(lista,reverse=False)
lista4=sorted(lista2,reverse=True)
#print(lista2)
#print(lista3)
#print(lista4)
listatuplas=[(5,3,8),(1,5,-3),(1,2,3),(7,4,-1)]
#listatuplascad=[('marcos','Luis','zulma'),('Juan','Maria','Sandra')]
#listuplaord2=sorted(listatuplascad,key=lambda x:x[2],reverse=False)
#listupordkey=sorted(listatuplas,key=lambda x:x[2],reverse=True)
listordkeysum=sorted(listatuplas,key=lambda x:sum(x),reverse=True)
#listuplaordcad=sorted(listatuplascad)
print('Tupla ordenada',listordkeysum)

diccionario=[{'nombre':'Juan','edad':25,'est':1.78},{'nombre':'Pedro','edad':42,'est':1.58},{'nombre':'Luis','edad':18,'est':1.89}]
print(diccionario)
diccionario2=sorted(diccionario,key=lambda x:x['edad'],reverse=False)
print(diccionario2)
