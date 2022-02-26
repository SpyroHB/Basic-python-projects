def emoji_converter(msg):
    words = msg.split(' ')
    emojis = {
        "<3": "♥",
        ":)": "☺"
    }
    output= ''
    for word in words:
        output += emojis.get(word, word) + " "
    return output.capitalize()


msg = input('')
print(emoji_converter(msg))



