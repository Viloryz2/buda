print("¡Bienvenido a la Frutería Súper Mega Locura Incrible!")

precios = {"manzanas": 1700, "naranjazas": 2000, "frutillazas": 1200}
carritín = {"manzanas": 0, "naranjazas": 0, "frutillazas": 0}

while True:
    print("\n[1] Agregar manzanas\n[2] Agregar naranjazas\n[3] Agregar frutillazas\n[4] Cobrar y limpiar carritín\n[5] Salir volando")
    opcion = input("¿Qué quieres, campeón?: ")

    if opcion == "1":
        fruta = "manzanas"
    elif opcion == "2":
        fruta = "naranjazas"
    elif opcion == "3":
        fruta = "frutillazas"
    elif opcion == "4":
        total = sum(carritín[f] * precios[f] for f in carritín)
        print(f" Total a pagar: ${total} ")
        carritín = {k:0 for k in carritín}
        print("Carritín limpio, ¡gracias por darme tu dinero!")
        continue
    elif opcion == "5":
        print("¡Manñana vendre por mas!")
        break
    else:
        print("Eso no vale, pon una opción de la lista, raton.")
        continue

    while True:
        try:
            kg = float(input(f"¿Cuántos kilos de {fruta} quieres? (0.5 a 5): "))
            if 0.5 <= kg <= 5:
                carritín[fruta] += kg
                print(f"{kg} kg de {fruta} agregados al carritín.")
                break
            else:
                print("No seas rata, mínimo 0.5 y máximo 5 kilos, bro.")
        except:
            print("Eso no es un número, intenta otra vez.")
