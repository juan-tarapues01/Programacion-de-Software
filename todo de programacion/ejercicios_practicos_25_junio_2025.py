# print("------------------------------------ejercicio_1--------------------------------")

# calificacion1=int(input("ingrese su calificacion: "))
# calificacion2=int(input("ingrese su calificacion: "))
# calificacion3=int(input("ingrese su calificacion: "))
# lista=(calificacion1,calificacion2,calificacion3)
# calificacion=(calificacion1 + calificacion2 + calificacion3)
# resultado=(calificacion/3)
# print(resultado)
# print(f"su promedio es bueno si sus notas son mayor que 4.0  ")


# print("------------------------------------ejercicio_2--------------------------------")

# productos= {"manzana":1500,
#              "pera":1000,
#              "banano":800
#              }
# print(productos)
# porcentajes = float(input("porcentaje de aumento (%): "))
# productos["manzana"] += productos["manzana"]*(porcentajes / 100)
# productos["pera"] += productos["pera"] * (porcentajes /100)
# productos["banano"] += productos["banano"] * (porcentajes /100)
# print (productos)

#print("------------------------------------ejercicio_3--------------------------------")

#solicitar temperaturas al usuario y guardarlas en una tupla
# c1 = float(input("Temperatura 1 en °C: "))
# c2 = float(input("Temperatura 2 en °C: "))i8
# c3 = float(input("Temperatura 3 en °C: "))
# c4 = float(input("Temperatura 4 en °C: "))
# c5 = float(input("Temperatura 5 en °C: "))

# celsius = (c1,c2,c3,c4,c5)

# #convertir cada temperatura a Fahrenheit ----°F = (°C * 9/5) + 32. ----
# f1 = c1 * 9/5 + 32
# f2 = c2 * 9/5 + 32
# f3 = c3 * 9/5 + 32
# f4 = c4 * 9/5 + 32
# f5 = c5 * 9/5 + 32

# fahrenheit = (f1,f2,f3,f4,f5)

# #mostrar ambas tuplas
# print(f"Temperaturas en °C:",celsius)
# print(f"Temperaturas en °f:",fahrenheit)


#print("------------------------------------ejercicio_4--------------------------------")


# edades = [int(input("ingrese la edad_1: ")),int(input("ingrese la edad_2: ")) , int(input("ingrese la edad_3: ")),int(input("ingrese la edad_4: ")),int(input("ingrese la edad_5: "))]
# promedio = sum(edades) / en (edades)
# print(f"Mayor: {max(edades)} , Menor: {min(edades)} , promedio:{promedio } ")

# print("------------------------------------ejercicio_5--------------------------------")


# frutas = { 
#     "manzana":1000,
#      "granadilla ":2000,
#      "fresa": 1700
# }

# kilo_m = float(input("ingrese el numero de manzanas que quiere comprar "))

# kilo_g = float(input("ingrese el numero de granadilla que quiere comprar "))

# kilo_f = float(input("ingrese el numero de fresa que quiere comprar "))

# proceso_m = kilo_m * frutas ["manzana"]
# proceso_g = kilo_g * frutas ["granadilla "]
# proceso_f = kilo_f * frutas ["fresa"]

# total =[proceso_m + proceso_g + proceso_f ]
# print(f"precio a pagar{total}")



# print("------------------------------------ejercicio_6--------------------------------")

# elementos =[int(input("ingresa un numero: ")) ,int(input("ingresa un numero: ")) , int(input("ingresa un numero: ")),int(input("ingresa un numero: ")),int(input("ingresa un numero: "))]
# resultado = sum(elementos)

# print(f"el resultado de esta suma es:{resultado}")


# print("------------------------------------ejercicio_7--------------------------------")

# print("Inventario de productos")
# nombre1 = input("Nombre del producto 1: ")
# cantidad1 = int(input("Cantidad: "))
# precio1 = float(input("Precio por unidad: "))

# nombre2 = input("Nombre del producto 2: ")
# cantidad2 = int(input("Cantidad: "))
# precio2 = float(input("Precio por unidad: "))

# nombre3 = input("Nombre del producto 3: ")
# cantidad3 = int(input("Cantidad: "))
# precio3 = float(input("Precio por unidad: "))

# total = (cantidad1 * precio1) + (cantidad2 * precio2) + (cantidad3 * precio3)
# print("Total del inventario:", total)


# print("------------------------------------ejercicio_8--------------------------------")

print("Aplicar descuento")
precio1 = float(input("Ingrese el primer precio: "))
precio2 = float(input("Ingrese el segundo precio: "))
precio3 = float(input("Ingrese el tercer precio: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

nuevo1 = precio1 - (precio1 * descuento / 100)
nuevo2 = precio2 - (precio2 * descuento / 100)
nuevo3 = precio3 - (precio3 * descuento / 100)

print("Precios con descuento:")
print("Producto 1:", nuevo1)
print("Producto 2:", nuevo2)
print("Producto 3:", nuevo3)
 
 
# print("------------------------------------ejercicio_9--------------------------------")

print("Notas de estudiante")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))

mayor = max(nota1, nota2, nota3, nota4)
menor = min(nota1, nota2, nota3, nota4)

print("Nota más alta:", mayor)
print("Nota más baja:", menor)




# print("------------------------------------ejercicio_10--------------------------------")




























#ejercicio_7


tupla_externa=[1,2,(10,11,12),4]


primer_valor_interna=tupla_externa[2][0]


print(f"el primer valor de la dupla interna es :{primer_valor_interna}")


