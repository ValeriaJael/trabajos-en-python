numeros = [23, 45, 12, 67, 8, 90, 4, 1, 78, 33, 56, 7, 19]
for num in numeros:
    print(f"el doble de {num} es {num*2}")

for num in numeros:
    if num % 2 ==0:
        print(f"{num} es par") 
    else:
        print(f"{num} es impar")

maximo = max (numeros)
minimo = min(numeros)

print(f"Este es el numero mayor de la lista {maximo}")
print(f"Este es el numero menor de la lista {minimo}")

numeros.sort()
print(numeros)

eliminar =int(input("Que numero desea eliminar?"))
numeros.remove(eliminar)

agregar= int(input("Que numero desea agregar?"))
numeros.append(agregar)

print(numeros)


ciente = input("es cliente frecuente")
print(ciente)

if ciente == "si":
    print("hola")
elif ciente == "no":
    print("adios")




