#Conversor de Unidades

#Fórmulas de conversión:
# 1. Celsius → Fahrenheit: F = (C × 9/5) + 32
# 2. Fahrenheit → Celsius: C = (F - 32) × 5/9
# 3. Metros → Centímetros: cm = m × 100
# 4. Centímetros → Metros: m = cm ÷ 100
# 5. Kilogramos → Gramos: g = kg × 1000
# 6. Gramos → Kilogramos: kg = g ÷ 1000



def menu():
    print("\n--- Conversor de Unidades ---")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Metros → Centímetros")
    print("4. Centímetros → Metros")
    print("5. Kilogramos → Gramos")
    print("6. Gramos → Kilogramos")
    print("7. Salir")

while True:
    menu()
    opcion = input("Por favor elige una opción: ")

    if opcion == "1":
        c = float(input("Ingresa temperatura en °C: "))
        f = (c * 9/5) + 32
        print(f"{c} °C = {f:.2f} °F")

    elif opcion == "2":
        f = float(input("Ingresa temperatura en °F: "))
        c = (f - 32) * 5/9
        print(f"{f} °F = {c:.2f} °C")

    elif opcion == "3":
        m = float(input("Ingresa longitud en m: "))
        cm = m * 100
        print(f"{m} m = {cm:.2f} cm")

    elif opcion == "4":
        cm = float(input("Ingresa longitud en cms: "))
        m = cm / 100
        print(f"{cm} cm = {m:.2f} m")

    elif opcion == "5":
        kg = float(input("Ingresa masa en Kg: "))
        g = kg * 1000
        print(f"{kg} kg = {g:.2f} g")

    elif opcion == "6":
        g = float(input("Ingresa masa en g: "))
        kg = g / 1000
        print(f"{g} g = {kg:.2f} kg")

    elif opcion == "7":
        print("Saliendo del conversor... ¡Nos Vemos Pronto!")
        break

    else:
        print("⚠ Opción no válida, intenta de nuevo.")
