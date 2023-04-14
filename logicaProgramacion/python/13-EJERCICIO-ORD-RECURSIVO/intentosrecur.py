def jugar(nombre,intentos=1):
    respuesta=input("De cual color es una naranja: ")
    if respuesta!='naranja':
        if intentos<3:
            print('Perdiste este intento, te quedan ',3-intentos)
            intentos=intentos+1
            jugar(nombre,intentos)
        else:
            print('\n Usted ha perdido el Juego ',nombre)
    else:
        print('Adivinaste el color de la naranja',nombre,' has ganado ')
nombre=input("Ingrese su nombre: ")
print("Bienvenido al juego", nombre,"tienes 3 intentos")
jugar(nombre)