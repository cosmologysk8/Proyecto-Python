


def comp(numenor,numayor):
    if numenor < numayor:
        print("{} es mayor que {}".format(numayor, numenor))
    elif numenor > numayor:
        print("{} es mayor que {}".format(numenor, numayor))
    else:
        print("son el mismo numero")

if __name__ == '__main__':
    num1 = float(input("ingresa un numero: "))
    num2 = float(input("ingresa otro numero: "))
    comp(num1, num2)