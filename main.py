def calcular_creditos():
    # Solicitar el número de materias cursadas
    num_materias = int(input("Enter the number of subjects taken: "))
    
    # Inicializar el total de créditos
    total_creditos = 0
    
    # Solicitar el puntaje para cada materia y evaluar si está aprobado
    for i in range(num_materias):
        puntaje = float(input(f"Enter the score for subject {i+1}: "))
        
        # Verificar si el puntaje es aprobado
        if puntaje >= 60:
            total_creditos += 3  # Cada materia aprobada otorga 3 créditos
    
    # Mostrar el total de créditos
    print(f"The total number of credits earned is: {total_creditos}")

# Llamar a la función para calcular los créditos
calcular_creditos()
