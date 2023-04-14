import os
contenido=os.listdir("./prueba/prueba 2")
print(contenido)
ruta=os.getcwd()
print(ruta)

os.chdir("./prueba/prueba 2")
ruta=os.getcwd()
print(ruta)

os.rmdir("./pruba3")