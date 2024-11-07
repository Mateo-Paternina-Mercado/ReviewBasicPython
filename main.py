def determinar_signo(numero):
    if numero > 0:
        print("The number is positive.")
    elif numero < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# Solicitar al usuario que ingrese un número
numero = float(input("Enter a number: "))
determinar_signo(numero)