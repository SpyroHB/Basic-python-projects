from ast import Await
from multiprocessing.connection import wait
from tkinter import N

# Printing a Simple Project Greeting!
Project_greeting="Hello World \nI'm New Project Created by:~~\nSpyroHB ~~ xD"
print(Project_greeting)
# Course fist Exercise
patient_name= 'John Smith'
patient_age=20
patient_exsiting = True, False 
print(patient_name,'\n',patient_age,'\n',patient_exsiting)
# Learning Basic  Input & Conversion {Strings and Int/float}
Q1_name= input('What is your name? ')
Q1_age= input('What is your Birth year? ')
age= 2022 - int(Q1_age)
Q1_weight_pounds= input('What is your Weight in Lbs: ')
Q1_weight_kilograms = float(Q1_weight_pounds) // 2.205
print('Name:', Q1_name, '\nAge:', age,'\nWeight in Kilograms:', Q1_weight_kilograms)