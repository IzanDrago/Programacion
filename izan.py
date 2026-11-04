Alumnos = input("¿Cuál es tu nombre?: ")
print("Te llamas", Alumnos)
Edad = int(input("Dime tu edad: "))
print("Entonces, te llamas", Alumnos, "y te faltan", 99 - Edad, "años para llegar a 99 años.")
if Edad < 24:
    print("Te faltan almenos 75 años para llegar a 99 años.")
if Edad > 99:
    print("Ya has llegado a 99 años, deberías replantear tu vida.")
if Edad < 99 and Edad > 24:
    print("estás entre medio")

if Edad == 18 and Alumnos == "Izan":
    print("Hola creador Izan, tenga un buen día.")

lista = ["Carlos","Izan","Sara","Angela","Ruben","Jesus"]
if Alumnos in lista:
    print("Bienvenido a la lista,", Alumnos)
else:
    print("Excuse mua, tu no estás en la lista, muere.")