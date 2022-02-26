def caesar_cipher(word=str, key=int):
    try:
      s = word.split(" ")
      a = ""
      for ch in s:
            for x in ch:
                r_ch = ord(x) - key
                a += chr(r_ch)
      print(f'''Cipher:{a}
key: 13''')
    except ValueError:
          print('Value Error:Try to use small sentences')
