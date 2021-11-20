def comp(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    else:
        return False

if __name__ == '__main__':
    le = str(input("ingresa una letra: "))
    var = comp(le)
    if var == True:
        print("es vocal")
    else:
        print("no es vocal")