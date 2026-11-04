raza = input("Es vosté Interiá (I) o Stringeriá (S)?: ")

if raza == "S":
    dia = input("Introdueix un dia de la setmana: ")
    if dia == "Dilluns":
        print("Día de la setmana:", dia)
        print("Traducció: 1")
    elif dia == "Dimarts":
        print("Día de la setmana:", dia)
        print("Traducció: 2")
    elif dia == "Dimecres":
        print("Día de la setmana:", dia)
        print("Traducció: 3")
    elif dia == "Dijous":
        print("Día de la setmana:", dia)
        print("Traducció: 4")
    elif dia == "Divendres":
        print("Día de la setmana:", dia)
        print("Traducció: 5")
    elif dia == "Dissabte":
        print("Día de la setmana:", dia)
        print("Traducció: 6")
    elif dia == "Diumenge":
        print("Día de la setmana:", dia)
        print("Traducció: 7")
    else:
        print("Dia no vàlid")

elif raza == "I":
    dia_num = int(input("Introdueix un dia de la setmana (1-7): "))
    if dia_num == 1:
        print("Día de la setmana:", dia_num)
        print("Traducció: Dilluns")
    elif dia_num == 2:
        print("Día de la setmana:", dia_num)
        print("Traducció: Dimarts")
    elif dia_num == 3:
        print("Día de la setmana:", dia_num)
        print("Traducció: Dimecres")
    elif dia_num == 4:
        print("Día de la setmana:", dia_num)
        print("Traducció: Dijous")
    elif dia_num == 5:
        print("Día de la setmana:", dia_num)
        print("Traducció: Divendres")
    elif dia_num == 6:
        print("Día de la setmana:", dia_num)
        print("Traducció: Dissabte")
    elif dia_num == 7:
        print("Día de la setmana:", dia_num)
        print("Traducció: Diumenge")
    else:
        print("Número de dia no vàlid")
else:
    print("Opció no vàlida")