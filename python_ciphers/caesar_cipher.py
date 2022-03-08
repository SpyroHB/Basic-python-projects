from utils import encrypt, decrypter


def main():
    msg = "Type (1) to encrypt a text\nType (2) to decrypt a text\n>: "
    z = input(msg)
    if z == "1":
        s = input('type your text to encrypt here: ')
        i = int(input('Type your cipher key: '))
        print(encrypt(s,i))
    elif z == "2":
        s = input('type your text to decrypt here: ')
        i = int(input('Type your cipher key: '))
        print(decrypter(s,i))
    else:
        z= input(msg)


if __name__ == '__main__':
    main()