import json

with open('diccionario.json') as archivo:
    diccionario=json.load(archivo)   
archivo.close()

print(diccionario)

print(diccionario['3'])
