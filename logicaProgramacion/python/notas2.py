nombre=input("Ingrese su nombre :")
nota=int(input("Ingrese su nota :"))
if ((nota>=0)and(nota<=100)):
    if nota<=59:
        nc="D"
    elif nota<=79:
         nc="C"
    elif nota<=89:
         nc="B"
    else:
        nc="A"
    print("Nombre del estuduiante :",nombre)
    print("Nota cuantitativa :",nota)
    print("Nota cualitativa :",nc)
else:
    print("Valor fuera de rango")
