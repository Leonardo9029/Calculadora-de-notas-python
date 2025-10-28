'''
Bienvenido a mi calculadora de notas y promedios de python



'''

'''

1° Funcionalidad: Quiero que calcule el promedio del semestre y me diga si pase o no pase.
2° Funcionalidad: Quiero que en base a algunas notas y los porcentajes me diga que nota nececito en el examen para pasar.

'''



#Menu de eleccion (2 opciones).


#Primero debe preguntar cuantas notas va a calcular
cant_notas=int(input("Cuantas notas desea ingresar: "))
#Segundo se ingresan las notas
nota=0
lista_notas=[]
for i in range(cant_notas):
    nota=float(input(f'Ingrese la nota {i+1}:'))
    lista_notas.append(nota)
#Tercero se ingresan los porcentajes
porcentaje=0
lista_porcentaje=[]
for i in range(cant_notas):
    porcentaje=(f'Ingresa el porsentaje de la nota {i+1}')
    porcentaje= porcentaje/100
    lista_porcentaje.append(porcentaje)
#Se calcula el promedio
    #Promedio con porcentajes:
prom=0
for i in range(cant_notas):
    prom+=lista_notas[i]*lista_porcentaje
    
print(f'El promedio es {prom}')
    #Promedio sin porcentajes:
prom

#Se entrega el resultado
