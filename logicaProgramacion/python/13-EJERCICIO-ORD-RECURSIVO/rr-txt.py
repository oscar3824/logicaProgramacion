import os
f="nombres.txt"
if os.path.isfile(f):
    os.rename(f,"saludo.txt")
else:
    print("El archivo",f,"no existe ")
f="txt/test.txt"
if os.path.isfile(f):
    os.remove(f)
else:
    print("El archivo",f,"no existe ")