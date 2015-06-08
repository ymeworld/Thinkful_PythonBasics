#!/usr/bin/python3

"""/**
 ThinkFul Computer Information Systems
 @AUTHOR: Jocelyn M.
 Thinkful Spring 2015
 Programming in Python Basics 
 API Guessing a number game
 *****************************************************************************************
 Execution:  ./GuessNumber.py
 WHAT: This program promps the user to guss a number between 0 and 100 withing a 5 tries. 
 
 *****************************************************************************************/ """

import random

number = random.randint(0, 100)
tries  = 1

guess = int(input("Enter your guess: "))

while guess != number and tries < 5:
    if guess > number:
        print("Too High")
    else:
        print("Too Low")

    tries += 1
    guess = int(input("Enter your guess: "))

if guess != number:
    print("You lost, the number is: ", number)
else:
    print("You got it right!. The number was: ", number)
