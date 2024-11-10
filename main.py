def convertir_temperatura():
    # Solicitar la temperatura y la escala
    temperatura = float(input("Enter the temperature: "))
    escala = input("Enter the scale (C for Celsius, F for Fahrenheit): ").upper()

    # Usar match para convertir la temperatura
    match escala:
        case "C":
            # Convertir de Fahrenheit a Celsius
            temp_convertida = (temperatura - 32) * 5/9
            print(f"{temperatura} Fahrenheit is equal to {temp_convertida:.2f} Celsius.")
        case "F":
            # Convertir de Celsius a Fahrenheit
            temp_convertida = (temperatura * 9/5) + 32
            print(f"{temperatura} Celsius is equal to {temp_convertida:.2f} Fahrenheit.")
        case _:
            print("Invalid scale. Please enter 'C' or 'F'.")

# Llamar a la función para convertir la temperatura
convertir_temperatura()
