#primer commit
print("--------ejercicio_1------------")

edad = int(input("Ingresa tu edad: "))
if edad < 18:
    print("Eres menor de edad.")#####
elif edad >= 65:
    print("Eres adulto mayor.")
else:
    print("Eres mayor de edad.")

# print("--------ejercicio_2------------")

# estatura = float(input("Ingresa tu estatura en metros: "))
# if estatura < 1.5:
#     print("Estatura baja.")
# elif estatura <= 1.8:
#     print("Estatura media.")
# else:
#     print("Estatura alta.")



# print("--------ejercicio_3------------")

# numero = int(input("Ingresa un número: "))
# if numero % 2 == 0 and numero % 3 == 0:
#     print("Es múltiplo de 2 y de 3.")
# elif numero % 2 == 0:
#     print("Es múltiplo de 2.")
# elif numero % 3 == 0:
#     print("Es múltiplo de 3.")
# else:
#     print("No es múltiplo ni de 2 ni de 3.")


# print("--------ejercicio_4------------")

# decimal = input("Ingresa un número decimal: ")
# partes = decimal.split(".")
# if len(partes) == 2:
#     decimales = len(partes[1])
#     if decimales == 1:
#         print("Tiene 1 decimal.")
#     elif decimales == 2:
#         print("Tiene 2 decimales.")
#     else:
#         print("Tiene más de 2 decimales.")
# else:
#     print("No es un número decimal válido.")


# print("--------ejercicio_5------------")

# pais = input("Ingresa un país: ")
# paises = ("Colombia", "Perú", "Argentina", "México")
# if pais in paises:
#     print("El país está en la lista.")
# else:
#     print("El país no está en la lista.")


# print("--------ejercicio_6------------")

# sangre = input("Ingresa tu tipo de sangre (A, B, AB, O): ")
# compatibilidad = {
#     "A": "A y AB",
#     "B": "B y AB",
#     "AB": "AB",
#     "O": "Todos"
# }
# if sangre in compatibilidad:
#     print("Compatible con:", compatibilidad[sangre])
# else:
#     print("Tipo de sangre no válido.")


# print("--------ejercicio_7------------")

# temp = float(input("Ingresa la temperatura en °C: "))
# if temp < 10:
#     print("Hace frío.")
# elif temp <= 25:
#     print("Templado.")
# else:
#     print("Hace calor.")


# print("--------ejercicio_8------------")

# print("1. Sumar\n2. Restar\n3. Multiplicar")
# opcion = int(input("Elige una opción: "))
# a = int(input("Ingresa el primer número: "))
# b = int(input("Ingresa el segundo número: "))

# if opcion == 1:
#     print("Resultado:", a + b)
# elif opcion == 2:
#     print("Resultado:", a - b)
# elif opcion == 3:
#     print("Resultado:", a * b)
# else:
#     print("Opción no válida.")


# print("--------ejercicio_9------------")

# meses = {
#     1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
#     5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
#     9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
# }
# n = int(input("Ingresa un número entre 1 y 12: "))
# if n in meses:
#     print("Mes:", meses[n])
# else:
#     print("Número fuera de rango.")


# print("--------ejercicio_10------------")

# numero = input("Ingresa un número de 4 dígitos: ")
# if numero.startswith("1"):
#     print("Empieza con 1.")
# elif numero.startswith("2"):
#     print("Empieza con 2.")
# else:
#     print("Empieza con otro número.")


# print("--------ejercicio_11------------")

# palabra = input("Ingresa una palabra: ")
# primera = palabra[0].lower()
# if primera in "aeiou":
#     print("Empieza con vocal.")
# elif primera.isdigit():
#     print("Empieza con número.")
# else:
#     print("Empieza con consonante.")


# print("--------ejercicio_12------------")

# frutas = {"manzana": 3000, "pera": 2500, "piña": 4000}
# fruta = input("Ingresa una fruta: ")
# if fruta in frutas:
#     print("Precio:", frutas[fruta])
# else:
#     print("No está disponible.")


# print("--------ejercicio_13------------")

# nota = float(input("Ingresa tu calificación (0 a 5): "))
# if nota < 3:
#     print("Reprobado.")
# elif nota <= 4:
#     print("Aprobado.")
# else:
#     print("Excelente.")


# print("--------ejercicio_14------------")

# n = int(input("Ingresa un número: "))
# if n % 4 == 0 and n % 6 == 0:
#     print("Es divisible entre 4 y 6.")
# elif n % 4 == 0:
#     print("Es divisible entre 4.")
# elif n % 6 == 0:
#     print("Es divisible entre 6.")
# else:
#     print("No es divisible entre 4 ni 6.")

# print("--------ejercicio_15------------")

# usuarios = {"juan": "1234", "ana": "abcd"}
# usuario = input("Usuario: ")
# clave = input("Clave: ")
# if usuario in usuarios and usuarios[usuario] == clave:
#     print("Acceso concedido.")
# else:
#     print("Acceso denegado.")


# print("--------ejercicio_16------------")

# edad = int(input("Ingresa tu edad: "))
# if edad <= 12:
#     print("Niño.")
# elif edad <= 17:
#     print("Adolescente.")
# elif edad <= 64:
#     print("Adulto.")
# else:
#     print("Mayor.")


# print("--------ejercicio_17------------")

# ciudad = input("Ingresa el nombre de una ciudad: ")
# capitales = ("Bogotá", "Lima", "Buenos Aires", "Ciudad de México")
# if ciudad in capitales:
#     print("Es una capital.")
# else:
#     print("Ciudad secundaria.")


# print("--------ejercicio_18------------")

# valor = float(input("Valor de la compra: "))
# if valor > 200000:
#     descuento = valor * 0.15
# elif valor >= 100000:
#     descuento = valor * 0.10
# else:
#     descuento = 0
# print("Descuento aplicado:", descuento)


# print("--------ejercicio_19------------")

# nombre = input("Nombre: ")
# horas = int(input("Horas trabajadas: "))
# salario = horas * 10000
# if horas > 40:
#     bono = salario * 0.20
#     salario += bono
# print("Salario total:", salario)


# print("--------ejercicio_20------------")

# puntaje = int(input("Ingresa tu puntaje (0-100): "))
# if puntaje < 50:
#     print("Insuficiente.")
# elif puntaje < 80:
#     print("Aceptable.")
# else:
#     print("Sobresaliente.")































