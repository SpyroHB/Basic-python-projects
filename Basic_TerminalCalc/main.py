from config import addition , subtraction, division , multiplication , exponent

def double_space():
    print()
    print()


msg = "multiplication (*)\naddition (+)\nsubtraction (-)\nexponent (**)\ndivision (/)\ntype 'quit' to exit\n:>  "

z = input(msg).lower()
double_space()


while not z == 'quit':
    if z == '+':
        n1 = float(input('type first number: '))
        n2 = float(input('type second number: '))
        double_space()
        print(f'{n1} + {n2} = ',addition(n1,n2))
        double_space()
    elif z == '-':
        n1 = float(input('type first number: '))
        n2 = float(input('type second number: '))
        double_space()
        print(f'{n1} - {n2} = ',subtraction(n1,n2))
        double_space()
    elif z == '*':
        n1 = float(input('type first number: '))
        n2 = float(input('type second number: '))
        double_space()
        print(f'{n1} * {n2} = ',multiplication(n1,n2))
        double_space()
    elif z == '**':
        n1 = float(input('type first number: '))
        n2 = float(input('type second number: '))
        double_space()
        print(f'{n1} ** {n2} = ',exponent(n1,n2))
        double_space()
    elif z == '/':
        n1 = float(input('type first number: '))
        n2 = float(input('type second number: '))
        double_space()
        print(f'{n1} / {n2} = ',division(n1,n2))
        double_space()
    z = input(msg).lower()
