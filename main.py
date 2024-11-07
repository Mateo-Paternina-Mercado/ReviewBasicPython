def imprimir_dia_semana(numero):
    match numero:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid number. Please enter a number from 1 to 7.")

# Solicitar al usuario que ingrese un número del 1 al 7
numero = int(input("Enter a number from 1 to 7: "))
imprimir_dia_semana(numero)