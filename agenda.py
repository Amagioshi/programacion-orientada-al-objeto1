# agenda 

contacto = []

def agregar_contacto(nombre, telefono):
    contacto.append({'nombre': nombre, 'telefono': telefono})


def buscar_contacto(nombre):
    for c in contacto:
        if c["nombre"].lower() == nombre.lower():
            return c
    return None
        
           

def listar_contactos():
    print("\n Lista de contactos:")
    for c in contacto:
        print(f"Nombre: {c['nombre']}, Telefono: {c['telefono']}")
        
listar_contactos()