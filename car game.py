


from codecs import replace_errors





command = ""
started = False
while True:
     command= input('> ').lower()
     if command == "start":
         if  started:
             print('Car already started ! ')
         else: 
             started = True   
             print('Car started ....')

     elif command == "stop":
         if not started:
             print('Car is already stopped!')
         else:
             started=False
             print('car stopped')
     elif command == 'help':
        print('''
start - to make the car go 
stop  - to make the car stop
quit  - to exit.        
        ''') 
     elif command == "quit":
        break
     else:
        print("I dont understand your word\ntry help instead!")            
