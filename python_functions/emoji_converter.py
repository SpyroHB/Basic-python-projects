def emoji_converter(msg):
    words = msg.split(' ')
    emojis_disc = {
        "<3": "♥",
        ":)": "☺",
        ":(": "☺"
    }
    output= ''
    for word in words:
        output += emojis_disc.get(word, word) + " "
    return output.capitalize()
