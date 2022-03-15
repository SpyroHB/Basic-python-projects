z = input('Welcome to guess game Type your guess:\n> ').lower() 

guess_words= ['car','house','python','java'] # any word but in lowercase

while True:

    if z in guess_words:

        print('You guess is correct!')
        
        print("If you want to Quit type 'exit'!")

        z = input('Play again?\nType your guess: ').lower()
    
    elif z == 'exit':
    
        print('Leaving ... \nThanks for playing!')
    
        break
    
    else:

        print('Your Guess is not correct Try again')
        z = input('Type your guess:\n> ').lower()
