#calcuradora IMC(indice de masa corporal)

#pedir la cantidad de registrados 
print("primero persona ")
nombre = input("ingrese su nombre: ")
peso1 = float(input("ingrese su peso en kilogramos: "))
estatura1 = float(input("ingrese su estatura en metros: "))

imc = peso1 / (estatura1**2)

if imc < 18.5:
    print ("bajo peso")
elif imc <= 18.5 and imc <25 :
    print ("peso normal")
elif imc <= 25 and imc < 30 :
    print ("sobrepeso")
else:
    print("obesidad")

