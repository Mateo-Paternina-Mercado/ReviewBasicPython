def calculadora():
    # Solicitar los números y la operación
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operacion = input("Enter the operation (+, -, *, /): ")

    # Usar match para elegir la operación
    match operacion:
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "*":
            resultado = num1 * num2
        case "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: Cannot divide by zero."
        case _:
            resultado = "Invalid operation."

    # Mostrar el resultado
    print(f"Result: {resultado}")

# Llamar a la función de la calculadora
calculadora()