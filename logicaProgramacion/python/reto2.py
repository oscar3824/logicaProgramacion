n=int(input(""))
totalSaldo=0
totalIva=0
for i in range (n):
    codigo=int(input(""))
    nombre=(input(""))
    cantidad=float(input(""))
    vUnitario=float(input(""))
    tipoIva=int(input(""))
    vProducto =(cantidad*vUnitario)
    if tipoIva==1:
        iva=0
    elif tipoIva==2:
        iva=(vProducto*5)/100
        
    else:
        iva=(vProducto*19)/100   
    vTotal=(vProducto+iva)
    totalSaldo=totalSaldo+vTotal
    totalIva=totalIva+iva
    print(codigo)
    print(nombre)  
    print(vProducto)     
    print(vTotal)
print(totalSaldo)
print(totalIva)


