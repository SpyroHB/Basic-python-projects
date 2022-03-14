# Using a simple coder/decoder with optional key "i"


def encrypt(sentence=str,key=int):
    s = sentence.split(" ")
    a = ""
    for ch in s:
        for x in ch:
            r_ch = ord(x) - key
            a += chr(r_ch) 
    return a


def decrypter(sentence=str,key=int):
    s = sentence.split(" ")
    a = ""
    for ch in s:
        for x in ch:
            r_ch = ord(x) + key
            a+=chr(r_ch) 
    return a
