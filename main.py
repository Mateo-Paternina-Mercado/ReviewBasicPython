def clasificar_edad():
    # Solicitar la edad al usuario
    edad = int(input("Enter your age: "))

    # Clasificar según la edad
    if 0 <= edad <= 12:
        categoria = "Child"
    elif 13 <= edad <= 17:
        categoria = "Adolescent"
    elif 18 <= edad <= 64:
        categoria = "Adult"
    else:
        categoria = "Senior"

    # Mostrar la categoría
    print(f"You are classified as: {categoria}.")

# Llamar a la función para clasificar la edad
clasificar_edad()
