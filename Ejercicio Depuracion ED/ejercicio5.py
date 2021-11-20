a = ((1, 2, 3),
     (3, 2, 1))
b = ((1, 2),
     (3, 4),
     (5, 6))

def producto(a, b):
    producto = []
    for i in range(len(a)):
        fila = [] 
        for j in range(len(b[0])):
            suma = 0
            for k in range(len(a[0])):
                suma += a[i][k] * b[k][j]
            fila.append(suma)
        producto.append(tuple(fila))
    return tuple(producto)

print(producto(a, b))

# Hay que cambiar el orden de los bucles for, primero buscamos el bucle a y luego indexamos para hacer otro bucle en la lista b
# también hay que quitar el + 1 del último bucle ya que no hace nada, y por último hay que añadir a la lista fila la suma con un append
# así mismo también hay que añadir al productor la lista fila con otro append y listo.