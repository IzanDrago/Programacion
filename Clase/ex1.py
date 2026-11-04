ImportIn = float(input("Ingrese el importe inicial: "))
Propina = float(input("Ingrese % de la propina: "))
Importepropina = ImportIn * (Propina / 100)
Total = ImportIn + Importepropina

print("Importe inicial:", ImportIn,"€")
print("Propina (", Propina, "%):", Importepropina,"€")
print("-------------------")
print("Total a pagar:", Total,"€")