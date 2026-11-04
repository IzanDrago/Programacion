horas = float(input("Cuantas horas has estado en la bici?:"))
agua = 0.5*horas
bebida = int(agua)
print("temps = ",horas," ----> litres = ", bebida)
if agua == 1:
    print("com has estat ",horas," fent exercici, has de beure ",bebida," litre de líquid per mantenir-te en un bon nivell d'hidratació")
if agua != 1:
    print("com has estat ",horas," fent exercici, has de beure ",bebida," litres de líquid per mantenir-te en un bon nivell d'hidratació")