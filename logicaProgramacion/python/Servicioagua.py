n=int(input("Ingrese numero de usuarios a cancelar el servicio: "))
contv=0
conts=0
totalRecaudo=0
for i in range(n):
    print("Ingrese informacion del usuario:",i)
    codigo=input("Digite codigo: ")
    nombre=input("Digite nombre: ")
    estado=input("Digite estado: (v:vigente/s:suspendido): ")
    estrato=int(input("Digite estrato de 1 a 6: "))
    consumo=float(input("Ingrese consumo del mes en (cm3): "))
    if estado=="v":
        contv=contv+1
        if estrato==1:
            tarifabasica=10000
        elif estrato==2:
            tarifabasica=20000
        elif estrato==3:
            tarifabasica=30000
        elif estrato==4:
            tarifabasica=45000
        elif estrato==5:
            tarifabasica=60000
        else:
            tarifabasica=70000
        valorconsumo=consumo*200
        totalpagar=valorconsumo+tarifabasica
        totalRecaudo=totalRecaudo+totalpagar
        print('\n********************************')
        print("Factura del servicio")
        print("Usuario :",nombre)
        print("Valor tarifa :",tarifabasica)
        print("Valor a pagar :",totalpagar)
    else:
        conts=conts+1
        print('\n********************************')
        print("Su servicio se encuentra suspendido")
print('\n********************************')        
print("Total recaudo del servicio :",totalRecaudo)
print("Total usuarios vigente :",contv)          
print("Total usuarios suspendidos :",conts) 