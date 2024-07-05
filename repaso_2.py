def es_par(numero):
    if numero%2 == 0:
        print("Su numero es par")
    else:
        print("Su numero es impar")

numero = int(input("Ingrese un numero"))
print(es_par(numero)) 

def saludar(nombre):
    print(f"Hola {nombre}")

print(saludar("Jael"))

listadefrutas=["kiwi", "sandia", "banana", "frutilla", "manzana"]

for lista in listadefrutas:
    print(f"Aquí lista de frutas {lista}")

edad = int(input("Ingrese su edad"))
print(edad)

if 18>edad:
    print("es menor de edad")
else:
    print("Es mayor de edad")

numero1=int(input("Ingrese un numero"))
print(numero1)
numero2=int(input("Ingrese un numero"))
print(numero2)

if numero1>numero2:
    print(f"{numero1} es mayor que numero {numero2} ")
elif numero1<numero2:
    print(f"{numero2} es mayor que numero {numero1} ")
elif numero1==numero2:
    print(f"{numero1} es igual a {numero2}")

num = int(input("Ingrese un numero"))
print(num)

def es_par(num):
    if num%2 ==0:
        print("Es un numero par")
    else:
        print("Es un numero impar")

par= es_par(num)
print(par)

listadefrutas=["kiwi", "sandia", "banana", "frutilla", "manzana"]
print(lista)
def buscar_fruta(fruta):
    fruta= input("Que fruta desea buscar?")
    if fruta in listadefrutas:
        print("Su fruta esta en la lista")
    else:
        print("Su fruta no esta en la lista")

buscar= buscar_fruta (listadefrutas)
print(buscar)

def cambiar_mayusculas(cadena):
    return cadena.lower()
cambiar= cambiar_mayusculas("JAEL")
print(cambiar)

texto= input("Ingrese un texto")

def cambiar_a_mayusculas(texto_de_usuario):
    return texto_de_usuario.lower(texto)
cambiar= cambiar_mayusculas(texto)
print(cambiar)

num = int(input("Ingrese un numero"))
cont= 1

while cont <= num:
    print(cont)
    cont+=1

listaenumeros= [2,4,4]

for num in listaenumeros:
    print(f"El doble de {num} es  {num*2}")
