def calcular_tiempo_viaje():
    # Solicitar la distancia y la velocidad promedio
    distancia = float(input("Enter the distance to travel (in km): "))
    velocidad = float(input("Enter the average speed of the car (in km/h): "))

    # Verificar si la velocidad es mayor a 120 km/h
    if velocidad > 120:
        print("Warning: Speed is over 120 km/h. Please drive safely!")

    # Calcular el tiempo en horas
    tiempo_horas = distancia / velocidad

    # Convertir el tiempo a horas y minutos
    horas = int(tiempo_horas)
    minutos = int((tiempo_horas - horas) * 60)

    # Mostrar el tiempo de viaje
    print(f"The travel time is: {horas} hours and {minutos} minutes.")

# Llamar a la función para calcular el tiempo de viaje
calcular_tiempo_viaje()
