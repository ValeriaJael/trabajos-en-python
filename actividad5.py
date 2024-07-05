num= int(input("Ingrese un número"))

números=[1, 2, 3, 4, ]

if num in números:
    print("su número esta en la lista")
    print(f"{números}")
else:
    print("Su número no esta en la lista")
    print(f"{números}")