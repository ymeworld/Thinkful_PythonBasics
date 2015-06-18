#!/usr/bin/python3
"""/**
 ThinkFul Computer Information Systems
 @AUTHOR: Jocelyn M.
 Thinkful Spring 2015
 Introduction to Programming in Python 
 API building a Fizz buzz game.
 *****************************************************************************************
 Compilation:  ./FizzBuzz.py
 Execution:    ./FizzBuzz.py
 Purpose: This version of the program is where the user supply a value number at the command
 line at the time the scrip runs, it will use that value to print the FizzBuzz game to the
 console. Otherwise, it will promp the user to enter a value. Print "Fizz buzz counting up 
 to n".Print out each number from 1 to n, replacing with Fizzes and Buzzes as appropriate.
 Print the digits rather than the text representation of the number
 *****************************************************************************************/ """
 
n = 100
print("Fizz buzz counting up to {}".format(n))
for x in range(1,n+1):
    if x % 5 == 0 and x % 3 == 0:
        #newlist.append('fizzbuzz')
        print("FizzBuzz")
    elif x % 3 == 0:
        #newlist.append('fizz')
        print("Fizz")
    elif x % 5 == 0:
        #newlist.append('buzz')
        print("Buzz")
    else:
        #newlist.append(x)
        print(x)
