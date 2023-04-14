while True:
    try:
        categoria=int(input("Ingrese categoria ente(1,2,3)"))
        if categoria<1 or categoria>3:
            print("Te has salido del rango de la categoria")
            continue
        break
    except ValueError:
        print("ojo utilice numeros enteros")
print("Ingresaste la categoria:",categoria)
