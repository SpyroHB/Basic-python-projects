# Printing a Simple Project Greeting!
Project_greeting='''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


                I'm New Project Created 
                        by:
                   ~~ SpyroHB ~~ xD



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
date_err = 'Please use a valid date!'
# Learning Basic  Input & Conversion "Strings and Int/float".
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Inputing your User's first name.
U1_Fname= input('What is your first name? ')
# Inputing your User's second name.
U1_Lname= input('What is your Last name? ')
# Inputing your User's Birthday.
U1_date= input('What is your birthday?\ndd/mm/yyyy  ')
# Coversing a String with int and subtracting 
U1_day= U1_date[0:2]
U1_month= U1_date[2:4]
U1_year= U1_date[4:]
date= 2022 - int(U1_year)
# Inputing your User's weight 
U1_weight_pounds= input('What is your Weight in Lbs: ')
# Conversing a String with float/int by using integer dividing "1 kilogram = 2.205 kbs"
U1_weight_kilograms = float(U1_weight_pounds) // 2.205
# Formatted string so we orgnaize our output message
msg= f'''Full Name: {U1_Fname} {U1_Lname}.
date:{date} years old
Birthday: {U1_day}/{U1_month}/{U1_year}.
Weight in Kilograms:{U1_weight_kilograms}
'''
# Using a basic output "Terminal"
print(Project_greeting)
print(msg)
while True:
    x = input('>  ').lower()
    if x == 'info':
        print('Your Information')
    elif x == 'quit':
        print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~Exiting!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~Thanks For using out program~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
        break