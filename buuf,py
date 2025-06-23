precios = {"manzanas": 1700, "naranjazas": 2000, "frutillazas": 1200}
carro = {"manzanas": 0, "naranjazas": 0, "frutillazas": 0}

while True:
    op = input("[1] Manzanas [2] Naranjazas [3] Frutillazas [4] Cobrar [5] Salir: ")
    if op in ["1", "2", "3"]:
        fruta = ["manzanas", "naranjazas", "frutillazas"][int(op)-1]
        try:
            kg = float(input("Kilos (0.5 a 5): "))
            if 0.5 <= kg <= 5:
                carro[fruta] += kg
                print(f"{kg} kg de {fruta} agregados.")
            else:
                print("Solo 0.5 a 5 kilos.")
        except:
            print("Pon un número.")
    elif op == "4":
        total = sum(carro[f]*precios[f] for f in carro)
        print(f"Total: ${total}")
        carro = {k:0 for k in carro}
    elif op == "5":
        print("Adiós!")
        break
    else:
        print("Opción no válida.")
