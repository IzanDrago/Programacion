import random

mosca = 1
matamoscas = 2
humano = 3
puntos = 0

while True:
    opcion = int(input("Ingrese un número (1 para mosca, 2 para matamoscas, 3 para humano)(humano>matamoscas>mosca>humano): "))

    while opcion not in (1, 2, 3):
        print("No hay otra opción... 1, 2 o 3.")
        opcion = int(input("Ingrese un número (1 para mosca, 2 para matamoscas, 3 para humano): "))

    aleatorio = random.randint(1, 3)

    if opcion == mosca and aleatorio == humano:
        print("1? Tu rival sacó 3, así que le has echo huir a ese humano")
        puntos += 1
    elif opcion == matamoscas and aleatorio == mosca:
        print("Cuidado ese 2, que te cargas a la mosca, ah, has ganado?")
        puntos += 1
    elif opcion == humano and aleatorio == matamoscas:
        print("Que haces con ese matamoscas? Has ganado")
        puntos += 1
    elif opcion == aleatorio:
        print("Os habeis cruzado la mirada, habéis empatado")
        puntos += 0
    elif opcion == mosca and aleatorio == matamoscas:
        print("Estaba claro ese 2, esto está arreglado")
        puntos -= 1
    elif opcion == matamoscas and aleatorio == humano:
        print("No te dejes coger... Ah, que no tienes piernas")
        puntos -= 1
    elif opcion == humano and aleatorio == mosca:
        print("DIOS, tan inutil como siempre, te ha ganado una mosca")
        puntos -= 1

    respuesta = input("¿Quieres volver a jugar, o te vas a llorar? llevas {} puntos (si/no): ".format(puntos)).strip().lower()
    if respuesta == "no":
        print("Te has picado?")
        break

print("       .-.-.")
print("     .-     -.")
print("     |  o o  |")
print("     |   v   |")
print("      '-._.-'")
print("         | |")
print("         | |")
print("        .-. ")
print("       .   .")
print("El baile de la mosca, no te mosquees")
