# agenda 
contacto = []

def agregar_contacto(nombre, telefono):
    contacto.append({'nombre': nombre, 'telefono': telefono})
    
    
nombre = input("Ingresa el nombre: ")
telefono = input("INgresa el telefono: ")
    
agregar_contacto(nombre, telefono)
ptint("Contacto agregado")