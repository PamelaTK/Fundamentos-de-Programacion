precio_menor3= 0
precio_menorE= 30
precio_mayorE= 45

descuento_3ra_edad= 0.12
descuento_prof= 0.10
descuento_stud= 0.10

print("Bienvenido al Museo de Antropología e Historia")
visitors= int(input("¿Cuantas personitas se nos unen hoy?: "))

tot_gen= 0

for i in range (visitors):

    print(f"\n Info Visitante {i+1} ")
    age = int(input("ingrese la edad del visitante: "))

    if age < 0:
        print("Ingrese una edad válida.")
        continue
    elif age < 3:
        price= precio_menor3

        print("El visitante es menor de 3 años, costo entrada: 0.00")

        print(f"Su total es ${tot_gen:.2f}")
        print("N/A descuento")
        print(f"Total a pagar: ${tot_gen:.2f}")

        tot_gen += price

        continue
    elif age >= 3 and age <= 17:
        price= precio_menorE
    else:
        price= precio_mayorE

    ####################################################################    
    tipo = input(
        "Tipo de visitante: \n1. Profesor \n2. Estudiante \n3. Adulto Mayor \n4. Ninguno \nIngrese el número correspondiente: ")
    
    if tipo == "1": 
        porcentaje_descuento = descuento_prof
        tipo_descuento = "Profesor 10%"

    elif tipo == "2":
        porcentaje_descuento = descuento_stud
        tipo_descuento = "Estudiante 10%"

    elif tipo == "3":
        porcentaje_descuento = descuento_3ra_edad
        tipo_descuento = "Adulto Mayor 12%"   

    elif tipo == "4":
        porcentaje_descuento = 0
        tipo_descuento = "Ninguno"

    descuento_aplicado = price * porcentaje_descuento

    gran_tot = price - descuento_aplicado

    print(f"Su total es ${price:.2f}")
    print(f"Descuento aplicado: ${descuento_aplicado:.2f}")
    print(f"Total a pagar: ${gran_tot:.2f}")

    tot_gen += gran_tot
    print(f"\nTotal a pagar por el grupo: ${tot_gen:.2f}")