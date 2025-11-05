'''
Bienvenido a mi calculadora de notas y promedios de python



'''


'''

1° Funcionalidad: Quiero que calcule el promedio del semestre y me diga si pase o no pase.
2° Funcionalidad: Quiero que en base a algunas notas y los porcentajes me diga que nota nececito en el examen para pasar.

'''
#Se inician alguna variables
cant_notas=0
suma_Porcentaje=0
prom=0
lista_porcentaje=[]
lista_notas=[]
#Funciones

#1
def ingresar_Notas_Porcentajes():
    while True:
        try:    
            print("-- Ingresar notas y/o porcentajes")
            op2=input('''Seleccione una opcion para agregar:
                    1.Notas y porcentajes
                    2.Solo notas
                    3.Solo porcentajes
                    4.Salir al menu principal'''
                    )
            #1.1
            if op2==1:
                cant_notas=int(input("Cuantas notas desea ingresar: "))
                for i in range(cant_notas):
                    nota=float(input(f'Ingrese la nota {i+1}:'))
                    lista_notas.append(nota)
                    porcentaje_input=float(f'Ingresa el porsentaje de la nota {i+1}')
                    suma_Porcentaje+= porcentaje_input
                    lista_porcentaje.append(porcentaje_input/100)

                if suma_Porcentaje !=100:
                    print(f'La suma de los porcentajes da: {suma_Porcentaje}')
                else:
                    print(f'Todo listo, se han ingresado {lista_notas.length()} notas y porcentajes.')

            #1.2
            elif op2==2:
                cant_notas=int(input("Cuantas notas desea ingresar: "))
                for i in range(cant_notas):
                    nota=float(input(f'Ingrese la nota {i+1}:'))
                    lista_notas.append(nota)

            #1.3
            elif op2==3:
                print("--Debe ingresar la cantidad de notas que desea agregar--")
                cant_notas=input("Cantidad de notas: ")
                print(f'  ---Ingresa los porcentajes sin el '%'---')
                for i in range(cant_notas):
                    porcentaje_input=float(f'Ingresa el porsentaje de la nota {i+1}')
                    suma_Porcentaje+= porcentaje_input
                    lista_porcentaje.append(porcentaje_input/100)

                if suma_Porcentaje !=100:
                    print(f'La suma de los porcentajes da: {suma_Porcentaje}%')
                else:
                    print(f'Se han ingresado {lista_porcentaje.length()} con exito ')
            elif op2==3:
                break
            else:
                print("Esa opcion no esta dentro de las opciones (1-4)")
                print(" ------------------------------------------------    ")
        except:
            print("Debe ingresar un numero entero (1-4)")
            print(" ------------------------------------------------    ")

#2
def editar_Notas_Porcentajes():
    pass

#3
def ver_Notas_Porcentajes():
    pass

#4
def eliminar_Nota_Porcentajes():
    pass


#5
def agregar_nota_Examen():
    pass

#6
def calcular_Promedio():
    pass
#7
def calcular_Examen():
    pass




print('----Bienvenido a la calculadora----')


while True:
    print(f'''
        --- Bienvenido al menu principal ---
        A continuacion tipea una de las siguientes opciones:
        ----------------------------------------------------
        1.Agregar notas y/o porcentajes.
        2.Modificar lista de notas y/o de porcentajes.
        3.Ver lista de notas y/o porcentajes.
        4.Eliminar notas y/o porcentajes.
        5.Agregar nota de examen.
        6.Calcular promedio.
        7.Calcular nota minima de examen.
        8.Salir del programa (se perderan los datos).
        
        ''')
    op= input(f'Ingresa una opcion numerica')
    #Manejo de exepciones
    try:


    #Menu de eleccion.
        match op:
            #1
            case 1:
                ingresar_Notas_Porcentajes()
            #2
            case 2:
                editar_Notas_Porcentajes()
            #3
            case 3:
                pass
            #4
            case 4:
                pass
        
            #5
            case 5:
                pass
        
            #6
            case 6:
                pass
        
            #7
            case 7:
                pass
        
            #8
            case 8:
                break
            
            case _:
                print("La opcion no estaba entre la lista (1-8)")

    except:
        print(f'Opcion no valida. Ingrese solo numeros (1-8)')









