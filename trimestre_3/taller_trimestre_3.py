# #ejemplo python  

# class Perro:
#     def _init_(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def ladrar(self):
#         return (f"{self.nombre} está ladrando.")

# mi_perro = Perro("Fido", 3)
# print(mi_perro.ladrar())

# class GoldenRetriever(Perro):
#         def _init_(self, nombre, edad, color):
#             super()._init_(nombre, edad)
#             self.color = color

#         def recuperar(self):
#             return (f"{self.nombre} está recuperando un objeto.")

# golden = GoldenRetriever("Buddy", 5, "dorado")
# print(golden.recuperar())



#POO en clase 

#Definición de una clase 

# class Estudiantes:
#     def __init__(self,nombre ,edad , programa_formacion):
#         self.nombre=nombre 
#         self.edad=edad
#         self.programa_formacion=programa_formacion

#     def mostrar_informacion(self):
#         print(f"nombre: {self.nombre}")
#         print(f"edad: {self.edad}")
#         print(f"programa de formación: {self.programa_formacion}")

# #creacion de la instancia del objeto 

# est1= Estudiantes("laura gomez",20,"programacion de software")
# est2= Estudiantes("clara perez",21,"programacion de software")

# #mostrar informacion

# est1.mostrar_informacion()
# est2.mostrar_informacion()

 #creacion de una calculadora basica

# class Calculadora:

#     def sumar(self, a, b):
#      return a + b 
#     def restar(self, a, b):
#      return a- b
#     def multiplicar(self, a, b):
#      return a * b
#     def dividir(self, a, b):
#      if b != 0:
#         return a / b
#      else:
#         return "error no se puede dividir entre cero"

# #programa principal

# numl = float(input ("ingresar el primer numero: ")) 
# num2 = float(input("ingresar el el segundo numero: "))

# calc = Calculadora ()

# print (f"suma: {calc.sumar (numl, num2)}")

# print(f"Resta: {calc.restar (numl, num2)}")

# print(f"Multiplicacion: {calc.multiplicar (numl, num2)}")

# print (f"División: {calc.dividir (numl, num2)}")



#parte 2

#Elige un mini-proyecto (ejemplo: biblioteca, gestión de cursos o tienda online) y

# responde:

# ¿Qué clases identificas en el problema?

# o ¿Qué atributos y métodos tendría cada clase?

# o ¿Qué relaciones existen entre ellas?

# Realiza un diagrama de clases para el problema elegido.

# Crea un diagrama de objetos con instancias concretas de tus clases.

# Dibuja un diagrama de secuencia que muestre cómo interactúan los objetos en un caso de uso (ej.: inscribir estudiante, prestar libro, hacer compra).

# Dibuja un diagrama de actividad con el flujo de pasos del caso de uso elegido

# print("El mini-proyecto es una tienda online")
# print("Las clases son producto,cliente y pedido")
# print("En clase producto los atributos son: nombre ,precio, tipo_producto y el metodo es mostrar_info()")
# print("En clase cliente  los atributos son: nombre ,correo y el metodo es ver_productos() ")
# print("En la clase pedido los atributo son: lista_productos , total(hereda de cliente) y los metodos agregar_producto(), calcular_total() y mostrar_pedido()")




#parte 3 implementación en python 


# Clase base
class Producto:
    def _init_(self, nombre, precio, tipo_producto):
        self.nombre = nombre
        self.precio = precio
        self.tipo_producto = tipo_producto

    def mostrar_info(self):
        return f"{self.nombre} - ${self.precio} (Tipo: {self.tipo_producto})"

# Clase base
class Cliente:
    def _init_(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def ver_productos(self, productos):
        print("Productos disponibles:")
        for p in productos:
            print(p.mostrar_info())

# Herencia y polimorfismo
class Pedido(Cliente):
    def _init_(self, nombre, correo):
        super()._init_(nombre, correo)
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def calcular_total(self):
        return sum(p.precio for p in self.lista_productos)

    def mostrar_pedido(self):
        print(f"\nPedido de {self.nombre}:")
        for p in self.lista_productos:
            print("-", p.nombre)
        print(f"Total a pagar: ${self.calcular_total()}")

# Ejecución
p1 = Producto("Celular", 900, "Tecnología")
p2 = Producto("Audífonos", 100, "Accesorios")

cliente = Pedido("Juan", "juan@mail.com")
cliente.ver_productos([p1, p2])
cliente.agregar_producto(p1)
cliente.agregar_producto(p2)
cliente.mostrar_pedido()
    
