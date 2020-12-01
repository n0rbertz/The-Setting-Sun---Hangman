import random
import pyfiglet
import sys
import time
import os

banner = pyfiglet.figlet_format("Hangman")
print(banner)

name = input("Before we start, please type your name: ")
menu = input("Welcome {0}!\nDo you want to play? ".format(name))


if menu == "yes":
    print("Alright, let's play!")
elif menu == "no":
    print("See you next time!")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    sys.exit()
else:
    print("Command is unavaliable")

levels = input("Please select a level (easy, normal, hard, expert): ")


goodluck = pyfiglet.figlet_format("Good Luck!\n")
print(goodluck)


words = [
    "hangman",
    "computer",
    "science",
    "programming",
    "python",
    "television"
    "mathematics",
    "player",
    "telephone",
    "visual studio",
    "milk",
    "apple",
    "water",
    "tomato",
    "potato",
    "CodeCool"
]
word = random.choice(words)
guesses = ""
# any number of turns can be used here
lives = 12
while lives > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_ ", end="")
            failed += 1
    if failed == 0:
        print("\n\nYou Win!")
        print("\nThe word is:", word)
        break

    guess = input("\n\nGuess the character: ")
    guesses += guess
    if guess not in word: #Not in the list
        lives -= 1 #-1 