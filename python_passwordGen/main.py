import string as s
import random as r

character = list(s.ascii_letters + s.digits + "!@#$%^&*()")

def generate_random_password():

    inval = int(input("Enter password length: "))

    password = []

    if not inval >= 6:
        print()
        print('Your password length must be alteast 6 characters!')
    
    elif not inval <= 30:
        print()
        print('Your password length must be smaller or equal to 30 characters!')
    
    else:

        r.shuffle(character)

        for i in range(inval):

            password.append(r.choice(character))

            r.shuffle(password)

    print("".join(password))


generate_random_password()