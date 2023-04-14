articulos={}
valores={}
continuar=True
n=int(input('Ingrese cantidad de articulos comprados :'))
for i in range (n):
while continuar:
    clave=input('Ingrese valor clave :')   #cedula
    dato=int(input(clave+':'))    #cedula : 6954546
    persona[clave]=dato
    print(persona)
    continuar=input('¿Quieres añadir mas informacion (Si/No) ?')=="Si"

#Creado los diccionario
articulos={1:'Lapiz', 2:'Cuaderno', 3:'Borrador',4:'Calculadora',5:'Escuadra'}
valores={1:2500,2:3800,3:1200,4:35000,5:3700}
totalcompra=0
n=int(input('Ingrese cantidad de articulos comprados :'))
for i in range(n):
    codigo=int(input('Ingrese código del Articulo :'))
    cantidad=int(input('Ingrese cantidad comprada :'))
    valorarticulo=cantidad*valores.get(codigo)
    totalcompra+=valorarticulo
    #totalcompra=totalcompra+valorarticulo
    print('\n*****Facturacion******\n')
    print('Codigo :',codigo)
    print('Nombre_Articulo :',articulos.get(codigo))
    print('Valor unitario :',valores.get(codigo))
    print('Valor articulo :','{:,.2f}'.format(valorarticulo))
    print('\n***********************\n')
print('\n*****Total Compra******\n')
print('Valor totalcompra :','{:,.2f}'.format(totalcompra))