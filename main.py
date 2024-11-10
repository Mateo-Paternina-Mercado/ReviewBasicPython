def es_bisiesto():
    # Solicitar el año al usuario
    año = int(input("Enter a year: "))

    # Determinar si el año es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        resultado = "Leap year"
    else:
        resultado = "Not a leap year"

    # Mostrar el resultado
    print(f"The year is {resultado}.")

# Llamar a la función para determinar si el año es bisiesto
es_bisiesto()
