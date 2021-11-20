listin = {'Juan':123456789, 'Pedro':987654321}

def elimina(listin, usuario):
    return listin.pop(usuario, '')

print(elimina(listin, 'Pablo'))

# Hay que usar la función pop que simplemente elimina y retorna un elemento que pongamos despues de la coma, pero en este caso como Pablo no está 
# indicado en la lista "listin" no hará nada , ya que no le está asignado ningún número de teléfono