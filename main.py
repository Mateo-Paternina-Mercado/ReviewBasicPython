def clasificar_nota():
    # Solicitar la nota numérica
    nota = float(input("Enter the grade (0-100): "))

    # Clasificar la nota
    if 90 <= nota <= 100:
        calificacion = "A"
    elif 80 <= nota <= 89:
        calificacion = "B"
    elif 70 <= nota <= 79:
        calificacion = "C"
    elif 60 <= nota <= 69:
        calificacion = "D"
    elif 0 <= nota < 60:
        calificacion = "F"
    else:
        calificacion = "Invalid grade"

    # Mostrar la calificación
    print(f"The grade is: {calificacion}.")

# Llamar a la función para clasificar la nota
clasificar_nota()
