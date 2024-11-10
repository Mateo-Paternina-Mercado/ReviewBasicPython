def calcular_imc():
    # Solicitar el peso y la altura
    peso = float(input("Enter your weight in kg: "))
    altura = float(input("Enter your height in meters: "))

    # Calcular el IMC
    imc = peso / (altura ** 2)

    # Clasificar el IMC
    if imc < 18.5:
        estado = "Underweight"
    elif 18.5 <= imc <= 24.9:
        estado = "Normal weight"
    elif 25 <= imc <= 29.9:
        estado = "Overweight"
    else:
        estado = "Obesity"

    # Mostrar el IMC y el estado
    print(f"Your BMI is {imc:.2f}. You are classified as: {estado}.")

# Llamar a la función para calcular el IMC
calcular_imc()
