import json

with open('lista.json') as archivo:
    lista=json.load(archivo)   
archivo.close()

print(lista)

for i in range(len(lista)) :
    print(lista[i])

                    