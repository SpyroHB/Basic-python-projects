from ast import Await
from multiprocessing.connection import wait
from tkinter import N

# Printing a Simple Project Greeting!
Project_greeting="Hello World \nI'm New Project Created by:~~\nSpyroHB ~~ xD"
print(Project_greeting)
# Learning Basic  Input & Conversion {Strings and Int/float}
Q1_Fname= input('What is your first name? ')
Q1_Lname= input('What is your Last name? ')
Q1_age= input('What is your Birth year? ')
age= 2022 - int(Q1_age)
Q1_weight_pounds= input('What is your Weight in Lbs: ')
Q1_weight_kilograms = float(Q1_weight_pounds) // 2.205
msg= f'Full Name: {Q1_Fname} {Q1_Lname}.\nAge:{age} years old\nWeight in Kilograms:{Q1_weight_kilograms}'
print(msg)          
