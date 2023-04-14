nombre=input("Ingrese su nombre: ")
salarioneto=float(input("Ingrese el salario: "))
if salarioneto<=1000000:
  subsidio=120000
  salariobasico=salarioneto+subsidio
else:
    subsidio=0
    salariobasico=salarioneto+subsidio
print("Nombre del trabajador:", nombre)
print("Salario del trabajador:", salarioneto)
print("Subsidio:", subsidio)
print("Total devengado:", salariobasico)
