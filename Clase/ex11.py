OPERAR = input("Introdueix operació a realitzar (+,-,*,/):")
NumA = float(input("Introudeix el primer nº:"))
NumB = float(input("Introudeix el segon nº:"))

if OPERAR == "+":
    print(NumA," + ", NumB, "=", NumA + NumB)
if OPERAR == "-":
    print(NumA," - ", NumB, "=", NumA - NumB)
if OPERAR == "*":
    print(NumA," * ", NumB, "=", NumA * NumB)
if OPERAR == "/":
    print(NumA," / ", NumB, "=", NumA / NumB)