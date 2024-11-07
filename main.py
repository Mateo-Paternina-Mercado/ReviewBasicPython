import random

def juego_adivina_numero():
    print("Welcome to the Guess the Number game!")
    numero_secreto = random.randint(1, 10)
    intentos = 0

    while True:
        try:
            # Pedimos al jugador que introduzca un número
            adivinanza = int(input("Guess the number (between 1 and 10): "))
            intentos += 1
            
            # Verificamos si el número es mayor, menor o igual al número secreto
            if adivinanza < numero_secreto:
                print("The number is greater. Try again!")
            elif adivinanza > numero_secreto:
                print("The number is less. Try again!")
            else:
                print(f"Congratulations! Have you guessed the number in {intentos} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Inicia el juego
juego_adivina_numero()