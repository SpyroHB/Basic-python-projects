msg = "Type (1) to encrypt a text\nType (2) to decrypt a text: "


def encrypt(sentence):
    s = sentence.split(" ")
    a = ""
    for ch in s:
        for x in ch:
            r_ch = ord(x) - 28
            a += chr(r_ch) 
    print(a)
def decrypter(sentence):
    s = sentence.split(" ")
    a = ""
    for ch in s:
        for x in ch:
            r_ch = ord(x) + 28
            a+=chr(r_ch) 
    print(a)


def main():
    z = input(msg)
    if z == "1":
        s = input('type your text to encrypt here: ')
        encrypt(s)
    elif z == "2":
        s = input('type your text to decrypt here: ')
        decrypter(s)
    else:
        z= input(msg)
if __name__ == '__main__':
    main()