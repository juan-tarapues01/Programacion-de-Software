#commit
# numero = float(input("ingrese un numero: "))
# if numero > 0:
#     print("este numero positivo")
# elif numero < 0:
#     print("este numero es negativo")
# else:
#     print("este numero es cero")

# print("ejercicio_2")

# numero = int(input("ingrese un numero: "))
# numero2 = int(input("ingrese otro numero: "))
# if numero > numero2:
#     print(f"{numero} es mayor que {numero2}")
# elif numero2 > numero:
#     print(f"{numero2} es mayor que {numero}")
# else:
#     print("los numeros son iguales ")

# print("ejercicio_3")

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

# print ("----------------ejercicio_5--------------")




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

# precio = float(input("Ingrese el precio: "))
# cliente = input("¿Es cliente VIP o normal?: ").lower()

# if cliente == "vip":
#     precio = precio - (precio * 0.20)
#     print("Descuento del 20% aplicado.")
# else:
#     print("No se aplicó descuento.")

# print("Total a pagar:", precio)


# print("ejercicio_9")

# numero = int(input("Ingresa un número: "))
# if numero % 5 == 0 and numero % 3 == 0:
#     print("Es múltiplo de 5 y de 3.")
# elif numero % 5 == 0:
#     print("Es múltiplo de 5.")
# elif numero % 3 == 0:
#     print("Es múltiplo de 3.")
# else:
#     print("No es múltiplo ni de 5 ni de 3.")

# print("ejercicio_10")

# numero = float(input("ingrese un numero: "))
# numero_division = float(input("ingrese un numero divisor: "))
# numero_division2 = float(input("ingrese un numero divisor: "))

# if numero % numero_division == 0 and numero % numero_division2 ==0:
#     print(f"{numero} es divisible entre {numero_division} y {numero_division2}")
# elif numero % numero_division == 0:
#     print(f"{numero} es divisible solo entre {numero_division}")
# elif numero % numero_division2 == 0:
#     print(f"{numero} es divisible solo entre {numero_division2}")
# else: 
#     print(f"este numero no es divisible entre {numero_division} ni entre {numero_division2}")

# print("ejercicio_11")

# numero = [float(input("ingrese un numero: ")),float(input("ingrese un numero: ")),float(input("ingrese un numero: ")),float(input("ingrese un numero: ")),float(input("ingrese un numero: "))]

# if numero[2] > 10:
#     print(f"{numero[2]} es mayor a 10")
# elif numero[2] == 10:
#     print(f"{numero[2]} es igual a 10")
# else:
#     print(f"{numero[2]} menor a 10")


# print("ejercicio_12")

# print("debes de agregar el numero 7 en cualquier casilla") 

# numero = [int(input("ingresa un numero: ")),int(input("ingresa un numero: ")),int(input("ingresa un numero: ")),int(input("ingresa un numero: "))]

# print(numero)
# if 7 in numero:
#     print("el numero 7 si esta en la lista")
# else:
#     print("el numero 7 no esta en la lista")

# print("ejercicio_13")

# numero = float(input("ingresa un numero: ")),float(input("ingresa un numero: ")),float(input("ingresa un numero: ")),float(input("ingresa un numero: "))


# if numero[0] + numero[1]> 10:
#     print("al sumar los dos primeros numaros el resultado es una suma alta")
# else:
#     print("al sumar los dos primeros numaros el resultado es una suma baja")

# print("ejercicio_14")                 
#                                         #pide los nombres
# nombres = input("ingresa un nombre: "),input("ingresa un nombre: "),input("ingresa un nombre: "),input("ingresa un nombre: ")
                       
#                                                         #verificar si el ultimo nombre es "marta"
# if nombres[3] == "marta" or nombres[3] == "Marta":
#     print("Nombre correcto")
# else:
#     print("Nombre incorrecto")


# print("ejercicio 15")

# colores = [input("Ingrese un color: "),input("Ingrese un color: "),input("Ingrese un color: ")]


# if colores[0]=="azul" or colores[1]=="azul" or colores[2]== "azul":
#     nuevo =input ("ingrese el nuevo color para reemplazar 'azul': ")
#     colores[0] =nuevo
#     print(f"Lista actualizada con el color: {nuevo}") 
#     print (colores)
# else:
#     print(colores)

# print ("ejercicio 16")

# numeros = (float(input("ingrese un numero: ")),float(input("ingrese un numero: ")),float(input("ingrese un numero: ")),float(input("ingrese un numero: ")))
 
# if numeros[0]< numeros[3]:
#     print("Orden ascendente")
# else:
#     print("Orden decendente")

# print("ejercicio  17")

# edades =(int(input("ingrese edad: ")),int(input("ingrese edad: ")),int(input("ingrese edad: ")))

# if edades[1]> 30:
#     print("Segunda Edad mayor a 30 años")
# elif edades[1]==30:
#     print("Segunda Edad igual a 30 años")
# else:
#     print("Segunda Edad menor a 30 años")

# print("ejercicio 18")#sena

# tupla = (int(input("Ingrese un numero: ")),int(input("Ingrese un numero: ")),int(input("Ingrese un numero: ")))

# lista=list(tupla)


# if lista[1]==2:
#     lista[1]= 10
#     tupla=tuple(lista)
#     print(f"tupla modificada:\n{tupla}")
# else:
#     print(tupla)

# print("ejercicio 19")

# numero = (float(input("ingrese un numero: ")),float(input("ingrese un numero: ")))

# if numero[1]>5:
#     print("Coordenada alta")
# else:
#     print("Coordenada baja")

# print("ejercicio 20 ")

# tupla1 =(int(input("Ingrese un numero: ")),int(input("Ingrese un numero: ")))
# tupla2 =(int(input("Ingrese un numero: ")),int(input("Ingrese un numero: ")))

# if tupla1==tupla2:
#     print("Tuplas iguales")
# else:
#     print("Tuplas diferentes")


# print("ejercicio 21")

# datos ={
#     "nombre":input("Ingrese su nombre: "),
#     "edad":int(input("Ingrese su edad: "))
# }

# if datos["edad"]>=18:
#     print(f"{datos["nombre"]} Eres Adulto")
# else:
#     print(f"{datos["nombre"]} Eres Menor de edad")


# print("ejercicio 22")

# persona ={
#      "nombre":input("Ingrese su nombre: "),
#      "edad":int(input("Ingrese su edad: "))
#  }

# if persona["edad"]> 18:
#     persona["edad"]=21
#     print(persona)
# else:
#     print(persona)

# print("ejercicio 23")

# persona = {
#     "nombre":input("Ingrese su nombre: ")
# }

# if "ciudad" not in persona:
#     persona["ciudad"]= "Bogotá"
#     print(persona)

# print("ejercicio 24")

# producto = {
#     "producto":input("Ingrese un producto: "),
#     "precio":float(input("Ingrese el precio del producto: "))
# }

# if producto["precio"]>0:
#     print("precio:",producto["precio"])
# else:
#     print("No hay precio")

# print("ejercicio 25")

# productos = {
#     "pan":1200,
#     "leche":2000
# }

# if "pan" in productos:
#     print("Precio del pan: ",productos["pan"])
# else:
#     print("Producto no disponible")
