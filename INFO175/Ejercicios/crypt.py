# -*- coding: utf-8 -*-

import string
class Enc():

    def __init__(self):
        self.word = str

    def cesar(word, jump=2):
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


    def cenit_polar(frase):
        cenit = "cenit"
        polar = "polar"
        new_word = ""
        for i in range(len(frase)):
            if frase[i] in polar:
                print cenit[polar.find(frase[i])],
            elif frase[i] in cenit:
                print polar[cenit.find(frase[i])],
            else:
                print frase[i],
        return new_word

e=Enc()
e.cesar("hola")
