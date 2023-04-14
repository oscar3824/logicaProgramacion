from io import open
f=open("./txt/test.txt","w")
f.write("Esta es la primera linea")
f.write("\nEsta es la segunda linea")
f.write("\nEsta es la tercera linea")
nombres=input("Ingrese nombre: ")
edad=input("Ingrese su edad: ")
cadena="\nEl nombre es "+nombres+" tu edad es "+edad+" anyos"
lista=list(range(10))
for i in range(10):
    lista[i]=i
    f.write(str(lista[i])+"\n")
f.write(cadena)
f.write(str(lista))
f.close()

f1=open("txt/test.txt","a")
for i in range(10):
    f1.write("Esta es la fila"+str(i)+"\n")
f1.close()
