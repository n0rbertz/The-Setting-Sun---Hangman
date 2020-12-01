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


levels = input("Please select a level (easy, normal, hard): ")
 #   if levels == "easy": #pár betű a szóból

  #  elif levels == "normal":
    
    elif levels == "hard":

  # else:
   # print("You typed something wrong! Try again.")

print("Your chose level is: {0}.\n".format(levels))

goodluck = pyfiglet.figlet_format("Good Luck!\n")
print(goodluck)

time.sleep(1)
clear()

words = open("countries-and-capitals.txt","r")  #import txt file

word = random.choice(words)
guesses = ""
#life = pyfiglet.figlet_format("Lives: ")

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
    print("Guessed letters: " + guesses +",")
