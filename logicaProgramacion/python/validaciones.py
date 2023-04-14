while True:
    try:
        dato=int(input("Ingrese su edad :"))
        break
    except ValueError:
        print("Estas ingresando un dato erroneo")
        