#programa diseñado para generar una tabla de pitágoras de 10x10 utilizando una matriz. La tabla se muestra de forma ordenada (sin usar corchetes ni comas)
#El código procede a pregintar dos coordenadas (una del renglón superior horizontal, y una de la columna izquierda vertical). Al hacer esto nos imprimirá el valor que se encuentra en dichas coordenadas.

matriz = []
for fila in range(1,11):
    renglon = []
    for columna in range(1, 11):
        renglon.append(fila*columna)
    matriz.append(renglon)

def imprimir_tabla(tabla):
    print("\t", end="")
    for columna in range (1,11):
        print(columna,end="\t")
    print()

    for i in range (len(tabla)):
        print(i + 1, end="\t")
        for elemento in tabla [i]:
            print (elemento, end="\t")
        print()

def consultar_producto(tabla, renglon, columna):
    return tabla [renglon - 1][columna - 1]

imprimir_tabla(matriz)

renglon = int(input("Ingresa un coordenada: "))
columna = int(input("Ingresa una más: "))
resultado = consultar_producto( matriz, renglon, columna)


print(f"El producto de {renglon} x {columna} es {resultado}")