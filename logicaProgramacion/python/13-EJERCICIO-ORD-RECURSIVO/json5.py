lista=['hola', 'como','estan']
print(lista)
persona={
    'nombre':'Luis',
    'edad':25,
    'estatura':1.75,
    'notas':[4,5,3,2]    
}
#print('nombre :'+persona['nombre'])
#print('edad :'+str(persona['edad']))
#print('estatura :'+str(persona['estatura']))
#print('notas :'+str(persona['notas']))

lista_persona=[
    #elemento 1
    {
    'nombre':'Luis',
    'edad':25,
    'estatura':1.75,
    'notas':[4,5,3,2]    
    },
    #elemento 2
    {
    'nombre':'Maria',
    'edad':35,
    'estatura':1.65,
    'notas':[6,7,2,1],
    'genero':'mujer'    
    },
    #elemento 3
    {
    'nombre':'Pedro',
    'edad':48,
    'estatura':1.80,
    'notas':[6,7,1]    
    }
]
print(lista_persona[1]['nombre'])
print(lista_persona[1]['edad'])
print(lista_persona[1]['genero'])

print(' **** Imprimir todos los elementos ****')

for elemento in lista_persona:
    print(elemento)
    
for elemento in lista_persona:
    print(elemento['edad'])
    
for elemento in lista_persona:
    print('Año de nacimiento ',2022-elemento['edad'])