"""
    Two Types of arguments used in argsparser
    1. Positional
    2. Optional
"""

# Creating a simple calculator using argparse feature
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("num1", help="Enter num1") # num1
parser.add_argument("num2", help="Enter num1") # num2
parser.add_argument("oper", help="Enter operation") # operation

args = parser.parse_args()

num1 = args.num1
num2 = args.num2
oper = args.oper
result = None

if oper == 'add' or oper == 'a':
    result = float(num1) + float(num2)
    print(f"The result of addition {num1} and {num2} is: {result}")
elif oper == 'subtract' or oper == 's':
    result = float(num1) - float(num2)
    print(f"The result of subtraction {num1} and {num2} is: {result}")
elif oper == 'multiply' or oper == 'm':
    result = float(num1) * float(num2)
    print(f"The result of multiplication {num1} and {num2} is: {result}")
elif oper == 'divide' or oper == 'd':
    if float(num2) != 0:
        result = float(num1) / float(num2)
        print(f"The result of division {num1} and {num2} is: {result}")
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"









