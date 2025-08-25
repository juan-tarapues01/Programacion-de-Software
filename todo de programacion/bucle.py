# num= int(input("ingrese un numero: "))

# while num>0:
#     print(f"{num}")
#     num -= 1
# print("Terminó el conteo")




# numero = int(input( "ingrese numero de la tabla  de multiplicar: "))


# i=1 #inicialización
# print(f"\ninicia el contador en 1 {numero}")

# while i <=10:
#     print(f"{numero}*{i}= {numero*i}")
#     i += 1
# print("Termino")    



# numero2=int(input("ingrese un numero: "))

# while True:
#     numero2 -=1
#     print(numero2)
#     if numero2 == 0:
#         break
# print("fin del bucle")


# x = 5
# while True:
#     x -=1
#     print(x)
#     if x == 0:
#         break
# print("Fn del bucle")

# suma=0
        
# numero=int(input("ingrese un numero: "))

# while numero !=0:
#     suma+=numero
#     numero=int(input("Ingrese un numero mas: "))
#     print (suma)

# "ejercicio 2"    

# contraseña_correcta= (input("ingrese una contraseña: "))


# while contraseña_correcta != "python123":
#     contraseña_correcta=(input("por favor ingrese la contraseña: "))
#     if contraseña_correcta!="python123":
#         print("Contrseña incorrecta")
# print ("contreseña correcta")


# "ejercicio 3"

# lista_compras = []
# producto = ""

# while producto.lower() != "fin":
#     producto = input("Introduce un producto (escribe 'fin' para terminar con la compra): ")
#     if producto.lower() != "fin":
#         lista_compras.append(producto)

# print(lista_compras)

# "ejercicio 4"

# contador_pares = 0
# contador_impares = 0
# numeros_pedidos = 0

# while numeros_pedidos < 10:
#         numero = int(input(f"Introduce el número {numeros_pedidos + 1}: "))
#         if numero % 2 == 0:
#             contador_pares += 1
#         else:
#             contador_impares += 1
#         numeros_pedidos += 1

        
# print(f"\nNúmeros pares: {contador_pares}")      
# print(f"Números impares: {contador_impares}")



# "ejercicio 5"

# notas = []
# nota_ingresada = ""

# print("escribe 'salir' para terminar")

# while nota_ingresada != "salir":
#     nota_ingresada = input("Introduce una nota entre 0 y 5 : ")
#     if nota_ingresada!= "salir":
        
#             nota = float(nota_ingresada)
#             if 0 <= nota <= 5:
#                 notas.append(nota)
#             else:
#                 print("La nota debe estar entre 0 y 5.")
        
            

# if notas:
#     promedio = sum(notas) / len(notas)
#     print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")
# else:
#     print("No se ingresaron calificaciones.")


# "ejercicio 6"


# numero = int(input( "ingrese numero de la tabla  de multiplicar: "))


# i=1 #inicialización
# print(f"\ninicia el contador en 1 {numero}")

# while i <=10:
#     print(f"{numero}*{i}= {numero*i}")
#     i += 1
# print("Termino")    



# "ejercicio 7"

# adivinanza=""
# suposición=int(input("Ingrese un numero: "))

# while adivinanza!= 17:
#     suposición=int(input("Ingrese un numero: "))
#     if suposición > 17:
#         print("el numero debe ser menor , sigue intentando")
#     elif suposición < 17:
#         print("el numero debe ser mayor , sigue intentando")
#     else:
#         print(f"lo lograste el numero era {suposición}")
    


# "ejercicio 8"


# frutas_disponibles = ("manzana", "banana", "uva", "fresa", "naranja", "kiwi")

# adivinanza_correcta = False
# while not adivinanza_correcta:
#     intento_usuario = input("Adivina una fruta: ").lower()
#     if intento_usuario in frutas_disponibles:
#         print(f"¡Felicidades! Adivinaste una fruta que está en la tupla: {intento_usuario}")
#         adivinanza_correcta = True
#     else:
#         print("Esa fruta no está en la tupla. Intenta de nuevo.")


# "ejercicio 9"

# diccionario_traduccion = {
#     "hola": "hello",
#     "adios": "goodbye",
#     "gracias": "thank you",
#     "por favor": "please",
#     "agua": "water"
# }

# print("escribe 'salir' para terminar")
# while True:
#     palabra_espanol = input("Ingresa una palabra en español: ").lower()
#     if palabra_espanol == "salir":
#         print("Saliendo del diccionario.")
#         break
#     if palabra_espanol in diccionario_traduccion:
#         print(f"La traducción de '{palabra_espanol}' es: {diccionario_traduccion[palabra_espanol]}")
#     else:
#         print(f"La palabra '{palabra_espanol}' no se encuentra en el diccionario.")


# "ejercicio 10"

# print("Elija la opcion segun su respectivo numero. ")

# while True:
#     print("\n--- Calculadora Básica ---")
#     print("1. Sumar")
#     print("2. Restar")
#     print("3. Multiplicar")
#     print("4. Dividir")
#     print("5. Salir")
    
 
#     opcion = input("Elige una opción: ")

#     if opcion in ('1', '2', '3', '4','5'):
    
#             num1 = float(input("Ingresa el primer número: "))
#             num2 = float(input("Ingresa el segundo número: "))
        
        

#             if opcion == '1':
#                print(f"Resultado: {num1 + num2}")
#             elif opcion == '2':
#                print(f"Resultado: {num1 - num2}")
#             elif opcion == '3':
#                print(f"Resultado: {num1 * num2}")
#             elif opcion == '4':
#                 if num2 != 0:
#                  print(f"Resultado: {num1 / num2}")
#                 else:
#                  print("Error: No se puede dividir por cero.")
#             elif opcion == '5':
#              print("Saliendo de la calculadora.")
#             break
#     else:
#         print("Opción inválida. Por favor, elige una opción del 1 al 5.")



# "ejercicio 11"        


