#Actividad Evaluable Semana 2
print("Bienvenido al Museo de Antropología e Historia")

num_visitantes = int(input("¿Cuántos visitantes tendremos hoy? -Ingrese un valor en números enteros- :"))

total_final_grupo = 0

precio_base_menor3 = 0
precio_base_menores_edad = 30
precio_base_adultos = 45

for visitante in range(num_visitantes):
    edad = int(input(f"Ingrese la edad del visitante {visitante + 1}: "))
    if edad < 3:
        print("El visitante es menor de 3 años, por lo que no paga entrada.")
    elif 3 <= edad < 18:
        print("El visitante es menor de edad, por lo que paga la entrada reducida.")
    else:
        print("El visitante es adulto, por lo que paga la entrada completa.")