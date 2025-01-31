#!/usr/bin/env python3
'''Lab3 Inv 2 function operate'''
#Author ID: salakoozi
'''
The purpose of the script is to have a single function that can perform:
addition, subtraction, or multiplication on a pair of numbers. 
But the function will allow us to choose exactly what operation 
we want to perform on the two numbers when we call it. 
If the operate function does NOT understand the operator given, 
it should return an error message (e.g. calling the function to 'divide' two numbers).
'''

def operate(number1, number2, operator):
    if operator == 'add':
        operate = number1 + number2

    elif operator == 'subtract':
        operate = number1 - number2

    elif operator == 'multiply':
        operate = number1 * number2

    elif operator == 'divide':
        operate = 'Error: function operator can be "add", "subtract", or "multiply"'

    return operate
    

    
if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))



