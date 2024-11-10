def calcular_calificacion_final():
    # Solicitar la calificación original del estudiante
    calificacion = float(input("Enter the student's grade: "))
    
    # Preguntar si hizo tareas adicionales
    tareas_adicionales = input("Did the student do additional tasks? (yes/no): ").lower()

    # Si hizo tareas adicionales, añadir un 5% extra
    if tareas_adicionales == "yes":
        calificacion += calificacion * 0.05
        # Asegurarse de que la calificación no exceda 100
        if calificacion > 100:
            calificacion = 100

    # Mostrar la calificación final
    print(f"The final grade is: {calificacion:.2f}")

# Llamar a la función para calcular la calificación final
calcular_calificacion_final()
