height = int(input("Altura:"))

for fila in range (1, height + 1):

    for espacios in range(height - fila):
        print(" ", end="")

    for asterisco in range(2 * fila - 1):
        print("*", end="")

    print() 