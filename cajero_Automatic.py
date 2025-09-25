# Cajero automático 

#Menú con opciones para consultar saldo, retirar, depositar y salir.
#Si se retira, verificar que el salo sea suficiente.
#Si se deposita, sumar el monto al saldo.
#Mostrar el saldo actualizado después de cada operación.

saldo = 5000  # Saldo inicial

while True:
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Retirar")
    print("3. Depositar")
    print("4. Salir")

    opcion = input("Por favor elija una opción: ")

    if opcion == "1":
        print("Tu saldo es:", saldo)

    elif opcion == "2":
        retiro = float(input("Digite el monto que desea retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            print("Retiraste:", retiro, "| Saldo actual:", saldo)
        else:
            print("Saldo insuficiente")

    elif opcion == "3":
        deposito = float(input("Monto a depositar: "))
        saldo += deposito
        print("Depositaste:", deposito, "| Saldo actual:", saldo)

    elif opcion == "4":
        print("Gracias por usar el cajero, vuelva pronto. Adiós!")
        break

    else:
        print("Opción no válida")
