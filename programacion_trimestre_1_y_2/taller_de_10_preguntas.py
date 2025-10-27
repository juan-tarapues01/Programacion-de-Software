# print ("----------------ejercicio_2--------------")
#4
# numero = float(input("Ingrese un número: "))

# if numero > 0:
#     print("El número es positivo.")
# elif numero < 0:
#     print("El número es negativo.")
# else:
#     print("El número es cero.")




# print ("----------------ejercicio_3--------------")



# numero = int(input("Ingrese un número: "))

# if numero % 2 == 0:
#     print("El número es par.")
# else:
#     print("El número es impar.")


# print ("----------------ejercicio_4--------------")


# numero = int(input("Ingrese un número: "))

# if numero >= 10 and numero <= 20:
#     print("El número está entre 10 y 20.")
# else:
#     print("El número NO está entre 10 y 20.")



# # print ("----------------ejercicio_5--------------")




# a = float(input("Primer número: "))
# b = float(input("Segundo número: "))
# c = float(input("Tercer número: "))

# if a >= b and a >= c:
#     print("El mayor es:", a)
# elif b >= a and b >= c:
#     print("El mayor es:", b)
# else:
#     print("El mayor es:", c)


# print ("----------------ejercicio_6--------------")

# total = float(input("Ingrese el total de la compra: "))

# if total > 100:
#     descuento = total * 0.10
#     total -= descuento
#     print("Se aplicó un 10% de descuento.")
# else:
#     print("No se aplicó descuento.")

# print("Total a pagar:", total)


# print ("----------------ejercicio_7--------------")


# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Puede votar.")
# else:
#     print("No puede votar.")


# print ("----------------ejercicio_8--------------")

precio = float(input("Ingrese el precio: "))
cliente = input("¿Es cliente VIP o normal?: ").lower()

if cliente == "vip":
    precio = precio - (precio * 0.20)
    print("Descuento del 20% aplicado.")
else:
    print("No se aplicó descuento.")

print("Total a pagar:", precio)


# print ("----------------ejercicio_9--------------")