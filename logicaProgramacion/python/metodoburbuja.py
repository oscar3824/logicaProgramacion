def validardato(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except ValueError:
            print('Error!! has ingresado un dato que no es entero ')
    return dato

def validarnombre(etiqueta):
    while True:
        try:
            nombre=input(etiqueta)
            if nombre.isalpha():
                break
            else:
                print('Error!!!, debes ingreser datos alfabéticos ')
        except ValueError:
            print('')
    return nombre

def validardefinitiva(etiqueta):
    while True:
        try:
            dato=float(input(etiqueta))
            break
        except ValueError:
            print('Error!!! Debes digitar una nota en formato decimal ')
    return dato
def ordenarburbuja(codigo,nombre,definitiva):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if nombre[i]>nombre[j]:
                temp=nombre[i]
                nombre[i]=nombre[j]
                nombre[j]=temp
                temp=codigo[i]
                codigo[i]=codigo[j]
                codigo[j]=temp
                temp=definitiva[i]
                definitiva[i]=definitiva[j]
                definitiva[j]=temp
    return codigo,nombre,definitiva
n=validardato('Ingrese la cantidad de estudiantes :')
codigo=[]
nombre=[]
definitiva=[]
for i in range(n):
    id=validardato('Codigo :')
    codigo.append(id)
    nom=validarnombre('Nombre :')
    nombre.append(nom)
    nota=validardefinitiva('Definitiva :')
    definitiva.append(nota)

codigo,nombre,definitiva=ordenarburbuja(codigo,nombre,definitiva)
print(codigo)
print(nombre)
print(definitiva)