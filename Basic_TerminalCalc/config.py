msg = "multiplication (*)\naddition (+)\nsubtraction (-)\nexponent (**)\ndivision (/)\ntype 'quit' to exit\n:>  "


class CalcuOptions:
    def __init__(self) -> None:
        pass
        

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
