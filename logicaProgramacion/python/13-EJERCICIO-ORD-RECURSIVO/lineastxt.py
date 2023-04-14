from io import open
archivotxt=open("nombres.txt","r")
lineas=archivotxt.readlines()
archivotxt.close()
print(lineas)
for i in range(len(lineas)):
    print("linea",i,":",lineas[i])