clientefrecuente = input("¿Es un cliente frecuente?")
print(f"Responda con un si o no{clientefrecuente}")
monto = float(input("Ingrese un monton"))
precio = float

if clientefrecuente == "si":
   if monto>1000:
      descuento = (20*monto)/100
      precio = monto-descuento
      print("Felicidades tendran un descuento del 20%")
      print(f"El precio de su producto es {monto}")
      print(f"su descuento es de {descuento}")  
      print(f"su precio final es de {precio}") 
   elif monto>500:
      descuento = (5*monto)/100
      precio = monto-descuento
      print("Felicidades tendran un descuento del 5%")
      print(f"El precio de su producto es {monto}")
      print(f"su descuento es de {descuento}") 
      print(f"Su precio final es de {precio}")     
elif clientefrecuente == "no": 
   if monto>1000:
      descuento = (10*monto)/100
      precio = monto-descuento
      print("Felicidades tendran un descuento del 10%")
      print(f"El precio de su producto es {monto}")
      print(f"su descuento es de {descuento}")
      print(f"su precio final es de {precio}") 
   elif 500<monto:
      print("No posee descuento")
      print(f"El precio de su producto es {monto}")
      print(f"su precio final es de {monto}") 
else:
   print("Vuelva a intentarlo")
   