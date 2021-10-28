Nombre_Telefono = []
while True:
    nombre = input("Nombre:")
    if nombre == "fin":
        break
    Telefono = input("Telefono:")
    linea = {}
    linea["Nombre"] = nombre
    linea["Telefono"] = Telefono
    Nombre_Telefono.append(linea)

