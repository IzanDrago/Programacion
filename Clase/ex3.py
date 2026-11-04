Vel = int(input("Ingrese la velocidad que ha volado el astronauta en km/h: "))
VeloNus = Vel/1.852
TVH = float(input("Ingrese el tiempo de vuelo en horas: "))
TVM = TVH*60

print("La nostra aeronau ha viatjat durant", TVM, "minuts a una velocitat de", VeloNus, "nusos, de manera que ha recorregut", Vel*TVH, "km")