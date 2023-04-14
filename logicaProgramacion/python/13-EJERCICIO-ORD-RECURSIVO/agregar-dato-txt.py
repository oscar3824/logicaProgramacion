from io import open
archivotxt=open("datos.txt","a")
nombre="\nManuella Rojas"
archivotxt.write(nombre)
archivotxt.close()

from io import open
with open ("./nombres.txt") as archivo:
    lineas=archivo.read()
    print(type(lineas))
    print(lineas)
archivo.close()

f=open("./nombres.txt")
filas=f.readlines()
print(filas[4][2:4])
f.close()