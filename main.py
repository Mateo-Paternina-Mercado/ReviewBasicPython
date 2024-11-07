# Programa para verificar si un número es par o impar

# Solicitar al usuario que ingrese un número
numero = int(input("Enter a number: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
