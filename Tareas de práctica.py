#Tarea 1: Encontrar el eror
nombre = input("¿Cuál es tu nombre?")
edad = int(input("¿Cuántos años tienes?"))
edad_el_proximo_ano = edad + 1
print("Hola, ", nombre, "¡en un año tendrás ", edad_el_proximo_ano, " años!")

#Tarea 2: Cantidad de vocales en una palabra
word = input("Ingresa una palabra:")
vowels = ["a", "e", "i", "o", "u"]
count = 0
for letter in word:
    if letter in vowels:
        count += 1
print("Número de vocales:", count)

#Tarea 3: Adivina el valor de x
x = 5
x = x + 2
x *= 3
print(x)
