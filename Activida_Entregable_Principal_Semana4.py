



matriz = [[" " , 1 , 2], [3 , 4 , 5], [5 , 6 , 7], [8 , 9 , 10]]
for fila in matriz:
    for elemento in fila:
        print(elemento,end=" ")
        print("")
    cant = 10
    print("   ", end="")
    for f in range (1, cant + 1):
        for c in range (1, cant+ 1):
            print(f * c, end="  ")
            print ( )




c1 = int(input("Ingresa una coordenada: "))
c2 = int(input("Ingresa una más: "))

coordenadas = c1*c2
print (coordenadas)