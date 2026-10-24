while True:
    print("--- MENÚ ---")
    print("1. Encriptar")
    print("2. Desencriptar")
    opcion = input("Seleccione una opción (1 o 2): ").strip()

    if opcion in ["1", "2"]:
        break
    print("Error: Opción no válida. Debe ingresar 1 o 2.\n")

# 2. Validación del mensaje
while True:
    mensaje = input("Ingrese un mensaje: ").strip().upper()

    if not mensaje:
        print("Error: El mensaje no puede estar vacío.\n")
        continue

    if opcion == "1":  # Opción Encriptar
        if all(letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for letra in mensaje):
            break
        print("Error: Para encriptar, utiliza solo letras de la A a la Z (sin tildes, caracteres especiales ni espacios).\n")

    elif opcion == "2":  # Opción Desencriptar
        if all(caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345" for caracter in mensaje):
            break
        print("Error: Para desencriptar, utiliza solo letras (sin tildes ni espacios) y números del 1 al 5.\n")

# 3. Procesamiento según la opción seleccionada
if opcion == "1":
    secreto = (
        mensaje.replace("A", "1")
        .replace("E", "2")
        .replace("I", "3")
        .replace("O", "4")
        .replace("U", "5")
    )
    print("\n--- Resultado ---")
    print("Mensaje original:", mensaje)
    print("Mensaje encriptado:", secreto)

else:  # opcion == "2"
    original = (
        mensaje.replace("1", "A")
        .replace("2", "E")
        .replace("3", "I")
        .replace("4", "O")
        .replace("5", "U")
    )
    print("\n--- Resultado ---")
    print("Mensaje encriptado:", mensaje)
    print("Mensaje desencriptado:", original)