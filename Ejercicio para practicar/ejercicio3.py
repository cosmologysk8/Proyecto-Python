def reverse(word):
    word2 = word[::-1]
    print("{} al reves es {}".format(word, word2))

if __name__ == '__main__':
    palabra = str(input("escribe algo: "))
    reverse(palabra)