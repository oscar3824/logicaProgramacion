contp=0
conti=0
numero=int(input("Ingrese numero :"))
while (numero!=-1):
    residuo=numero%2
    if residuo==0:
        print("El numero :",numero, "es par")
        contp=contp+1
    else:
        print("El numero :",numero, "es inpar")
        conti=conti+1
    numero=int(input("Ingrese siguiente numero :"))
print("Cantidad de numeros leidos")
print("Cantidad de numeros pares :",contp)
print("Cantidad de numeros inpares :",conti)