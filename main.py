
edad = int(input("¿Que edad tienes?: "))

cantidad_ingresos = float(input("¿Que cantidad de dinero ganas al mes?: "))

def averiguar_tributar():
    if edad >= 16 and cantidad_ingresos >= 1000:
        print('Tienes que tributar')
    else:
        print('No tienes que tributar')

averiguar_tributar()

variable2 = "Voy a comprar {} panes"
cantidad = int(input("Ingrese cantidad de panes: "))

print(variable2.format(cantidad))
