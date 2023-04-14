import json
lista=[10,20,30,40,50]

#Fase de apertura y creación
with open('lista.json','w') as archivo:
    json.dump(lista, archivo)
archivo.close()


diccionario={'1':'Lapiz','2':'Borrador','3':'Compas','4':'Portaminas'}
with open('diccionario.json','w') as archivo:
    json.dump(diccionario, archivo)
archivo.close()


