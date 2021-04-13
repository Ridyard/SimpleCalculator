# small project - used to test git functionality for development
# simple calc script

## to do
# add additional calculations (floor division, power etc)
# add gui

import pyinputplus as ip

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def breakOut(i): # check if input is empty / user wants to end the script
    if i == '':
        raise Exception()
        
  

try:
    while True:
        x = ip.inputNum('\nenter number...\n', blank = True)
        breakOut(x)
        c = ip.inputChoice(['+', '-', '*', '/', ''], blank = True)
        breakOut(c)
        y = ip.inputNum('enter number...\n', blank = True)
        breakOut(y)

        if c == '+':
            result = add(x, y)
            print(result)

        elif c == '-':
            result = subtract(x, y)
            print(result)

        elif c == '*':
            result = multiply(x, y)
            print(result)

        elif c == '/':
            result = divide(x, y)
            print(result)

except:
    print('goodbye')
