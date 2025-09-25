#Opciones del programa:
# 1. Promedio: (C1 + C2 + C3) ÷ 3
# 2. Calificación final con ponderaciones: (C1 × P1) + (C2 × P2) + (C3 × P3),donde P1 + P2 + P3 = 100%
# 3. Mayor y menor: se obtiene con max() y min()
# 4. Aprobar o reprobar: Aprueba si el promedio ≥ 6.
# En caso contrario reprueba.

while True:
    print("\n--- Gestor de Calificaciones ---")
    print("1. Promedio")
    print("2. Calificación final ponderada")
    print("3. Mayor y menor")
    print("4. Aprueba o reprueba")
    print("5. Salir")

    opcion = input("Elige opción: ")

    if opcion == "1":
        c1 = float(input("Parcial 1: "))
        c2 = float(input("Parcial 2: "))
        c3 = float(input("Parcial 3: "))
        print("Promedio:", (c1 + c2 + c3)/3)

    elif opcion == "2":
        c1 = float(input("Parcial 1: "))
        c2 = float(input("Parcial 2: "))
        c3 = float(input("Parcial 3: "))
        p1 = float(input("P1 (%): "))/100
        p2 = float(input("P2 (%): "))/100
        p3 = float(input("P3 (%): "))/100
        if abs(p1+p2+p3 - 1) > 0.001:
            print("⚠ Ponderaciones deben sumar 100%")
        else:
            print("Final ponderada:", c1*p1 + c2*p2 + c3*p3)

    elif opcion == "3":
        c1 = float(input("Parcial 1: "))
        c2 = float(input("Parcial 2: "))
        c3 = float(input("Parcial 3: "))
        print("Mayor:", max(c1,c2,c3))
        print("Menor:", min(c1,c2,c3))

    elif opcion == "4":
        c1 = float(input("Parcial 1: "))
        c2 = float(input("Parcial 2: "))
        c3 = float(input("Parcial 3: "))
        print("Aprueba" if (c1+c2+c3)/3 >=6 else "Reprueba")

    elif opcion == "5":
        print("Saliendo...¡¡Estudia más!!")
        break

    else:
        print("Opción no válida")