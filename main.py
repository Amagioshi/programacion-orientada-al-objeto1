from menu import menuprincipal
from agenda import agregar_contacto, buscar_contacto, listar_contactos

while True:
    menuprincipal()
    opcion = input("Selecciona una opcion: ").strip()
    if not opcion.isdigit():
        print("Por favor ingresa un numero valido.")
        continue
    opcion = int(opcion)
    if opcion == 1:
        nombre = input("Ingresa el nombre: ").strip()
        if not nombre.isalpha():
            print(f"El nombre '{nombre}', no es valido. Debe contener solo letras.")
            input()# Pausa para que el usuario vea el mensaje
            continue    
        telefono = input("Ingresa el telefono: ").strip()
        if not telefono.isdigit():
            print("El telefono debe contener solo digitos.")
            input()# Pausa para que el usuario vea el mensaje
            continue
        agregar_contacto(nombre, telefono)
        print("Contacto agregado")
    elif opcion == 2:
        nombre = input("Ingresa el nombre a buscar: ").strip()
        resultado = buscar_contacto(nombre)
        if resultado:
            print(f"Contacto encontrado: Nombre: {resultado['nombre']}, Telefono: {resultado['telefono']}")
        else:
            print(f"El contacto con nombre '{nombre}' no fue encontrado.")

    elif opcion == 3:
        listar_contactos()
        input("Presiona Enter para continuar...")
            
    elif opcion == 4:
        input
        print("Saliendo de la agenda...")
        break
    else:
        print("Opcion no valida, por favor intenta de nuevo.")
