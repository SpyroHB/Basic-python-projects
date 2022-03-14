# Optional passwrod length

def generate_random_password(passLength=int):
    import string,random
    character = list(string.ascii_letters + string.digits + "+*/-().")
    password = []
    if passLength > 30:
        return 'Your password length must be smaller or equal to 30 characters!'
    else:
        random.shuffle(character)
        for i in range(passLength):
            password.append(random.choice(character))
            random.shuffle(password)
    return "".join(password)


