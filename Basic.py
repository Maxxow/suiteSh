# Pedimos al usuario que ingrese su nombre
nombre = input("¿Cuál es tu nombre? ")

# Pedimos al usuario que ingrese su edad
edad = int(input("¿Cuántos años tienes? "))

# Calculamos el año en que nació el usuario
año_nacimiento = 2023 - edad

# Imprimimos un mensaje personalizado con los datos ingresados
print("Hola,", nombre, "! Naciste en el año", año_nacimiento)