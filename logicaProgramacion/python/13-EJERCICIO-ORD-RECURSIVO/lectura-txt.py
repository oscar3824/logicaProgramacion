from io import open
archivotxt=open("nombres.txt","r")
texto=archivotxt.read()
print(texto)
texto=archivotxt.close()

