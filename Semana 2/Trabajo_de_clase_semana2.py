edad = 16 
if edad >= 18:
    print("Eres mayor de edad")
else:
    print ("Eres menor de edad")

print("----------------------------------------------------")

calif = 42
conducta = 8
if calif >= 90:
    print("A")
    if conducta >= 9:
        print("Tu conducta es excelente")
elif calif >= 80:
    print("B")
    if conducta >= 8:
        print("Tu conducta es buena")
elif calif >= 70:
    print("C")
    if conducta >= 7:
        print("Tu conducta es mala")
elif calif >= 60:
    print("D")
    if conducta >= 6:
        print("Tu conducta es pésima")
else:
    print("E, sáquese perro")

print("---------------------------------------------------")
Pl1 = True
Pl2 = False

print(Pl1 and Pl2)
print(Pl1 or Pl2) 

Edad = 65
tipo = "Adulto_Mayor"

es_mayor = edad >= 18
print ("es_mayor")
aplica_descuento = (edad >= 60) and (tipo >= "Adulto_Mayor")
print ("aplica_descuento")

print("------------------------------")

edad=int(input("Ingresa tu edad: "))

if not ( edad <= 0):
    print("Aguarda, no hay edades menores a 0")
else:
    print("Ahora sí, vamos a trabajar con edades reales")
