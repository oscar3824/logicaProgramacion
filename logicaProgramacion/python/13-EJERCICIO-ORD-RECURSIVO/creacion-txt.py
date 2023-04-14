from io import open
archivotxt=open("nombres.txt","w")
nombres=("juan\npedro\nmazana\n8")
archivotxt.write(nombres)
archivotxt.close()