precio_infantil = 0
precio_menor_edad = 30
precio_mayor_edad = 45

descuento_3ra_edad = 0.12
descuento_profesor = 0.10
descuento_estudiante = 0.10

print("--- SISTEMA DE COBRO: MUSEO ---")

total_visitantes = int(input("¿Cuántos visitantes son en total?: "))

total_general_pagar = 0.0
visitantes_procesados = 0

while visitantes_procesados < total_visitantes:
    print("\n--- Datos del Visitante ---")
    
    edad = int(input("Ingrese la edad del visitante (o ponga 999 para SALIR): "))
    
    if edad == 999:
        print("Se detiene el registro por el usuario.")
        break

    if edad < 3:
        precio_base = precio_infantil
    elif edad >= 3 and edad <= 17:
        precio_base = precio_menor_edad
    else:
        precio_base = precio_mayor_edad

    if precio_base == 0:
        print("Resultado: Niño menor de 3 años - Entrada Gratis ($0.00)")
        total_general_pagar = total_general_pagar + 0
        visitantes_procesados = visitantes_procesados + 1
        continue

    print("Responda con 'si' o 'no'")
    es_profesor = input("¿Es profesor?: ")
    es_estudiante = input("¿Es estudiante?: ")

    descuento_aplicado = 0.0
    tipo_descuento = "Ninguno"

    if edad >= 60:
        descuento_aplicado = precio_base * descuento_3ra_edad
        tipo_descuento = "Adulto Mayor 12%"
    elif es_profesor == "si" and es_estudiante == "no":
        descuento_aplicado = precio_base * descuento_profesor
        tipo_descuento = "Profesor 10%"
    elif es_estudiante == "si" and es_profesor == "no":
        descuento_aplicado = precio_base * descuento_estudiante
        tipo_descuento = "Estudiante 10%"
    elif es_profesor == "si" and es_estudiante == "si":
        # Si tiene ambos, se queda con el de profesor por orden de la tabla
        descuento_aplicado = precio_base * descuento_profesor
        tipo_descuento = "Profesor (Descuento Único)"
    else:
        descuento_aplicado = 0.0
        tipo_descuento = "Ninguno"

    precio_final_individual = precio_base - descuento_aplicado
    total_general_pagar = total_general_pagar + precio_final_individual

    
    print(f"Subtotal: ${precio_base:.2f}")
    print(f"Descuento: -${descuento_aplicado:.2f} ({tipo_descuento})")
    print(f"Total de este boleto: ${precio_final_individual:.2f}")
    
    visitantes_procesados = visitantes_procesados + 1

print("\n==========================================")
print(f"Total de visitantes cobrados: {visitantes_procesados}")
print(f"TOTAL GENERAL A PAGAR: ${total_general_pagar:.2f}")
print("==========================================")
