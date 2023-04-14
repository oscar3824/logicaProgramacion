persona={}
continuar=True
cont=0
while continuar:
    if cont==0:
        clave=input('Ingrese un dato numerico al primer campo de informacion personal :')   #cedula
        dato=int(input(clave+':'))    #cedula : 6954546
    elif cont>=1:
        clave=input('Ingrese otro campo a diligenciar, para su informacion personal :')   #nombre
        dato=(input(clave+':'))    #nombre : 
    persona[clave]=dato
    cont+=1
    print(persona)
    continuar=input('¿Quieres añadir mas informacion (Si/No) ?')=='si'
    
