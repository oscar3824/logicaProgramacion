from io import open
archivo=open("datos.txt","w")
n=int(input("Ingrese numero de usuarios: "))
for i in range(n):
    nombres=input("Ingrese nombre: ")
    archivo.write("\n""Nombre: "+nombres)
    edad=input("Ingrese su edad: ")
    archivo.write(str("\n""Edad:"+edad))
    if edad>"18":
        estado=(" eres mayor de edad")
        archivo.write("\n"+estado)
    else:
        estado=(" eres menor de edad")
        archivo.write("\n"+estado)    
archivo.close()


