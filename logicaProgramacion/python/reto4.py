def ordenamiento(n,lCodigo,lNombre,lVproducto,lVtotal):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if lNombre[i]>lNombre[j]:
                temp=lNombre[i]
                lNombre[i]=lNombre[j]
                lNombre[j]=temp  
                lCodigo[i]>lCodigo[j]
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
    return lCodigo,lNombre,lVproducto,lVtotal
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
    lCodigo.append(int(input("")))
    lNombre.append(input(""))
    lCantidad.append(float(input("")))
    lVunitario.append(float(input("")))
    lTipoiva.append(int(input("")))
    lVproducto.append(lCantidad[i]*lVunitario[i])
    
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
lCodigo,lNombre,lVproducto,Vtotal=ordenamiento(n,lCodigo,lNombre,lVproducto,lVtotal)

for i in range (n):
    print(lCodigo[i])
    print(lNombre[i])
    print(lVproducto[i])
    print(lVtotal[i])
print(totalSaldo)
print(totalIva)