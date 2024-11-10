def clasificar_triangulo():
    # Solicitar los tres ángulos del triángulo
    angulo1 = float(input("Enter the first angle of the triangle (in degrees): "))
    angulo2 = float(input("Enter the second angle of the triangle (in degrees): "))
    angulo3 = float(input("Enter the third angle of the triangle (in degrees): "))

    # Verificar si la suma de los ángulos es igual a 180° (condición necesaria para un triángulo)
    if angulo1 + angulo2 + angulo3 != 180:
        print("The angles do not form a valid triangle.")
    else:
        # Clasificar el triángulo según sus ángulos
        if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
            print("The triangle is acute.")
        elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
            print("The triangle is right-angled.")
        else:
            print("The triangle is obtuse.")

# Llamar a la función para clasificar el triángulo
clasificar_triangulo()