# Using a simple coder with a key of "28"
def encrypt(sentence=str,i=int):
    s = sentence.split(" ")
    a = ""
    for ch in s:
        for x in ch:
            r_ch = ord(x) - i
            a += chr(r_ch) 
    return a

# Using a simple decoder with a key of "28"
def decrypter(sentence=str,i=int):
    s = sentence.split(" ")
    a = ""
    for ch in s:
        for x in ch:
            r_ch = ord(x) + i
            a+=chr(r_ch) 
    return a
