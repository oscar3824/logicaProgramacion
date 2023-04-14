'''Crear un programa lea desde teclado nombre y edad de una persona,
  lo vaya almacenando en una lista, y para cada persona en un diccionario
  finalmente lo envie a un achivo tipo json
  numero de persona 3

1) codigo de importacion
2) Crear una lista vacia
3) Crear un for 
4)   un diccionario vacio
5)   Lectura nombre, edad
6)   enviar los datos al diccionario
7)   enviar los datos a la lista
8) Ejecutar las instrucciones para almacenar los datos en JSON

'''
import json
base_de_datos=[]
n=int(input("Ingrese numero de usuarios: "))
for i in range(n):
    persona={}
    nombre=input('Ingrese el nombre :')
    edad=int(input('Ingrese su edad :'))
    estatura=float(input('Ingrese su estatura :'))
    persona['nombre']=nombre
    persona['edad']=edad
    persona['estatura']=estatura
    base_de_datos.append(persona)
print(base_de_datos)
with open('registro_personas.json','w') as archivo:
    json.dump(base_de_datos,archivo)
    print(' Archivo generado con exito....')
    



