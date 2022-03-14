# Basic Math operations for "Terminal Calculator"
class CalcuOptions:
    def __init__(self,num1,num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def exponent(num1,num2):
        return num1**num2


    def addition(num1,num2):
        return num1+num2


    def subtraction(num1,num2):
        return num1-num2


    def multiplication(num1,num2):
        return num1*num2


    def division(num1,num2):
        return num1/num2



def double_space():
    print()
    print()