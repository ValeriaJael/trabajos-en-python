def es_par (num):
    if num % 2 == 0:
      print(f"El numero es par {num}")
    else:
       print(f"EL numero es impar {num} ")

num= int(input("Ingrese un numero"))

par = es_par (num)
print(par)


def saludar(nombre):
    print(f"hola{nombre}")

saludar("Jael")

nombre = input("su nombre")

listadefrutras = ["Manzana", "pera", "kiwi", "banana", "sandia"]

for lista in listadefrutras:
    print(f"Aca la lista {lista}")

edad = int(input("Ingrese su edad"))
print(edad)

if edad >18:
   print("es mayor de edad")
elif edad < 18:
   print("es menor de edad")
else:
   print("Error")

numero1 = int(input("Ingrese el primer numero "))
print(numero1)
numero2 = int(input("Ingrese el segundo numero"))
print(numero2)

if numero1>numero2:
   print(f"{numero1} es mayor que {numero2}")
elif numero1<numero2:
   print(f"{numero2} es mayor que {numero1}")
elif numero1==numero2:
   print(f"{numero2} es igual a {numero1}")


num= int(input("Ingrese un numero"))

def nombre_usuario (num):
    if num % 2 == 0:
      print(f"El numero es par {num}")
    else:
       print(f"EL numero es impar {num} ")

pr= nombre_usuario(num)
print(pr)

listadefrutras = ["manzana", "pera", "kiwi", "banana", "sandia"]
def buscar_fruta(fruta):
   fruta_buscar = input("Cual es el nombre que desea buscar? ")
   if fruta_buscar in listadefrutras:
         print ("La fruta que busca, si está en la lista")
   else:
       print ("La fruta que busca NO está en la lista")

fru= buscar_fruta( listadefrutras)
print(fru)

def cambia_a_minusculas(cadena):
   return cadena.lower()

print(cambia_a_minusculas("JAEL"))


def cambia_a_minusculas(cadena):
   return cadena.lower()

print(cambia_a_minusculas("PALABRA"))

numerolimite= int(input("Ingrese un numero"))
print(numerolimite)

cont = 1
while cont <= numerolimite:
   print(cont)
   cont +=1

 