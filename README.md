# Bloques-de-programa-1-y-2-
Explicación de los programas 
```
Ejercicio 1.1 Crea un programa que muestre tu nombre. 
# Programa 1.1 Programa que imprime un mensaje  de texto en la pantalla 
# Fecha: 2024/10/14
# Elaborado por: Jazmin Macias Sabas 
print("Hola , mi nombre es Jazmin Macias Sabas")
```

```
Ejercicio 1.2 Realice un programa que solicite el nombre al usuario e imprima un mensaje personalizado con el nombre ingresado 
# Programa 1.2  Programa que solicita el nombre al usuario y lo imprime como un mensaje de texto
# Personalizado 
# Fecha: 2024/10/14
# Elaborado por: Jazmin Macias Sabas 
nombre = input ("Ingresa tu nombre:") # Método que permite ingresar texto 
# Desde el teclado 
print("Hola, " + nombre)
```
nombre = input("Ingresa tu nombre:"):
Esta línea usa la función input(), que permite al programa recibir texto del usuario a través del teclado. El texto que aparece entre paréntesis y comillas ("Ingresa tu nombre:") es lo que verá el usuario como una especie de pregunta o instrucción. Cuando el usuario escribe su nombre y presiona "Enter", ese valor se almacena en la variable nombre.

print("Hola, " + nombre):
En esta línea, se utiliza nuevamente la función print() para mostrar un mensaje en la pantalla. El mensaje es "Hola, " seguido del contenido de la variable nombre. El operador + se utiliza aquí para concatenar (unir) cadenas de texto. Por ejemplo, si el usuario ingresó "Jazmin", el programa imprimirá "Hola, Jazmin".

```
Ejercicio 1.3 Realice un programa que imprima 3 tipos de datos diferentes 
# Programa 1.3 Programa que imprime el número de días de una semana el nombre de una figura de 3 lados y equivalencia de 250 cm en metros
# Fecha: 2024/10/14
# Elaborado por: Jazmin Macias Sabas 
print(7)
print("Triángulo")
print(0.25)
```
print(7):
Esta línea utiliza la función print() de Python, que sirve para mostrar en la pantalla lo que se le indique. En este caso, se le indica que imprima el número entero 7, que representa el número de días de una semana.

print("Triángulo"):
Aquí se vuelve a utilizar la función print(), esta vez para imprimir una cadena de texto, en este caso la palabra "Triángulo", que hace referencia a una figura de tres lados.

print(0.25*:
La última línea también usa la función print(). En este caso, se imprime un número en coma flotante, concretamente 0.25, que representa la equivalencia de 250 centímetros en metros.

Cuando se ejecuta este programa, se imprimirán en la pantalla las tres líneas: "7", "Triángulo" y "0.25", una debajo de la otra. Cada línea representa un tipo de dato diferente: entero, texto y decimal respectivamente.

```
Ejercicio 1.4 Compruebe el funcionamiento del siguiente programa 
# Programa 1.4 Probar el funcionamiento del siguiente código 
# Fecha: 2024/10/14
# Elaborado por: Jazmin Macias Sabas 
print(1 +2)
print(1 -2)
print (1*2)
print("concatenando cadenas" +"esta bien")

print("no es posible" -"restar cadenas ")
```
print(1 + 2):
Esta línea utiliza la función print() de Python para imprimir el resultado de la suma de los números 1 y 2. Al ejecutar este programa, se imprimirá el valor "3" en la pantalla.

print(1 - 2):
Aquí se vuelve a utilizar la función print(), esta vez para imprimir el resultado de la resta de los números 1 y 2. El resultado mostrado será "-1".

print(1 * 2):
Nuevamente se usa print() para imprimir el producto de los números 1 y 2, que es 2.

print("concatenando cadenas" + "esta bien"):
En esta línea se utiliza la función print() para mostrar la concatenación de dos cadenas de texto: "concatenando cadenas" y "esta bien". El operador + se utiliza para unir las dos cadenas y se imprimirá "concatenando cadenasesta bien".

print("no es posible" - "restar cadenas "):
Aquí se intenta realizar una operación no permitida, ya que no se pueden restar cadenas de texto. Al ejecutar este comando, Python generará un error de tipo TypeError.

```
Ejercicio 1.5 Realice un programa que que sume, reste, divida, y multiplique dos números e imprima el resultado 
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
```
num_1 = int(input("ingresa el primero número:")):
En esta línea se utiliza la función input() para pedir al usuario que ingrese el primer número. La función int() se utiliza para convertir el valor introducido en un número entero (sin decimales), y este valor se guarda en la variable num_1.

num_2 = int(input("ingresa el segundo número:")):
Aquí se pide al usuario que ingrese el segundo número, siguiendo el mismo procedimiento que para el primer número. Este valor se almacena en la variable num_2.

suma = num_1 + num_2:
Esta línea calcula la suma de num_1 y num_2 y guarda el resultado en la variable suma.

resta = num_1 - num_2:
Aquí se calcula la resta entre num_1 y num_2 y se guarda el resultado en la variable resta.

division = num_1 / num_2:
Esta línea calcula la división de num_1 por num_2 y guarda el resultado en la variable division. Si num_2 es igual a cero, ocurrirá un error de ZeroDivisionError.

multiplicación = num_1 * num_2*:
Aquí se multiplican num_1 y num_2 y el resultado se guarda en la variable multiplicación.

print("El valor de la suma es: " + str(suma)):
En esta línea, la función print() imprime el texto "El valor de la suma es: " concatenado con el valor de la variable suma. La función str() se utiliza para convertir el valor numérico de suma en una cadena de texto para poder concatenarlo.

print("El valor de la resta es: " + str(resta)):
Aquí se imprime el texto "El valor de la resta es: " junto con el valor de la variable resta.

print("El valor de la división es: " + str(división)):
Esta línea imprime el texto "El valor de la división es: " concatenado con el resultado de la variable división.

print("El valor de la multiplicación es: " + str(multiplicación))*:
este muestra el resultado

 ```
Ejercicio 1.6 Realice un programa que solicite la base y la altura y calcule el área de un triángulo 
# Programa 1.6 Programa que calcula el área de un triángulo 
# Dados la base # y la altura por el usuario 
# Fecha: 2024/10/15
# Elaborado por: Jazmin Macias Sabas 
base = float(input("ingrese el valor de la base:"))
altura = float(input("ingrese el valor de la altura"))
área   = base * altura / 2
print("el area del triangulo es:" + str(área))
 ```
base = float(input("ingrese el valor de la base:")):
En esta línea se utiliza la función input() para solicitar al usuario que ingrese el valor de la base del triángulo. La función float() se utiliza para convertir el valor introducido en un número decimal, y este valor se guarda en la variable base.

altura = float(input("ingrese el valor de la altura")):
Aquí se pide al usuario que ingrese el valor de la altura del triángulo, siguiendo el mismo procedimiento que para la base. Este valor se almacena en la variable altura.

área = base * altura / 2:
Esta línea calcula el área del triángulo, usando la fórmula base * altura / 2, y guarda el resultado en la variable área.

print("el area del triangulo es:" + str(área)):
En esta línea, la función print() imprime el texto "el área del triángulo es:" concatenado con el valor de la variable área. La función str() se utiliza para convertir el valor numérico de área en una cadena de texto para poder concatenarlo.

Al ejecutar el programa, se pedirá al usuario que ingrese la base y la altura del triángulo. Una vez ingresados ambos valores, se calculará el área y se mostrará el resultado en pantalla.

 ```
Ejercicio 1.7 Ingresado por el usuario el radio de un círculo, calcule su perímetro y área
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
 ```
radio = float(input("ingresa el valor del radio:")):
En esta línea se utiliza la función input() para solicitar al usuario que ingrese el valor del radio del círculo. La función float() se utiliza para convertir el valor introducido en un número decimal, y este valor se guarda en la variable radio.

areacirculo = 3.1416 * radio * 2:
Aquí se calcula el área del círculo, utilizando la fórmula 3.1416 * radio ** 2, y se guarda el resultado en la variable areacirculo.

perimetrocirculo = 3.1416 * 2 * radio:
Esta línea calcula el perímetro del círculo, usando la fórmula 3.1416 * 2 * radio, y guarda el resultado en la variable perimetrocirculo.

print("el valor del área es:" + str(areacirculo)):
En esta línea, la función print() imprime el texto "el valor del área es:" concatenado con el valor de la variable areacirculo. La función str() se utiliza para convertir el valor numérico de areacirculo en una cadena de texto para poder concatenarlo.

print("el valor del perimetro es:" + str(perimetrocirculo)):
Aquí se imprime el texto "el valor del perímetro es:" junto con el valor de la variable perimetrocirculo.

Cuando se ejecuta el programa, se pedirá al usuario que ingrese el radio del círculo. Una vez ingresado el valor, se calcularán el área y el perímetro del círculo, y se mostrarán los resultados en pantalla.

 ```
Ejercicio 1.8 Realice un programa que calcule el número de minutos, horas y meses dado el número de días por el usuario 
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
 ```
Días = float(input("Ingrese el número de días:")):
En esta línea se utiliza la función input() para solicitar al usuario que ingrese el número de días. La función float() se utiliza para convertir el valor introducido en un número decimal, y este valor se guarda en la variable Días.

Horas = Días * 24*:
Aquí se calculan las horas equivalentes al número de días ingresado, utilizando la fórmula Días * 24, y se guarda el resultado en la variable Horas.

Minutos = Horas * 60:
Esta línea calcula el número de minutos equivalentes al número de horas calculado anteriormente, utilizando la fórmula Horas * 60. El resultado se guarda en la variable Minutos.

Meses = Días / 30:
Aquí se calcula el número de meses equivalentes al número de días ingresado, utilizando la fórmula Días / 30. Este resultado se guarda en la variable Meses.

print("Días:" + str(Días)):
En esta línea, la función print() imprime el texto "Días:" concatenado con el valor de la variable Días. La función str() se utiliza para convertir el valor numérico de Días en una cadena de texto para poder concatenarlo.

print("Horas::" + str(Horas)):
Aquí se imprime el texto "Horas::" junto con el valor de la variable Horas.

print("Minutos::" + str(Minutos)):
En esta línea se imprime el texto "Minutos::" concatenado con el valor de la variable Minutos.

print("Meses::" + str(Meses)):
 Aquí se imprime el texto "Meses::" junto con el valor de la variable Meses.

Cuando se ejecuta el programa, se pedirá al usuario que ingrese el número de días. Una vez ingresado el valor, se calcularán el número equivalente de minutos, horas y meses, y se mostrarán los resultados en pantalla.

 ```
Ejercicio 1.9 variables
# Programa 1.9 
# Fecha: 2024/10/17
# Elaborado por: Jazmin Macias Sabas 
num = 38
print (num)
num = num +1
print (num)
```
num = 38:
En esta línea se crea una variable llamada num y se le asigna el valor entero 38.

print(num):
Aquí se imprime en pantalla el valor actual de la variable num, que en este caso es 38.

num = num + 1:
En esta línea se actualiza el valor de la variable num. Se suma 1 al valor actual de num (38) y se guarda el resultado (39) en la misma variable num.

print(num):
Aquí se imprime en pantalla el valor actualizado de la variable num, que ahora es 39.

Cuando se ejecuta este programa, se muestra primero el valor inicial de num (38), luego se actualiza el valor de num sumándole 1, y finalmente se muestra el valor actualizado (39). Este programa es un ejemplo básico de cómo se pueden crear, manipular y mostrar las variables en Python.

```
Ejercicio 1.10 Unicode 
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
```
print("Hola,\n\"Osvaldo\""):
Aquí se imprime la cadena "Hola, \"Osvaldo\"" en pantalla. La secuencia de escape \n hace que se imprima el texto "Osvaldo" en una línea nueva. La barra invertida \ antes de las comillas dobles " hace que las comillas se interpreten como parte de la cadena y no como el fin de la cadena.

print("Estoy feliz \u263A\t\u2615\t\u2650"):
Esta línea imprime la cadena "Estoy feliz" seguida de tres símbolos Unicode, una cara sonriente (\u263A), una taza de café (\u2615) y una cruz (\u2650). La secuencia de escape \t hace que haya una tabulación entre los símbolos Unicode.

print("Alineado:\t\u263A")*:
Aquí se imprime la cadena "Alineado:", una tabulación (\t) y el símbolo Unicode de la cara sonriente (\u263A). La tabulación hace que el símbolo Unicode se alinee con el texto "Alineado:".

Cuando se ejecuta este programa, se imprimirán los mensajes y los símbolos Unicode en pantalla, mostrando cómo se pueden utilizar caracteres especiales y secuencias de escape en las cadenas de Python.

```
Ejercicio 1.11 Programa para analizar los operadores de comparación 
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
```
"print("-----Operador IGUAL (==)")":
Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos del operador de igualdad (==).

"print(5 == 5)   # True":
Aquí se imprime el resultado de la comparación 5 == 5, que es True, ya que 5 es igual a 5.

"print(10 == 7)  # False":
Esta línea imprime el resultado de la comparación 10 == 7, que es False, ya que 10 no es igual a 7.

"print(5.0 == 5) # True":
Aquí se imprime el resultado de la comparación 5.0 == 5, que es True, ya que 5.0 es igual a 5.

"print("\n-----Operador DIFERENTE o NO IGUAL (!=)")":
Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos del operador de desigualdad (!=).

"print(5 != 5)   # False":
Aquí se imprime el resultado de la comparación 5 != 5, que es False, ya que 5 es igual a 5.

"print(10 != 7)  # True":
Esta línea imprime el resultado de la comparación 10 != 7, que es True, ya que 10 no es igual a 7.

"print(5.0 != 5) # False":
Aquí se imprime el resultado de la comparación 5.0 != 5, que es False, ya que 5.0 es igual a 5.

"print("\n-----Operador MAYOR QUE (>)")":
Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos del operador de mayor que (>).

"print(10 > 5) # True":
Aquí se imprime el resultado de la comparación 10 > 5, que es True, ya que 10 es mayor que 5.

"print(5 > 10) # False":
Esta línea imprime el resultado de la comparación 5 > 10, que es False, ya que 5 no es mayor que 10.

"print("\nOperador MENOR QUE (<)")":
Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos del operador de menor que (<).

```
Ejercicio 1.12 Programa para probar las compuertas lógicas AND OR 
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
```
"print("compuerta OR")":
Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos de la compuerta lógica "OR".

"print(False or False)":
Aquí se imprime el resultado de la expresión False or False, que es False, ya que ambos valores son falsos.

"print(False or True)":
Esta línea imprime el resultado de la expresión False or True, que es True, ya que al menos uno de los valores es verdadero.

"print(True or False)":
Aquí se imprime el resultado de la expresión True or False, que es True, ya que al menos uno de los valores es verdadero.

"print(True or True)":
Esta línea imprime el resultado de la expresión True or True, que es True, ya que ambos valores son verdaderos.

"print("compuerta AND")":
Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos de la compuerta lógica "AND".

print(False and False)
Aquí se imprime el resultado de la expresión False and False, que es False, ya que ambos valores son falsos.

"print(False and True)":
Esta línea imprime el resultado de la expresión False and True, que es False, ya que al menos uno de los valores es falso.

"print(True and False)":
Aquí se imprime el resultado de la expresión True and False, que es False, ya que al menos uno de los valores es falso.

"print(True and True):
Esta línea imprime el resultado de la expresión True and True, que es True, ya que ambos valores son verdaderos.

Cuando se ejecuta este programa, se muestran los resultados de diferentes combinaciones de valores booleanos usando las compuertas lógicas "OR" y "AND".

```
Ejercicio 1 Compuerta NOT
# Programa 1 Demuestre el funcionamiento compuerta NOT 
# Fecha: 2024/10/22
# Elaborado por: Jazmin Macias Sabas 
print (not True)  # Imprime False 
print (not False) # Imprime True 
```
"print(not True)  # Imprime False":
Esta línea imprime el resultado de la expresión not True, que es False. La compuerta NOT invierte el valor True a False.

"print(not False) # Imprime True":
Aquí se imprime el resultado de la expresión not False, que es True. La compuerta NOT invierte el valor False a True.

Cuando se ejecuta este programa, se muestran los resultados de las expresiones utilizando la compuerta lógica NOT, demostrando su funcionamiento al invertir valores booleanos.

```
Ejercicio 2 Programa que si Chorchis o Choto van a la fiesta, no hay fiesta 
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
```

"#/ A / B // NOT (A or B) /":
Estas líneas son comentarios que representan una tabla de verdad de la función lógica NOT(A or B).

"print(not(False or False)) # Si hay fiesta":
Aquí se imprime el resultado de la expresión not(False or False), que es True. Como ni Chorchis ni Choto van a la fiesta (ambos valores son False), entonces sí hay fiesta.

"print(not(False or True))  # No hay fiesta":
Esta línea imprime el resultado de la expresión not(False or True), que es False. Como Chorchis no va a la fiesta pero Choto sí (valores False y True respectivamente), entonces no hay fiesta.

"print(not(True or False))  # No hay fiesta":
Aquí se imprime el resultado de la expresión not(True or False), que es False. Como Chorchis va a la fiesta pero Choto no (valores True y False respectivamente), entonces no hay fiesta.

"print(not(True or True))   # No hay fiesta":
Esta línea imprime el resultado de la expresión not(True or True), que es False. Como tanto Chorchis como Choto van a la fiesta (ambos valores son True), entonces no hay fiesta.

Cuando se ejecuta este programa, se muestran los resultados de las expresiones utilizando las compuertas lógicas NOT y OR, que representan la situación de que si Chorchis o Choto van a la fiesta, entonces no hay fiesta.


```
Ejercicio 3 Funcionamiento de adicción y concatenación de varias variables 
# Programa 3 Programa que comprueba el funcionamiento de la adición o concatenación  
# CONCATENACIÓN de varias cadenas de texto 
# Fecha: 2024/10/22
# Elaborado por: Jazmin Macias Sabas 
print ("Mi " + "nombre " + "es " + "Jazmin") 
```
print("Mi " + "nombre " + "es " + "Jazmin"):
Esta línea es donde ocurre la concatenación real. Utiliza el operador + para unir varias cadenas de texto. Cada cadena está separada por un espacio, y al ejecutarse, se combinan todas las partes en una sola cadena resultante.

   - "Mi ": La primera cadena.
   - "nombre ": La segunda cadena.
   - "es ": La tercera cadena.
   - "Jazmin": La cuarta cadena.

Al concatenar estas cadenas, el resultado final es la oración: *"Mi nombre es Jazmin"*. 

Cuando se ejecuta este programa, imprime en la consola la frase completa resultante de la concatenación, mostrando cómo se pueden unir múltiples cadenas para formar un mensaje coherente. ¡Es una manera sencilla y efectiva de trabajar con texto en Python!

```
Ejercicio 4 Programa que calcula los impuestos de un valor
# Programa 4 Calcular los impuestos y dar un valor 
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
```
"valor = float(input("Ingrese el valor sobre sobre el cual quieres calcular los impuestos: "))":
En esta línea, se solicita al usuario que ingrese un valor (valor original) sobre el cual se calcularán los impuestos. La función float() se utiliza para convertir la entrada del usuario en un número decimal.

"porcentaje_impuesto = float(input("Ingrese el porcentaje de impuesto: "))":
En esta línea, se solicita al usuario que ingrese el porcentaje de impuesto que se aplicará al valor original. También se utiliza la función float() para convertir la entrada del usuario en un número decimal.

"impuesto = (porcentaje_impuesto / 100) * valor":
Aquí se calcula el impuesto, multiplicando el valor original por el porcentaje de impuesto dividido por 100.

"total_a_pagar = valor + impuesto":
En esta línea, se calcula el total a pagar sumando el valor original y el impuesto calculado.

"print(f"El impuesto a pagar es: {impuesto:.2f}")":
Aquí se imprime el valor del impuesto calculado con 2 dígitos decimales.

"print(f"El total a pagar, incluyendo impuestos, es: {total_a_pagar:.2f}")":
En esta línea, se muestra el total a pagar con impuestos incluidos, también con 2 dígitos decimales.

"print("Gracias por usar nuestro sistema")":
Aquí se imprime un mensaje de agradecimiento al usuario por utilizar el programa.

Cuando se ejecuta el programa, solicita al usuario los valores necesarios y calcula el impuesto y el total a pagar. Finalmente, muestra los resultados por pantalla.

```
Ejercicio 5 Comparación, membership, indexing, método de slicing  
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
```
Comparación:

print("perro" == "perro"): Aquí se utiliza el operador de comparación == para comparar dos cadenas. Si son idénticas, la expresión devolverá True; en este caso, se imprime True porque ambas cadenas son "perro".

print("perro" != "gato"): Este ejemplo utiliza el operador !=, que compara si dos cadenas son diferentes. En este caso, como "perro" y "gato" son distintos, se imprime True.

print("Aguascalientes" < "Zacatecas"): Aquí se utiliza el operador < para comparar cadenas alfabéticamente. Si la primera cadena viene antes alfabéticamente que la segunda, la expresión devolverá True. En este ejemplo, como "Aguascalientes" alfabéticamente viene antes que "Zacatecas", se imprime True.

print("Aire" >= "Agua"): Este ejemplo usa el operador >= para una comparación alfabética. Devolverá True si la primera cadena es alfabéticamente mayor o igual que la segunda. Como "Aire" alfabéticamente está después que "Agua", se imprime True.

Membership (Pertenencia):

El operador in se utiliza para comprobar si una cadena aparece dentro de otra.

print("house" in "boathouse"): Aquí se evalúa si la cadena "house" aparece en la cadena "boathouse". Como la cadena "house" sí está presente en "boathouse", la expresión devuelve True.

print("bien" in "bienvenidos"): En este caso, la palabra "bien" sí forma parte de la palabra "bienvenidos", por lo que se imprime True.

print("y" not in "ejes"): Aquí se utiliza la negación del operador in, buscando si la cadena "y" no está presente en la cadena "ejes". Como la letra "y" no está presente en "ejes", se imprime True.

print("je" not in "ejes"): En este caso, se busca si la subcadena "je" no está presente en "ejes". Como "je" sí está presente en "ejes", la expresión es falsa, y se imprime False.

Indexing (Indexación):

mi_nombre = "Choto Chorchis": Se crea una variable llamada mi_nombre y se le asigna la cadena "Choto Chorchis".

print(mi_nombre[3]): Aquí se utiliza la indexación para acceder al cuarto carácter de la cadena mi_nombre, ya que la indexación en Python empieza en 0. En este caso, se imprime la letra "t", que está en la posición 3 (cuarta letra).

```
Ejercicio 6 word = hamster
# Programa 6 word = hamster
# Fecha: 2024/10/23
# Elaborado por: Jazmin Macias Sabas 
word = "hamster"
print (word[-1])
print (word[1:-1])
print (word[-3:])
print (word[:3])
```
word = "hamster": Se define una variable llamada word y se le asigna la cadena "hamster".

print(word[-1]): Aquí se accede al último carácter de la cadena word mediante indexación negativa, donde -1 representa el último carácter. En este caso, se imprime la letra "r".

print(word[1:-1]): Este ejemplo utiliza rebanado (slicing) para obtener una subcadena de word, empezando desde la posición 1 y terminando en la posición -1 (la penúltima letra). Esto imprime la subcadena "amste", excluyendo la primera y la última letra de la palabra original.

print(word[-3:]): En este caso, se utiliza rebanado para obtener una subcadena que empieza desde la tercera última letra hasta el final de la palabra word. Se imprime la subcadena "ster".

print(word[:3]): Aquí se obtiene una subcadena de word que va desde el inicio hasta la posición 2 (ya que la indexación empieza en 0), utilizando rebanado. Se imprime la subcadena "ham", que son las primeras tres letras de la palabra original.

```
Ejercicio 7 El bar”
# Programa 7 Programa que solicite la edad e indique si puede entrar un bar
# Fecha: 2024/10/24
# Elaborado por: Jazmin Macias Sabas 
edad = int(input("Ingresa tu edad: "))
if edad >=18:print("Puede ingresar al bar")
else:print("Vete a tu casa")
print("Fin del programa")
```
edad = int(input("Ingresa tu edad: ")): Esta línea pide al usuario que ingrese su edad a través de la función input(). La función int() convierte la entrada del usuario en un número entero y lo almacena en la variable edad.

if edad >= 18:: Esta es una sentencia condicional if que verifica si la edad ingresada es mayor o igual a 18. Si la condición se cumple, se ejecutará el bloque de código que está indentado justo debajo de esta línea.

print("Puede ingresar al bar"): Si la edad es mayor o igual a 18, se imprimirá este mensaje informando al usuario que puede ingresar al bar.

else:: Si la condición if anterior no se cumple (la edad es menor que 18), se ejecutará este bloque else.

print("Vete a tu casa"): En caso de que la edad sea menor que 18, se imprimirá este mensaje indicando que no puede ingresar al bar.

print("Fin del programa"): Este mensaje se imprimirá al final, independientemente de si la edad es mayor o menor que 18, indicando el final del programa.

Este programa utiliza una estructura de control condicional (if-else) para determinar qué bloque de código ejecutar en función de la edad ingresada por el usuario.

```
Ejercicio 8 Calificaciones aprobó o reprobó
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
```
unidades = []: Esta línea inicializa una lista vacía llamada unidades que se utilizará para almacenar las calificaciones de cada unidad.

for i in range(5):: Se utiliza un bucle for para recorrer cinco iteraciones, ya que hay cinco unidades en total.

calificación = float(input("Ingresa la calificación de la unidad " + str(i + 1) + ": ")): Dentro del bucle, se solicita al usuario que ingrese la calificación de cada una de las cinco unidades. La función float() se utiliza para convertir la entrada del usuario en un número decimal. Se utiliza str(i + 1) para mostrar al usuario el número de la unidad actual (de 1 a 5).

unidades.append(calificación): Se agrega la calificación ingresada por el usuario a la lista unidades usando el método append().

promedio = sum(unidades) / 5: Se calcula el promedio sumando todas las calificaciones almacenadas en la lista unidades y dividiendo la suma por 5, que es el número de unidades.

if promedio >= 70:: Aquí, se utiliza una sentencia condicional if para comprobar si el promedio calculado es mayor o igual a 70 (por ciento). Si la condición se cumple, se ejecutará el bloque de código indentado debajo de esta línea.

print("Aprobaste la materia con un promedio de:", promedio): Si el promedio es mayor o igual a 70, se imprime un mensaje informando al usuario que aprobó la materia y se muestra el promedio obtenido.

else:: Si la condición if anterior no se cumple (el promedio es menor que 70), se ejecutará este bloque else.

print("Reprobaste la materia con un promedio de:", promedio): Si el promedio es menor que 70, se imprime un mensaje indicando que el usuario reprobó la materia y se muestra el promedio obtenido.

Este programa utiliza un bucle for para solicitar y almacenar las calificaciones de las unidades, luego calcula el promedio y finalmente utiliza una estructura de control condicional if-else para determinar si el usuario aprobó o reprobó la materia.

```
Ejercicio 9 Costo total de un número de artículos  
# Programa 9 Programa que calcule el costo total de un número de artículos si: Son 3 artículos o menos precio unitario: $45.00. Más de 3 artículos precio unitario: $30. al final mostrar un mensaje 
# Fecha: 2024/10/25
# Elaborado por: Jazmin Macias Sabas 
cantidad = int(input("¿Cuantos articulos compro? "))
if cantidad>3:total = cantidad * 30
else: total = cantidad * 45
print("El total a pagar es: $" + str(total))
print("Saludos")
```
cantidad = int(input("¿Cuantos articulos compro? ")): Se solicita al usuario que ingrese la cantidad de artículos que compró. La función input() recoge la entrada como una cadena de texto, y luego int() convierte esa entrada en un número entero, que se almacena en la variable cantidad.

if cantidad > 3:: Aquí se utiliza una sentencia condicional if para verificar si la cantidad de artículos comprados es mayor a 3.

total = cantidad * 30*: Si la condición anterior es verdadera (es decir, si el usuario compró más de 3 artículos), se calcula el total multiplicando la cantidad de artículos por el precio unitario de $30. Este valor se almacena en la variable total.

else:: Si la condición del if no se cumple (lo que significa que el usuario compró 3 artículos o menos), se ejecutará este bloque else.

total = cantidad * 45*: En este caso, se calcula el total multiplicando la cantidad de artículos por el precio unitario de $45 y se almacena en la variable total.

print("El total a pagar es: $" + str(total)): Después de calcular el total, esta línea imprime el costo total a pagar. Se utiliza str(total) para convertir el valor numérico total en una cadena para poder concatenarlo con el mensaje.

print("Saludos"): Finalmente, se imprime un mensaje de despedida que dice "Saludos".

Este programa utiliza una estructura condicional para aplicar diferentes precios según la cantidad de artículos y luego muestra el total a pagar al usuario. Es una forma efectiva de calcular costos basados en condiciones específicas.

```
Ejercicio 10 Película de Netflix 
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
```
edad = int(input("¿Cuantos años tienes?")): Se solicita la edad del usuario y se convierte en un número entero para su almacenamiento en la variable edad.

if edad >= 18:: Se comprueba si la edad es mayor o igual a 18, ya que esto es la condición para poder ver la película.

compra = int(input("¿Compraste la película?")): Se pregunta al usuario si ha comprado la película. La entrada se convierte en un número entero y se guarda en la variable compra.

if compra == 1:: Se verifica si el valor de compra es igual a 1, lo que significa que el usuario compró la película.

print("Puede ver la película"): Si la condición anterior se cumple (la persona es mayor de edad y ha comprado la película), se imprime un mensaje indicando que puede ver la película.

else:: Si la edad del usuario es menor que 18, se ejecutará este bloque else.

print("Vete a hacer la tarea"): Se imprime un mensaje indicando que el usuario debe ir a hacer la tarea, ya que no cumple con las condiciones para ver la película.

Este programa utiliza estructuras condicionales para validar la edad del usuario y la compra de la película, permitiéndole ver la película solo si las condiciones son satisfactorias.
