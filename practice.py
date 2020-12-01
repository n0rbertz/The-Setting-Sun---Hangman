import random
import pyfiglet
import sys
import time
import os

def clear(): os.system('clear')
reminder = pyfiglet.figlet_format("Friendly Reminder")
print(reminder+"\nIf you want to [Quit], just type exit.\n")
print("Loading")
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
clear()
banner = pyfiglet.figlet_format("Hangman")
print(banner)

name = input("Before we start, please type your name: ")
if not name:
        name = "player"
cap = name.capitalize()
clear()

menuset = input("Welcome {0}!\nDo you want to play? ".format(cap))
no = pyfiglet.figlet_format("See you next time!")

if menuset == "yes":
    print("Alright, let's play!")
    time.sleep(1)
    clear()
elif menuset == "no":
    clear()
    print(no) 
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    sys.exit()
else:
     print("Command is unavaliable")

easy = pyfiglet.figlet_format("Easy")
medium = pyfiglet.figlet_format("Medium")
hard = pyfiglet.figlet_format("Hard")


levels = str(input("Please select a level (easy, medium, hard): "))
if levels == "easy":
        print(easy)
        print("\nYour chose level is: {0}\n".format(levels))
        print("You will see a few letters from the guessing word.")
        time.sleep(3)
elif levels == "medium":
        print(medium)
        print("\nYour chose level is: {0}\n".format(levels))
        print("You will see a few letters from the guessing word")
        time.sleep(3)
elif levels == "hard":
        print(hard)
        print("\nYour chose level is: {0}\n".format(levels))
        print("You won't see any letters from the guessing word.")
        time.sleep(3)
else:
       print("\nYou typed something wrong! Try again.")


clear()
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

time.sleep(0.65)
clear()

#importing countries-and-capitals.txt somehow

word = random.choice(words)
guesses = ""

lives = 12
while lives > 0:
    print("Lives: " + str(lives))
    failed = 0
    for char in word:
        if char in guesses:
            print(char + " ", end="")
        else:
            print("_ ", end="")
            failed += 1
    if failed == 0:
        print("\n\nYou Win!")
        print("\nThe word is:", word)
        break

    guess = input("\n\nGuess the character: ")
    if guess in guesses:
        print("You already used this letter")
    if guess not in word and guess not in guesses:
        lives -= 1 #-1
    if guess not in guesses:
        guesses += guess
    print("Guessed letters: " + guesses)
