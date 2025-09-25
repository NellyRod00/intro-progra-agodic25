#Menú de una tienda para calcular totales con IVA, descuentos y precios unitarios.
#Opciones:
# 1. Total con IVA: Total = Precio × Cantidad × (1 + IVA =0.16)
# 2. Total con descuento + IVA: Total = Precio × Cantidad × (1 - Descuento) × (1 + IVA)
# 3. Precio unitario: Precio unitario = Total ÷ Cantidad
# 4. Salir

IVA = 0.16  
#Diccionario de cupones y sus descuentos
CUPONES = {"VERANO": 0.10, "SALDOS": 0.35, "BBVA": 0.05, "BANORTE25": 0.25}

while True:
    print("\n--- Mi Tienda Nelly ---")
    print("1. Total con IVA")
    print("2. Total con descuento + IVA")
    print("3. Precio unitario")
    print("4. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        precio = float(input("Ingresa el precio del producto: "))
        cantidad = int(input("Ingresa la cantidad: "))
        subtotal = precio * cantidad
        total = subtotal * (1 + IVA)
        print(f"Total: ${total:.2f}")

    elif opcion == "2":
        precio = float(input("Ingresa el precio del producto: "))
        cantidad = int(input("Ingresa la cantidad: "))
        cupon = input("Cupón (VERANO, SALDOS, BBVA, BANORTE25): ").upper()
        descuento = CUPONES.get(cupon, 0)
        subtotal = precio * cantidad * (1 - descuento)
        total = subtotal * (1 + IVA)
        print(f"Total con descuento: ${total:.2f}")

    elif opcion == "3":
        total = float(input("Total: "))
        cantidad = int(input("Cantidad: "))
        if cantidad == 0:
            print("Cantidad no puede ser 0")
        else:
            print(f"Precio unitario: ${total / cantidad:.2f}")

    elif opcion == "4":
        print("¡Gracias por usar el cotizador de Nelly, Vuelva pronto!")
        break

    else:
        print("Opción inválida")
