import json
archivo='diccionario.json'
try:
    with open(archivo, 'r') as f:
        a=json.load(f)
except FileNotFoundError:
    diccionario={'1':'Lapiz','2':'Borrador','3':'Compas','4':'Portaminas'}
    with open(archivo,'w') as f:
        a=json.dump(diccionario,f)
else:
    print(a)
    print(a['2'])