peso = float (input("Ingrese su peso en kilogramos"))
print(f"Su peso es de {peso}")
estatura = float (input("Ingrese su estatura en metros"))
print(f"Su estatura es de {estatura}")

imc = peso/(estatura*estatura)

if imc < 18.5:
    print(f"Su peso es bajo, su IMC es {imc}")#ftgbt
elif imc <= 25:
    print(f"Su peso es normal, su IMC es {imc}")
elif imc<=30:
    print(f"Tiene sobrepeso, su IMC es {imc}")
else:
    print(f"Tiene obesidad, su IMC es {imc}")


