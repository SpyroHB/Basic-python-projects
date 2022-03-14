def generate_random_password(passLength=int,):
    import string as s
    import random as r
    character = list(s.ascii_letters + s.digits + "+*/-().")
    password = []
    if passLength > 30:
        return 'Your password length must be smaller or equal to 30 characters!'
    else:
        r.shuffle(character)
        for i in range(passLength):
            password.append(r.choice(character))
            r.shuffle(password)
    return "".join(password)