# Bloques-de-programa-1-y-2-
Explicación de los programas 
```
Ejercicio 1.1 Crea un programa que muestre tu nombre. 
# Programa 1.1 Programa que imprime un mensaje  de texto en la pantalla 
# Fecha: 2024/10/14
# Elaborado por: Jazmin Macias Sabas 
print("Hola , mi nombre es Jazmin Macias Sabas")
```
linea 4 "print("Hola , mi nombre es Jazmin Macias Sabas")":
Esta línea utiliza la función "print" de Python, que se utiliza para imprimir texto en la pantalla. Dentro de los paréntesis, entre comillas, se encuentra el texto a imprimir, que en este caso es "Hola , mi nombre es Jazmin Macias Sabas". Cuando se ejecuta este programa, se mostrará este texto en la pantalla.

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
linea 4 nombre = input("Ingresa tu nombre:"):

Esta línea usa la función input(), que permite al programa recibir texto del usuario a través del teclado. El texto que aparece entre paréntesis y comillas ("Ingresa tu nombre:") es lo que verá el usuario como una especie de pregunta o instrucción. Cuando el usuario escribe su nombre y presiona "Enter", ese valor se almacena en la variable nombre.

linea 5 print("Hola, " + nombre):

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
4. *print(7)*:

   Esta línea utiliza la función print() de Python, que sirve para mostrar en la pantalla lo que se le indique. En este caso, se le indica que imprima el número entero 7, que representa el número de días de una semana.

5. *print("Triángulo")*:

   Aquí se vuelve a utilizar la función print(), esta vez para imprimir una cadena de texto, en este caso la palabra "Triángulo", que hace referencia a una figura de tres lados.

6. *print(0.25)*:

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
4. *print(1 + 2)*:

   Esta línea utiliza la función print() de Python para imprimir el resultado de la suma de los números 1 y 2. Al ejecutar este programa, se imprimirá el valor "3" en la pantalla.

5. *print(1 - 2)*:

   Aquí se vuelve a utilizar la función print(), esta vez para imprimir el resultado de la resta de los números 1 y 2. El resultado mostrado será "-1".

6. *print(1 * 2)*:

   Nuevamente se usa print() para imprimir el producto de los números 1 y 2, que es 2.

7. *print("concatenando cadenas" + "esta bien")*:

   En esta línea se utiliza la función print() para mostrar la concatenación de dos cadenas de texto: "concatenando cadenas" y "esta bien". El operador + se utiliza para unir las dos cadenas y se imprimirá "concatenando cadenasesta bien".

8. *print("no es posible" - "restar cadenas ")*:

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
4. *num_1 = int(input("ingresa el primero número:"))*:

   En esta línea se utiliza la función input() para pedir al usuario que ingrese el primer número. La función int() se utiliza para convertir el valor introducido en un número entero (sin decimales), y este valor se guarda en la variable num_1.

5. *num_2 = int(input("ingresa el segundo número:"))*:

   Aquí se pide al usuario que ingrese el segundo número, siguiendo el mismo procedimiento que para el primer número. Este valor se almacena en la variable num_2.

6. *suma = num_1 + num_2*:

   Esta línea calcula la suma de num_1 y num_2 y guarda el resultado en la variable suma.

7. *resta = num_1 - num_2*:

   Aquí se calcula la resta entre num_1 y num_2 y se guarda el resultado en la variable resta.

8. *division = num_1 / num_2*:

   Esta línea calcula la división de num_1 por num_2 y guarda el resultado en la variable division. Si num_2 es igual a cero, ocurrirá un error de ZeroDivisionError.

9. *multiplicación = num_1 * num_2*:

   Aquí se multiplican num_1 y num_2 y el resultado se guarda en la variable multiplicación.

10. *print("El valor de la suma es: " + str(suma))*:

   En esta línea, la función print() imprime el texto "El valor de la suma es: " concatenado con el valor de la variable suma. La función str() se utiliza para convertir el valor numérico de suma en una cadena de texto para poder concatenarlo.

11. *print("El valor de la resta es: " + str(resta))*:

   Aquí se imprime el texto "El valor de la resta es: " junto con el valor de la variable resta.

12. *print("El valor de la división es: " + str(división))*:

   Esta línea imprime el texto "El valor de la división es: " concatenado con el resultado de la variable división.

13. *print("El valor de la multiplicación es: " + str(multiplicación))*:
14. este muestra el resultado

15. ```
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
5. *base = float(input("ingrese el valor de la base:"))*:

   En esta línea se utiliza la función input() para solicitar al usuario que ingrese el valor de la base del triángulo. La función float() se utiliza para convertir el valor introducido en un número decimal, y este valor se guarda en la variable base.

6. *altura = float(input("ingrese el valor de la altura"))*:

   Aquí se pide al usuario que ingrese el valor de la altura del triángulo, siguiendo el mismo procedimiento que para la base. Este valor se almacena en la variable altura.

7. *área = base * altura / 2*:

   Esta línea calcula el área del triángulo, usando la fórmula base * altura / 2, y guarda el resultado en la variable área.

8. *print("el area del triangulo es:" + str(área))*:

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
5. *radio = float(input("ingresa el valor del radio:"))*:

   En esta línea se utiliza la función input() para solicitar al usuario que ingrese el valor del radio del círculo. La función float() se utiliza para convertir el valor introducido en un número decimal, y este valor se guarda en la variable radio.

6. **areacirculo = 3.1416 * radio ** 2**:

   Aquí se calcula el área del círculo, utilizando la fórmula 3.1416 * radio ** 2, y se guarda el resultado en la variable areacirculo.

7. *perimetrocirculo = 3.1416 * 2 * radio*:

   Esta línea calcula el perímetro del círculo, usando la fórmula 3.1416 * 2 * radio, y guarda el resultado en la variable perimetrocirculo.

8. *print("el valor del área es:" + str(areacirculo))*:

   En esta línea, la función print() imprime el texto "el valor del área es:" concatenado con el valor de la variable areacirculo. La función str() se utiliza para convertir el valor numérico de areacirculo en una cadena de texto para poder concatenarlo.

9. *print("el valor del perimetro es:" + str(perimetrocirculo))*:

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
4. *Días = float(input("Ingrese el número de días:"))*:

   En esta línea se utiliza la función input() para solicitar al usuario que ingrese el número de días. La función float() se utiliza para convertir el valor introducido en un número decimal, y este valor se guarda en la variable Días.

5. *Horas = Días * 24*:

   Aquí se calculan las horas equivalentes al número de días ingresado, utilizando la fórmula Días * 24, y se guarda el resultado en la variable Horas.

6. *Minutos = Horas * 60*:

   Esta línea calcula el número de minutos equivalentes al número de horas calculado anteriormente, utilizando la fórmula Horas * 60. El resultado se guarda en la variable Minutos.

7. *Meses = Días / 30*:

   Aquí se calcula el número de meses equivalentes al número de días ingresado, utilizando la fórmula Días / 30. Este resultado se guarda en la variable Meses.

8. *print("Días:" + str(Días))*:

   En esta línea, la función print() imprime el texto "Días:" concatenado con el valor de la variable Días. La función str() se utiliza para convertir el valor numérico de Días en una cadena de texto para poder concatenarlo.

9. *print("Horas::" + str(Horas))*:

   Aquí se imprime el texto "Horas::" junto con el valor de la variable Horas.

10. *print("Minutos::" + str(Minutos))*:

   En esta línea se imprime el texto "Minutos::" concatenado con el valor de la variable Minutos.

11. *print("Meses::" + str(Meses))*:

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
4. *num = 38*:

   En esta línea se crea una variable llamada num y se le asigna el valor entero 38.

5. *print(num)*:

   Aquí se imprime en pantalla el valor actual de la variable num, que en este caso es 38.

6. *num = num + 1*:

   En esta línea se actualiza el valor de la variable num. Se suma 1 al valor actual de num (38) y se guarda el resultado (39) en la misma variable num.

7. *print(num)*:

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
4. *print("Hola,\n\"Osvaldo\"")*:

   Aquí se imprime la cadena "Hola, \"Osvaldo\"" en pantalla. La secuencia de escape \n hace que se imprima el texto "Osvaldo" en una línea nueva. La barra invertida \ antes de las comillas dobles " hace que las comillas se interpreten como parte de la cadena y no como el fin de la cadena.

5. *print("Estoy feliz \u263A\t\u2615\t\u2650")*:

   Esta línea imprime la cadena "Estoy feliz" seguida de tres símbolos Unicode, una cara sonriente (\u263A), una taza de café (\u2615) y una cruz (\u2650). La secuencia de escape \t hace que haya una tabulación entre los símbolos Unicode.

6. *print("Alineado:\t\u263A")*:

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
4. *"print("-----Operador IGUAL (==)")"*:

   Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos del operador de igualdad (==).

5. *"print(5 == 5)   # True"*:

   Aquí se imprime el resultado de la comparación 5 == 5, que es True, ya que 5 es igual a 5.

6. *"print(10 == 7)  # False"*:

   Esta línea imprime el resultado de la comparación 10 == 7, que es False, ya que 10 no es igual a 7.

7. *"print(5.0 == 5) # True"*:

   Aquí se imprime el resultado de la comparación 5.0 == 5, que es True, ya que 5.0 es igual a 5.

8. *"print("\n-----Operador DIFERENTE o NO IGUAL (!=)")"*:

   Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos del operador de desigualdad (!=).

9. *"print(5 != 5)   # False"*:

   Aquí se imprime el resultado de la comparación 5 != 5, que es False, ya que 5 es igual a 5.

10. *"print(10 != 7)  # True"*:

   Esta línea imprime el resultado de la comparación 10 != 7, que es True, ya que 10 no es igual a 7.

11. *"print(5.0 != 5) # False"*:

   Aquí se imprime el resultado de la comparación 5.0 != 5, que es False, ya que 5.0 es igual a 5.

12. *"print("\n-----Operador MAYOR QUE (>)")"*:

   Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos del operador de mayor que (>).

13. *"print(10 > 5) # True"*:

   Aquí se imprime el resultado de la comparación 10 > 5, que es True, ya que 10 es mayor que 5.

14. *"print(5 > 10) # False"*:

   Esta línea imprime el resultado de la comparación 5 > 10, que es False, ya que 5 no es mayor que 10.

15. *"print("\nOperador MENOR QUE (<)")"*:

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
4. *"print("compuerta OR")"*:

   Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos de la compuerta lógica "OR".

5. *"print(False or False)"*:

   Aquí se imprime el resultado de la expresión False or False, que es False, ya que ambos valores son falsos.

6. *"print(False or True)"*:

   Esta línea imprime el resultado de la expresión False or True, que es True, ya que al menos uno de los valores es verdadero.

7. *"print(True or False)"*:

   Aquí se imprime el resultado de la expresión True or False, que es True, ya que al menos uno de los valores es verdadero.

8. *"print(True or True)"*:

   Esta línea imprime el resultado de la expresión True or True, que es True, ya que ambos valores son verdaderos.

9. *"print("compuerta AND")"*:

   Esta línea imprime una línea de separación y un título que indica que se mostrarán ejemplos de la compuerta lógica "AND".

10. *"print(False and False)"*:

   Aquí se imprime el resultado de la expresión False and False, que es False, ya que ambos valores son falsos.

11. *"print(False and True)"*:

   Esta línea imprime el resultado de la expresión False and True, que es False, ya que al menos uno de los valores es falso.

12. *"print(True and False)"*:

   Aquí se imprime el resultado de la expresión True and False, que es False, ya que al menos uno de los valores es falso.

13. *"print(True and True)"*:

   Esta línea imprime el resultado de la expresión True and True, que es True, ya que ambos valores son verdaderos.

Cuando se ejecuta este programa, se muestran los resultados de diferentes combinaciones de valores booleanos usando las compuertas lógicas "OR" y "AND".

