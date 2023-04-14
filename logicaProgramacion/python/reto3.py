lCodigo=[]
lNombre=[]
lCantidad=[]
lVunitario=[]
lTipoiva=[]
lVproducto=[]
lValoriva=[]
lVtotal=[]
lTotalsaldo=[]
lTotaliva=[]
totalSaldo=0
totalIva=0
n=int(input(""))
for i in range (n):
    codigo=int(input(""))
    lCodigo.append(codigo)
    nombre=(input(""))
    lNombre.append(nombre)
    cantidad=float(input(""))
    lCantidad.append(cantidad)
    vUnitario=float(input(""))
    lVunitario.append(vUnitario)
    tipoIva=int(input(""))
    lTipoiva.append(tipoIva)
    vProducto=(cantidad*vUnitario)
    lVproducto.append(vProducto)
    if tipoIva==1:
        iva=0
    elif tipoIva==2:
        iva=(vProducto*5)/100     
    else:
        iva=(vProducto*19)/100   
    lValoriva.append(iva)
    vTotal=(vProducto+iva)
    lVtotal.append(vTotal)   
    totalSaldo=totalSaldo+vTotal
    totalIva=totalIva+iva
print(len(lCodigo))
print(len(lNombre))
print(len(lCantidad))   
print(len(lVunitario))
print(len(lTipoiva))
for i in range (n):
    print(lCodigo[i])
    print(lNombre[i])
    print(lVproducto[i])
    print(lVtotal[i])
print(totalSaldo)
print(totalIva)

