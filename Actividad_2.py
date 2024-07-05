def contiene_pares (lista):
    for num in lista:
     if num % 2 == 0:
       print(f"True si tiene numero par {num}")
     else:
       print(f"false no tiene numero impar {num} ")

lista= [23, 45, 12, 19]

pares = contiene_pares (lista=[23, 45, 12, 19])
print(pares)