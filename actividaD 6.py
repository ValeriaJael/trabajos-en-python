numeros = [23, 45, 12, 67, 8, 90, 4, 1, 78, 33, 56, 7, 19]
# Doble de un numero 
maximo = max (numeros)
minimo = min (numeros)

print(numeros)

numeros.sort()
print(numeros)

for num in numeros:
    print(f"El doble de {num} es {num*2}")

for num in numeros:
    if num % 2 == 0:
     print(f"El numero {num} es par")
     numeros.sort()
    else:
     print(f"El numero {num} es impar")

#dentro del while

#Orden lista
print("Aca se odena", numeros)

maximo = max(numeros)
minimo = min(numeros)

print(maximo)
print(minimo)
