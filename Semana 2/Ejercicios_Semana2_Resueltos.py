#Programa que pida la edad e indique si una persona es mayor o menor de edad
edad = int(input("¿Qué edad tienes? "))
if (edad >=18):
    print("Eres mayor de edad, alócate")
else:
    print("Vete a jugar a las barbies, estás chiquito")

print("---------------------------------------------")
      
  #Programa que determina sin un número es par o impar
numero = int(input("Ingresa un número entero:"))

if (numero % 2 == 0):
    print("Es un número par")
else:
    print("Es un número impar")

print ("----------------------------------------------------")

calificacion = int(input("Que sacaste hermousaaa?"))
if (calificacion >=7):
    print("Heyyy pasaste (de milagro)")
else:
    print("Tocó repetir curso broski")


print("------------------------------------------------------")

#Programa de clasificación de rangos de edad con elif
age = int(input("What's your age again?"))
if (age >=0 and age <3):
    print("Eres un bebé")
elif (age >=3 and age <12):
    print("Eres un niño")
elif (age >=12 and age <17):
    print("Eres un adolescente")
else:
    print("Eres un adulto")


print("------------------------------------------------------")

#Programa que pide el tipo de cliente y determina si aplica descuento

tipo_cliente = str(input("¿Que tipo de client eres? (adulto_mayor, estudiante, profesor, otro): "))
if (tipo_cliente == "adulto_mayor"):
    print("Tienes descuento del 12%")
    print("Tu cuenta es de: ", 45 - (45 * 0.12))    
elif (tipo_cliente == "estudiante"):
    print("Tienes descuento del 10%")
    print("Tu cuenta es de: ", 45 - (45 * 0.1)) 
elif (tipo_cliente == "profesor"):
    print("Tienes descuento del 10%")
    print("Tu cuenta es de: ", 45 - (45 * 0.1))
elif (tipo_cliente == "otro"):
    print("No tienes descuento")
    print("Tu cuenta es de: ", 45)

print("------------------------------------------------------")
#Acceso denegado o permitido acorde a vigencia de credencial y edad del usuario
vigencia = int(input("¿Cuál es el año de vencimiento de tu credencial? "))
if(vigencia  <=  2025):
    print("Acceso denegado")
    exit 
else:
    print( " ¡Excelente!, ahora solo tenemos que verificar su edad.")

edad = int(input("¿Qué edad tiene?"))
if (edad >= 18):
    print ("Acceso Concedido")
else:
    print("Acceso Denegado")

print("----------------------------------------------------------------------------------------")



















print("-------------------------------------------------------------------------------------")


















print("-------------------------------------------------------------------------------------------")















