# Programa para determinar si una nota numérica es "Aprobado" o "Reprobado"

# Solicitar al usuario que ingrese una nota
nota = float(input("Enter a numerical note : "))

# Verificar si la nota es aprobatoria o reprobatoria
if nota >= 60:
    print("Approved")
else:
    print("Failed")
