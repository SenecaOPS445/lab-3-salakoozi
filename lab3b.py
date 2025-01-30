#!/usr/bin/env python3
'''Lab 3 Part 1 - functions'''
# Author ID: salakoozi

def sum_numbers(number1, number2):
    sum_numbers = number1 + number2
    return sum_numbers
#print(sum_numbers(1, 1))

def subtract_numbers(number1, number2):
    subtract_numbers = number1 - number2
    return subtract_numbers
#print(subtract_numbers(1, 1))

def multiply_numbers(number1, number2):
    multiply_numbers = number1 * number2
    return multiply_numbers
#print(multiply_numbers(5, 5))


if __name__ == '__main__': #Note: Sohail, you can see: https://teamtreehouse.com/community/why-do-i-have-to-write-if-name-main-print#:~:text=The%20if%20__name__,a%20module%20into%20other%20programs.
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))
    