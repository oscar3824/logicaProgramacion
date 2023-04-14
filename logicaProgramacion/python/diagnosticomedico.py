print("Diagnostico Medico")
nombre=input("Ingrese nombre del paciente :")
cedula=int(input("Ingrese cedula:"))
peso=float(input("Ingrese peso del paciente:"))
estatura=float(input("Ingrese estatura del paciente :"))
imc=(peso/(estatura**2))
if imc<=20:
   estado="Delgado"
elif imc>=20 and imc<=25:
    estado="Normal de peso"
elif imc>=25 and imc<=45:
    estado="Sobrepeso"
elif imc>45:
    estado="Obesidad"
print("Nombre del paciente:", nombre)
print("Cedula :", cedula)    
print("Peso del paciente:", peso,"Kg")
print("Estatura del paciente:", estatura,"m")
print("El estado del paciente es:", estado, "con un Idnice de masa corporal de:","{:,.2f}" .format(imc))
