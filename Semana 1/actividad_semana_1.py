#Reto Plataforma
print ("Bienvenido a tu screen time")
nombre = str(input("¿Cuál es tu nombre?"))
insta = float(input("¿Cuantas horas pasas en Instagram?:"))
tiktok = float(input("¿Cuantas horas pasas en tiktok?:"))
X = float(input("¿Cuantas horas en apps de X (antes twitter)?:"))
canvas = float(input("¿Cuantas horas inviertes apps para estudiar?:"))
spot = float(input("¿Cuantas horas pasas en spotify?:"))
tiempo_total = insta + tiktok + X + canvas + spot 
porcentaje = (tiempo_total / 24 ) * 100 
porcentaje = round(porcentaje, 2)
print("Hola " + nombre +" pasaste " + str(tiempo_total) + " horas "
"y usas " + str(porcentaje) + "% de tu tiempo en medios digitales")

#Segundo Ejercicio

print ("¿Cuanto vas a dejar de propa paps?")

cuenta_total = float(input("Ingresa el total de la cuenta:"))
propa = int(input("ingresa el porcentaje de propina:")) 
comensales = int(input("¿Cuantos paps son?"))

propina = (cuenta_total * propa /100) / comensales
print ("$" + str(propina) + " por mirrey, acuérdate que viene tu chiqui")

##TERCER EJERCICIO
print ("Calculadora de calificación final")

pb = float(input("Calificación primer bimestre:"))
sb = float(input("Calificación segundo bimestre:"))
tb = float(input("Calificación tercer bimestre:"))

total = (pb + sb + tb)/3
print ("Tu promedio queda en: " + str(total) )

###CUARTO EJERCICIO
print ("Casa de Cambio Virtual")

mxn = (float(input("Ingresa la cantidad en Pesos Mexicanos:")))

dolares = mxn / 13.07
dolares = round(dolares, 2)

euros = mxn / 19.65
euros = round(euros, 2)

print ("$" + str (dolares) + " USD")

print ("$" + str (euros) + " EUR")
input("Presiona enter para salir")