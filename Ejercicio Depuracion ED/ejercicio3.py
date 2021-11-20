u = [1, 2, 3]
v = [4, 5, 6]

def producto_escalar(u, v):
    for i in range(len(u)):
        u[i] *= v[i]
    return sum(u)

print(producto_escalar(u, v))

#Hay que usar range y len para que recorra la lista u y se vaya multiplicando las dos listas  