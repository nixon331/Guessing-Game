'''
Created on 27 Feb 2017

@author: James.Nixon
'''
import random

number = random.randint(1,9)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("What's your guess?")
    if guess == "exit":
        break
    
    guess = int(guess)
    count += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        print("And it only took you",count,"tries!")