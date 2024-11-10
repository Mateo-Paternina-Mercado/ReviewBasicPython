def convertir_calificacion():
    # Solicitar la calificación numérica
    calificacion = float(input("Enter the numeric grade (0-100): "))

    # Usar match para convertir la calificación a letra
    match calificacion:
        case calificacion if 90 <= calificacion <= 100:
            letra = "A"
        case calificacion if 80 <= calificacion <= 89:
            letra = "B"
        case calificacion if 70 <= calificacion <= 79:
            letra = "C"
        case calificacion if 60 <= calificacion <= 69:
            letra = "D"
        case _:
            letra = "F"

    # Mostrar la calificación en letra
    print(f"The letter grade is: {letra}.")

# Llamar a la función para convertir la calificación
convertir_calificacion()
