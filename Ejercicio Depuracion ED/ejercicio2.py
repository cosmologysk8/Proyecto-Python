
base = int(input('Introduce la base imponible en la facutura: '))

def aplica_iva(base,iva = 21):
    
    base = base * iva
    return base

print(aplica_iva(base,iva = 21))

# No se puede usar un print llamando a la función antes de definir dicha función, además hay que indicar el valor de IVA cuando 
# se llama a la función y en el ejemplo no se llama. Por último hay que indicar que BASE es un número entero int()
# sino te ejecuta el dinero base la cantidad de veces que indiquemos en el IVA 