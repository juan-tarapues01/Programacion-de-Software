# Sección 1 


# 1. Variable nombre
nombre = "Juan"        

# 2. Saludo personalizado
print(f" ¡Hola, {nombre}!")

# 3. Variable ciudad
ciudad = "Bogotá"      

# 4. Presentación
print(f" Hola, soy {nombre} y vivo en {ciudad}.")

# 5. Preguntar color favorito
color = input(" ¿Cuál es tu color favorito? ")

# 6. Mostrar color favorito
print(f" Tu color favorito es {color}.")

# 7. Variable animal: primero “gato”, luego se cambia a “perro”
animal = "gato"
animal = "perro"
print(f" Ahora mi animal es: {animal}")

# 8. Concatenar nombre y ciudad
presentacion = nombre + " - " + ciudad
print(f"presentacion: {presentacion}")

# 9. Pedir 4 datos al usuario
dato1 = input(" Escribe dato 1: ")
dato2 = input(" Escribe dato 2: ")
dato3 = input(" Escribe dato 3: ")
dato4 = input(" Escribe dato 4: ")
print(" Datos ingresados:", dato1, dato2, dato3, dato4)

# 10. Pedir 5 números y sumarlos
num1 = int(input(" Ingresa un número: "))
num2 = int(input(" Ingresa un número: "))
num3 = int(input(" Ingresa un número: "))
num4 = int(input(" Ingresa un número: "))
num5 = int(input(" Ingresa un número: "))
resultado_suma = num1 + num2 + num3 + num4 + num5
print(" La suma de los 5 números es:", resultado_suma)

# ───────────────────────────────────────────────
# Sección 2 ▸ Operaciones matemáticas con int (11‑20)
# ───────────────────────────────────────────────

a = 5
b = 3

print(" Suma a + b =", a + b)           # 11
print(" Resta a - b =", a - b)          # 12

multiplicacion = a * b                     # 13
print(" Multiplicación a * b =", multiplicacion)

division = a / b                           # 14
print(" División a / b =", division)

potencia = a ** b                          # 15
print(" a elevado a la potencia b =", potencia)

edad = int(input(" ¿Cuántos años tienes? "))  # 16
print(" En 10 años tendrás:", edad + 10)      # 17

n1 = int(input(" Ingresa un número: "))       # 18
n2 = int(input(" Ingresa otro número: "))
print("La suma es:", n1 + n2)

print("Residuo:", a % b)  #19


x = int(input("Primer número: "))
y = int(input("Segundo número: "))
z = int(input("Tercer número: "))        #20
promedio = (x + y + z) / 3
print("Promedio:", promedio)

# 21. Nombre completo
nombre_completo = input("Escribe tu nombre completo: ")

# 22. Mostrar solo primer nombre
primer_nombre = nombre_completo.split()[0]
print("Tu primer nombre es:", primer_nombre)

# 23. Mayor de dos números
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
if num1 > num2:
    print("El mayor es:", num1)
elif num2 > num1:
    print("El mayor es:", num2)
else:
    print("Son iguales")

# 24. Calcular edad a partir del año de nacimiento
anio_nacimiento = int(input("¿En qué año naciste? "))
edad = 2025 - anio_nacimiento
print("Tienes", edad, "años.")

# 25. Mensaje con año y edad
nombre = input("¿Cuál es tu nombre? ")
print("Hola", nombre + ", naciste en", anio_nacimiento, "y tienes", edad, "años.")

# 26. Fruta favorita
fruta = input("¿Cuál es tu fruta favorita? ")
print("Me gusta la", fruta)

# 27. Operaciones con dos números
a = int(input("Dame un número: "))
b = int(input("Dame otro número: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)









