precio_menor3= 0
precio_menorE= 30
precio_mayorE= 45

descuento_3ra_edad= 0.12
descuento_prof= 0.10
descuento_stud= 0.10
print("Bienvenido al Museo de Antropología e Historia")

visitantes_tot= int(input("¿Cuántas personas nos acompañan el día de hoy?: "))
total_a_pagar=0.0
visitantes_registrados=0

while visitantes_registrados < visitantes_tot:
    print("Datos del Visitante")
    
    edad= int(input("Ingrese la edad del visitante (o ingrese 841 para SALIR): "))
    
    if edad==841:
        print("Gracias por usar el sistema de registro, vuelva pronto.")
        break

    elif edad < 3:
        precio_base= precio_menor3
        print("Niño menor de 3 años - Costo: 0.00")

    elif edad >= 3 and edad <= 17:
        print("Menor de edad - Costo: 30.00")
        precio_base= precio_menorE
        
    else:
        print("Adulto - Costo: 45.00")
        precio_base= precio_mayorE

    if precio_base==0:
        total_a_pagar= total_a_pagar + 0
        visitantes_registrados= visitantes_registrados + 1
        continue

    print("Responda con 'si' o 'no'")
    es_profesor= str(input("¿Es profesor?: "))
    es_estudiante= str(input("¿Es estudiante?: "))
    es_adulto_mayor= str(input("¿Es adulto mayor?: "))

    descuento_aplicado=0.0
    tipo_descuento="Ninguno"

    if edad >= 60:
        descuento_aplicado= precio_base * descuento_3ra_edad
        tipo_descuento="Adulto Mayor 12%"
    elif es_profesor=="si" and es_estudiante=="no":
        descuento_aplicado= precio_base * descuento_prof
        tipo_descuento="Profesor 10%"
    elif es_estudiante=="si" and es_profesor=="no":
        descuento_aplicado= precio_base * descuento_stud
        tipo_descuento="Estudiante 10%"
    elif es_profesor=="si" and es_estudiante=="si":
        # Si tiene ambos, se queda con el de profesor por orden de la tabla
        descuento_aplicado= precio_base * descuento_prof
        tipo_descuento="Profesor (Descuento Único)"
    else:
        descuento_aplicado=0.0