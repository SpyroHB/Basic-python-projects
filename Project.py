from ast import Await
from multiprocessing.connection import wait
from tkinter import N
import math 
# Printing a Simple Project Greeting!

Project_greeting='''Hello World! 
I'm New Project Created 
by:
~~ SpyroHB ~~ xD'''

# Learning Basic  Input & Conversion "Strings and Int/float".
# Inputing your User's first name.
U1_Fname= input('What is your first name? ')
# Inputing your User's second name.
U1_Lname= input('What is your Last name? ')
# Inputing your User's Age.
U1_age= input('What is your Birth year? ')
# Coversing a String with int and subtracting 
age= 2022 - int(U1_age)
# Inputing your User's weight 
U1_weight_pounds= input('What is your Weight in Lbs: ')
# Conversing a String with float/int by using integer dividing "1 kilogram = 2.205 kbs"
U1_weight_kilograms = float(Q1_weight_pounds) // 2.205
# Formatted string so we orgnaize our output message
msg= f'''Full Name: {U1_fname} {U1_Lname}.
Age:{age} years old
Weight in Kilograms:{U1_weight_kilograms}
'''
# Using a basic output "Terminal"
print(Project_greeting)
print(msg)   
