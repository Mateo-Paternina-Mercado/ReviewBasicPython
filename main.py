def calcular_costo_estacionamiento():
    # Solicitar el número de horas de estacionamiento
    horas = int(input("Enter the number of hours of parking: "))

    # Inicializar el costo
    costo = 0

    # Calcular el costo basado en las tarifas progresivas
    if horas <= 1:
        costo = 5
    elif 2 <= horas <= 4:
        costo = 5 + (horas - 1) * 4
    else:
        costo = 5 + 3 * 3 + (horas - 4) * 3

    # Mostrar el costo total
    print(f"The total parking cost is: ${costo}")

# Llamar a la función para calcular el costo de estacionamiento
calcular_costo_estacionamiento()

