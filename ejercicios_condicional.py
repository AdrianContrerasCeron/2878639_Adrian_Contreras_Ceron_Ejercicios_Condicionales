#Miscelanea
# Condicionales

#Ejercicio 2.1
print("Ejercicio 2.1 - Escribir un algoritmo para saber si el número ingresado por teclado es positivo o negativo")
print("")

x = float(input("Escriba un número positivo o negativo: "))

if x > 0:
    print("El número es positivo.")
elif x == 0:
    print("El cero es un número neutral, no tiene valor positivo o negativo.")
else:
    print("El número es negativo.")

print("")
#Ejercicio 2.2
print("Ejercicio 2.2 - Escribir un algoritmo que reciba dos números por teclado y diga cuál es el mayor y cuál el menor.")
print("")

a = float(input("Escriba el primer número: "))
b = float(input("Escriba el segundo número: "))

if a > b:
    print(f"el número {a} es el numero mayor y el número {b} es el numero menor.")
elif a < b:
    print(f"el número {a} es el numero menor y el número {b} es el numero mayor.") 
    
print("")
#Ejercicio 2.3
print("Ejercicio 2.3 - Escriba un programa que lea tres números enteros positivos y que calcule e imprima en pantalla el menor y el mayor de ellos.")
print("")

a = int(input("Escriba el primer número: "))
b = int(input("Escriba el segundo número: "))
c = int(input("Escriba el tercer número: "))

#Este ejercicio lo resolví con permutaciones: 3! = 3*2*2 = 6. Es decir existen 6 combinaciones posibles de tres números enteros positivos cualquiera


if a > 0 and b > 0 and c > 0:
    if a < b and a < c and c > b and c > a:
        print(f"el número {a} es el numero menor y el número {c} es el número mayor.")
    elif a < c and a < b and b > c and b > a:
        print(f"el número {a} es el numero menor y el número {b} es el número mayor.")
    elif b < c and b < a and a > c and a > b:
        print(f"el número {b} es el numero menor y el número {a} es el número mayor.")
    elif c < b and c < a and a > b and a > c:
        print(f"el número {c} es el numero menor y el número {a} es el número mayor.")
    elif b < a and b < c and c > a and c > b:
        print(f"el número {b} es el numero menor y el número {c} es el número mayor.")
    elif c < a and c < b and b > a and b > c:
        print(f"el número {c} es el numero menor y el número {b} es el número mayor.")
else:
    print(f"Uno o todos los números ingresados no son enteros positivos")

print("")
#Ejercicio 2.4
print("Ejercicio 2.4 - Dados dos números A y B, sumarlos si A es menor que B o sino restarlos.")
print("")

a = float(input("Escriba el primer número: "))
b = float(input("Escriba el segundo número: "))

if a < b:
    suma = a + b
    print(f"La suma de los dos números es {suma}")
else:
    resta = a - b
    print(f"La resta de los dos números es {resta}")

print("")
#Ejercicio 2.5
print("Ejercicio 2.5 - Dados dos números A y B encontrar el cociente entre A y B. Recordar que la división por cero no está definida, en ese caso debe aparecer una leyenda anunciando que la división no es posible..")
print("")

a = float(input("Escriba el primer número: "))
b = float(input("Escriba el segundo número: "))

if b == 0:
    print(f"La división no es posible, por cuanto la división por cero no está definida.")
else:
    division = a / b
    print(f"El cociente entre los dos números es {division}")

print("")
#Ejercicio 2.6
print("Ejercicio 2.6 - Dados dos números A y B, sumarlos si al menos uno de ellos es negativo, en caso contrario multiplicarlos.")
print("")

a = float(input("Escriba el primer número: "))
b = float(input("Escriba el segundo número: "))

if a < 0 or b < 0:
    suma = a + b
    print(f"La suma de los dos números es {suma}")
else:
    multiplicacion = a * b
    print(f"El producto de los dos números es {multiplicacion}")

print("")
#Ejercicio 2.7
print("Ejercicio 2.7 - Escribir un algoritmo que determine si un año es bisiesto o no.")
print("")

año = int(input("Escriba el año que dese saber si es bisiesto: "))

if año % 4 == 0:
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")
