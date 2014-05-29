# -*- coding: utf-8 -*-
import  string

class enc:

    def __init__(self):
        pass

    def cesar(self, word, jump):
        abcd = string.ascii_lowercase
        encrypt_word = ""
        for char in word:
            if char != " ":
                try:
                    index = (abcd.index(char.lower()) + jump) % len(abcd)
                    encrypt_word = encrypt_word + abcd[index]
                except ValueError:
                    encrypt_word = encrypt_word + char
            else:
                encrypt_word = encrypt_word + char

        return encrypt_word


    def cenit_polar(self, frase):
        cenit = "cenit"
        polar = "polar"
        new_word = ""
        for i in range(len(frase)):
            if frase[i] in polar:
                new_word += str(cenit[polar.find(frase[i])])
            elif frase[i] in cenit:
                new_word += str(polar[cenit.find(frase[i])])
            else:
                new_word += (frase[i])
        return new_word


if __name__ == "__main__":
    e=enc()
    print e.cesar("hola")
    print e.cenit_polar("polar")

