numeros = []
while True:
    try:
        numero = input("Ingrese un número (o cualquier otra tecla para finalizar): ")
        numero = float(numero)  # Convertimos el valor a número flotante (para permitir decimales)
        numeros.append(numero)
    except ValueError:
        break

suma = sum(numeros)
print("La suma de los números ingresados es:", suma)