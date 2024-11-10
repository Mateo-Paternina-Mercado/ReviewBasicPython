def adivinanza_letra():
    # Letra secreta
    letra_secreta = "A"
    
    # Solicitar la letra al usuario
    letra_usuario = input("Guess the secret letter: ").upper()
    
    # Usar match para comparar la letra ingresada
    match letra_usuario:
        
        case _:
            if letra_usuario == letra_secreta:
                print("Congratulation, you guessed the letter")
            else:           
                print("Sorry, that's not the correct letter. Try again.")
        

# Llamar a la función para iniciar el juego
adivinanza_letra()
