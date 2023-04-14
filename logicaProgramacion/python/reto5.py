def ordenamiento(lCodigo,lVproducto,lVtotal):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if  lCodigo[i]>lCodigo[j]:
                temp=lCodigo[i]
                lCodigo[i]=lCodigo[j]
                lCodigo[j]=temp   
                lVproducto[i]>lVproducto[j]
                temp=lVproducto[i]
                lVproducto[i]=lVproducto[j]
                lVproducto[j]=temp  
                lVtotal[i]>lVtotal[j]
                temp=lVtotal[i]
                lVtotal[i]=lVtotal[j]
                lVtotal[j]=temp                  
    return lCodigo,lVproducto,lVtotal
articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}
lCodigo=[]
lCantidad=[]
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
    lCodigo.append(int(input("")))
    lCantidad.append(float(input("")))
    lTipoiva.append(int(input("")))
    lVproducto.append(lCantidad[i]*precios.get(lCodigo[i]))
    
for i in range (n):    
    if lTipoiva[i]==1:
        iva=0
    elif lTipoiva[i]==2:
        iva=(lVproducto[i]*5)/100     
    else:
        iva=(lVproducto[i]*19)/100   
    lValoriva.append(iva)
    vTotal=(lVproducto[i]+iva)
    lVtotal.append(vTotal)   
    totalSaldo=totalSaldo+vTotal
    totalIva=totalIva+iva
lCodigo,lVproducto,Vtotal=ordenamiento(lCodigo,lVproducto,lVtotal)

for i in range (n):
    print(lCodigo[i])
    print(articulos.get(lCodigo[i]))
    print(lVproducto[i])
    print(lVtotal[i])
print(totalSaldo)
print(totalIva)