# agenda 
contacto = []

def agregar_contacto(nombre, telefono):
    contacto.append({'nombre': nombre, 'telefono': telefono})
nombre = input("Ingresa el nombre: ")
telefono = input("INgresa el telefono: ")

agregar_contacto(nombre, telefono)
print("Contacto agregado")

def buscar_contacto(nombre):
    for c in contactos:
        if c["nombre"].lower() == nombre.lower():
            print(f"Contacto encontrado: Nombre: {c['nombre']}, Telefono: {c['telefono']}")

def listar_contactos():
    print("\n Lista de contactos:")
    for c in contactos:
        print(f"Nombre: {c['nombre']}, Telefono: {c['telefono']}")
        
listar_contactos()