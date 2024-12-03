
# Programa 1.1 Programa que imprime un mensaje  de texto en la pantalla 
# Fecha: 2024/10/14
# Elaborado por: Jazmin Macias Sabas 
print("Hola , mi nombre es Jazmin Macias Sabas")


# Programa 1.2  Programa que solicita el nombre al usuario y lo imprime como un mensaje de texto
# Personalizado 
# Fecha: 2024/10/14
# Elaborado por: Jazmin Macias Sabas 
nombre = input ("Ingresa tu nombre:") # Método que permite ingresar texto 
# Desde el teclado 
print("Hola, " + nombre)

# Programa 1.3 Programa que imprime el número de días de una semana el nombre de una figura de 3 lados y equivalencia de 250 cm en metros
# Fecha: 2024/10/14
# Elaborado por: Jazmin Macias Sabas 
print(7)
print("Triángulo")
print(0.25)

# Programa 1.4 Probar el funcionamiento del siguiente código 
# Fecha: 2024/10/14
# Elaborado por: Jazmin Macias Sabas 
print(1 +2)
print(1 -2)
print (1*2)
print("concatenando cadenas" +"esta bien")

print("no es posible" -"restar cadenas ")

# Programa 1.5 Programa que sume, reste, divida y multiplique 2 números 
# Fecha: 2024/10/14
# Elaborado por: Jazmin Macias Sabas
num_1 = int(input("ingresa el primero número:"))
num_2 = int(input("ingresa el segundo número:"))
suma = num_1 + num_2
resta = num_1 - num_2
division = num_1 / num_2
multiplicación = num_1 * num_2
print("El valor de la suma es: " + str (suma))
print("El valor de la resta es: " + str (resta))
print("El valor de la división es: " + str (división))
print("El valor de la multiplicación es: " + str (multiplicación))

# Programa 1.6 Programa que calcula el área de un triángulo 
# Dados la base # y la altura por el usuario 
# Fecha: 2024/10/15
# Elaborado por: Jazmin Macias Sabas 
base = float(input("ingrese el valor de la base:"))
altura = float(input("ingrese el valor de la altura"))
área   = base * altura / 2
print("el area del triangulo es:" + str(área))

# Programa 1.7 Calcula el área y el perímetro de un círculo 
# ingresando el valor del radio por el usuario 
# Fecha: 2024/10/15
# Elaborado por: Jazmin Macias Sabas 
#------------------------------------------------------------------#
radio = float(input("ingresa el valor del radio:"))
areacirculo = 3.1416 * radio ** 2
perimetrocirculo =  3.1416 * 2 * radio 

print("el valor del área es:" + str(areacirculo))
print("el valor del perimetro es:" + str(perimetrocirculo))

#  Programa 1.8 Realice un programa que calcule el número de minutos, horas y meses dado el número de días por el usuario 
# Fecha: 2024/10/16
# Elaborado por: Jazmin Macias Sabas 
Días = float(input("Ingrese el número de días:"))
Horas = Días * 24
Minutos = Horas * 60
Meses = Días / 30 
print("Días:" + str(Días))
print("Horas::" + str(Horas))
print("Minutos::" + str(Minutos))
print("Meses::" + str(Meses))

# Programa 1.9 
# Fecha: 2024/10/17
# Elaborado por: Jazmin Macias Sabas 
num = 38
print (num)
num = num +1
print (num)

# Programa 1.10
# Fecha: 2024/10/17
# Elaborado por: Jazmin Macias Sabas 
print ("Hola,\n\"Osvaldo\"")
# alt 165 para la ñ 
# alt 92 para la b 
# alt 94 para ^
# alt 
#
print ("Estoy feliz \u263A\t\u2615\t\u2650")
print("Alineado:\t\u263A")

# Programa 1.11
# Fecha: 2024/10/18
# Elaborado por: Jazmin Macias Sabas 

print("-----Operador IGUAL (==)")
print(5 == 5)   # True
print(10 == 7)  # False
print(5.0 == 5) # True

print("\n-----Operador DIFERENTE o NO IGUAL (!=)")
print(5 != 5)   # False
print(10 != 7)  # True
print(5.0 != 5) # False

print("\n-----Operador MAYOR QUE (>)")
print(10 > 5) # True
print(5 > 10) # False

print("\nOperador MENOR QUE (<)")
print(5 < 10) # True
print(10 < 5) # False

print("\nOperador MENOR O IGUAL QUE (<=)")
print(5 <= 5)   # True
print(10 <= 7)  # False
print(3 <= 5)   # True

print("\nOperador MAYOR O IGUAL QUE (>=)")
print(5 >= 5)   # True
print(10 >= 7)  # False
print(3 >= 5)   # True

print("\u263A" * 10)

# Programa 1.12
# Fecha: 2024/10/18
# Elaborado por: Jazmin Macias Sabas 
print ("compuerta OR")
print (False or False)
print (False or True)
print (True or False)
print (True or True)
print("compuerta AND")
print (False and False)
print (False and True)
print (True and False)
print (True and True)

# Programa 1 Demuestre el funcionamiento compuerta NOT 
# Fecha: 2024/10/22
# Elaborado por: Jazmin Macias Sabas 
print (not True)  # Imprime False 
print (not False) # Imprime True 

# Programa 2 Programa que si Chorchis o Choto van a la fiesta 
# Fecha: 2024/10/22
# Elaborado por: Jazmin Macias Sabas 

#/ A / B // NOT (A or B) /
#/ 0 / 0 // 1
#/ 0 / 1 // 0
#/ 1 / 0 // 0
#/ 1 / 1 // 0 

print(not(False or False)) # Si hay fiesta 
print(not(False or True))  # No hay fiesta 
print(not(True or False))  # No hay fiesta 
print(not(True or True))   # No hay fiesta 

# Programa 3 Programa que comprueba el funcionamiento de la adición o concatenación  
# CONCATENACIÓN de varias cadenas de texto 
# Fecha: 2024/10/22
# Elaborado por: Jazmin Macias Sabas 
print ("Mi " + "nombre " + "es " + "Jazmin") 

# Programa 4 Calcular los impuestos y de un valor 
# Fecha: 2024/10/22
# Elaborado por: Jazmin Macias Sabas 

# Solicitamos que el usuario ingrese el valor y el porcentaje del impuesto
valor = float(input("Ingrese el valor sobre sobre el cual quieres calcular los impuestos: "))
porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto: "))

# Calculamos el impuesto
impuesto = (porcentaje_impuesto / 100) * valor

# Calculamos el total a pagar
total_a_pagar = valor + impuesto

# Resultados
print(f"El impuesto a pagar es: {impuesto:.2f}")
print(f"El total a pagar, incluyendo impuestos, es: {total_a_pagar:.2f}")
print("Gracias por usar nuestro sistema")

# Programa 5  Comparación
# Fecha:2024/10/23
# Elaborado por: Jazmin Macias Sabas 

#Comparación:
print ("perro" == "perro")
print ("perro" != "gato")
print ("Aguascalientes" < "Zacatecas")
print ("Aire" >= "Agua")

#Membership 
#operador in 
#revisa si la primer cadena está en la segunda
print ("house" in "boathouse")
print ("bien" in "bienvenidos")
print ("y" not in "ejes")
print ("je" not in "ejes")

#Slicing (Rebanar) 
#sirve para obtener un fragmento de una cadena dada. Si solo deseamos obtener un solo carácter, entonces usaremos la indexación 
#Indexing (indexado) 
mi_nombre = "Choto Chorchis"
print (mi_nombre[3])
print (mi_nombre[12])

# Programa 6 word = hamster
# Fecha: 2024/10/23
# Elaborado por: Jazmin Macias Sabas 
word = "hamster"
print (word[-1])
print (word[1:-1])
print (word[-3:])
print (word[:3])

# Programa 7 Programa que solicite la edad e indique si puede entrar un bar
# Fecha: 2024/10/24
# Elaborado por: Jazmin Macias Sabas 
edad = int(input("Ingresa tu edad: "))
if edad >=18:print("Puede ingresar al bar")
else:print("Vete a tu casa")
print("Fin del programa")

# Programa 8 Programa que calcule el promedio de 5 unidades e indique si aprobó la materia 
# Fecha: 2024/10/24
# Elaborado por: Jazmin Macias Sabas 
# Realizamos una lista para guardar las calificaciones
unidades = []

# Pedimos al usuario que ingrese las calificaciones de 5 unidades
for i in range(5):
    calificación = float(input("Ingresa la calificación de la unidad " + str(i + 1) + ": "))
    unidades.append(calificación)  # Agregamos la calificación a la lista

# Calculamos el promedio sumando todas las calificaciones y dividiendo por 5
promedio = sum(unidades) / 5

# Verificamos si el promedio es mayor o igual a 7
if promedio >= 70:
    print("Aprobaste la materia con un promedio de:", promedio)
else:
    print("Reprobaste la materia con un promedio de:", promedio)

# Programa 9 Programa que calcule el costo total de un número de artículos si: Son 3 artículos o menos precio unitario: $45.00. Más de 3 artículos precio unitario: $30. al final mostrar un mensaje 
# Fecha: 2024/10/25
# Elaborado por: Jazmin Macias Sabas 
cantidad = int(input("¿Cuantos articulos compro? "))
if cantidad>3:total = cantidad * 30
else: total = cantidad * 45
print("El total a pagar es: $" + str(total))
print("Saludos")

# Programa 10 Revisar si puedes ver una película en Netflix. la condición para esto es que seas mayor de edad y que hayas comprado la película agregar, gracias por usar Netflix 
# Fecha: 2024/10/25
# Elaborado por: Jazmin Macias Sabas 
edad = int(input("¿Cuantos años tienes?"))
if edad >=18:
    compra = int(input("¿Compraste la película?"))
    if compra ==1:
        print("Puede ver la película")
else:
    print("Vete a hacer la tarea")

