#a={'nombre':'Alfredo','edad':35,'email':'alfredo@gmail.com','despacho':258}
#print(a['nombre'])
#print(a['edad'])
#a['edad','email'] = 258
#a['despacho']=[300,200,'hola']
#print(a['despacho'][1])
a={'nombre':'Alfredo','edad':35,'a-email':'alfredo@gmail.com','despacho':258}
b={28:'Alfredo',2:218,445:'correo@gmail.com'}
c={'nombre':'Juan Manuel','Automovil':True,'email2':'alfredo2@gmail.com',25:'Hola'}
d={25:'Pedro',35:'Juan',45:'Sofia'}

#print(a['edad'])
#print(a.get('edad','No existe esta clave'))
#valor=a.get('despacho','No existe')
#print(valor)
#Funciones sobre diccionarios
#print(len(d))
#print(min(a))
#print(sum(d))

#Funciones para acceso a los elementos de un diccionario
estado='a-email' in a
#print(estado)
#listaclaves=a.keys()
#print(listaclaves)
#listavalores=a.values()
#print(listavalores)
#listaitems=a.items()
#print(listaitems)
#a['estatura']=1.80
#print('Agregar clave y dato ',a)
#a.update(c)
#print(a)
#posicion=d.pop(75,'Clave no encontrada')
#print(d)
#print(posicion)
#del d[45]
#print(d)
#b.clear()
#print(b)
#a.popitem()
#print(a)

frutas={'Manzana':5000,'Pera':4500,'Uva':2500,'Limon':3000} #Valores kilogramo
fruta=input('¿Que fruta vas a comprar? :').title()  #manzana --> Manzana --> Uva
kg=float(input('Cuantos kilos va a comprar :'))
if fruta in frutas:
    print(kg,' Kilos de ',fruta,' valen :',frutas[fruta]*kg,' $')
else:
    print('Lo siento la fruta ',fruta,' No existe en la tabla de precios ')
""""
curso={'Matematicas':5,'Fisica':8,'Calculo':3,'Python':4}
totalcreditos=0
for materia, creditos in curso.items():
    print(materia,' tiene ',creditos,' creditos')
    totalcreditos=totalcreditos+creditos

print('El total de creditos es :',totalcreditos)
"""





