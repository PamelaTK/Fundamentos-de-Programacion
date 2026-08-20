print ("Bienvenido a la calculadora de tu tiempo!")
nombre = str(input("Ingresa tu nombre:"))
tig = float(input("¿Cuantas horas pasas en Instagram?:"))
twh = float(input("¿Cuantas horas pasas en Whatsapp?:"))
tst = float(input("¿Cuantas horas en apps de streaming?:"))
tes = float(input("¿Cuantas horas inviertes en apps de estudio?:"))
tmus = float(input("¿Cuantas horas pasas en apps de Musica?:"))
tiempo_total = tig + twh + tst + tes + tmus 

porcentaje = (tiempo_total / 24 ) * 100 
print("Hola " + nombre +" acumulaste " + str(tiempo_total) + " horas y pasas el " + str(porcentaje) + "% de tu tiempo en medios digitales")