#!/usr/bin/python3
"""/**
 ThinkFul Computer Information Systems
 @AUTHOR: Jocelyn M.
 Thinkful Spring 2015
 Introduction to Programming in Python 
 API building a Fizz buzz game.
 *****************************************************************************************
 Compilation:  ./fizzbuzz.py
 Execution:    ./fizzbuzz.py
 Purpose: This version of the program is where the user supply a value number at the command
 line at the time the scrip runs, it will use that value to print the FizzBuzz game to the
 console. Otherwise, it will promp the user to enter a value. Print "Fizz buzz counting up 
 to n".Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
 Print the digits rather than the text representation of the number
 *****************************************************************************************/ """

for i in range(0,100):

    if i % 15 == 0:
        print("FizzBuzz")    

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
