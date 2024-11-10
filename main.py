def calcular_salario_neto():
    # Solicitar el salario bruto y el país de residencia
    salario_bruto = float(input("Enter your gross salary: "))
    pais = input("Enter your country of residence (Country A, Country B, Country C): ").title()

    # Calcular el porcentaje de impuestos según el país
    match pais:
        case "Country A":
            impuestos = 0.20
        case "Country B":
            impuestos = 0.15
        case "Country C":
            impuestos = 0.10
        case _:
            impuestos = 0.25

    # Calcular el salario neto
    salario_neto = salario_bruto * (1 - impuestos)

    # Mostrar el salario neto
    print(f"Your net salary is: {salario_neto:.2f}.")

# Llamar a la función para calcular el salario neto
calcular_salario_neto()
