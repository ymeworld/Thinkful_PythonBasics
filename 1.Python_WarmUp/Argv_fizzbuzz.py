#!/usr/bin/python3
"""/**
 ThinkFul Computer Information Systems
 @AUTHOR: Jocelyn M.
 Thinkful Spring 2015
 Introduction to Programming in Python 
 API building a Fizz buzz game.
 *****************************************************************************************
 Compilation:  ./Argv_fizzbuzz.py
 Execution:    ./Argv_fizzbuzz.py 55
 Purpose: This version of the program is where the user supply a value number at the command
 line at the time the scrip runs, it will use that value to print the FizzBuzz game to the
 console. Otherwise, it will promp the user to enter a value. Print "Fizz buzz counting up 
 to n".Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
 Print the digits rather than the text representation of the number
 *****************************************************************************************/ """

import sys

number = ""
        
if len(sys.argv) > 1:
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Entered value is not a number...")

while type(number) != int:
    try:
        number = int(input("Please enter a number: "))
    except ValueError:
        print("Please enter a number...")

print("Fizz buzz counting up to {}".format(number))
for y in range(1, number + 1):
    if y % 5 == 0 and y % 3 == 0:
        print("FizzBuzz")
    elif y % 3 == 0:
        print("Fizz")
    elif y % 5 == 0:
        print("Buzz")
    else:
        print(y)
