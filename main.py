def tipo_triangulo():
    # Solicitar las longitudes de los tres lados
    lado1 = float(input("Enter the length of the first side: "))
    lado2 = float(input("Enter the length of the second side: "))
    lado3 = float(input("Enter the length of the third side: "))

    # Determinar el tipo de triángulo
    if lado1 == lado2 == lado3:
        tipo = "Equilateral"
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        tipo = "Isosceles"
    else:
        tipo = "Scalene"

    # Mostrar el tipo de triángulo
    print(f"The triangle is {tipo}.")

# Llamar a la función para determinar el tipo de triángulo
tipo_triangulo()
