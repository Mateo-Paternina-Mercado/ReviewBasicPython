def mayor_de_tres():
    # Solicitar tres números al usuario
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Determinar el mayor de los tres números
    if num1 >= num2 and num1 >= num3:
        mayor = num1
    elif num2 >= num1 and num2 >= num3:
        mayor = num2
    else:
        mayor = num3

    # Mostrar el número mayor
    print(f"The largest number is: {mayor}.")

# Llamar a la función para determinar el mayor de los tres números
mayor_de_tres()
