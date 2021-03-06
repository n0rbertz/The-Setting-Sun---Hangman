import random
import pyfiglet
import sys
import time
import os

exit1 = print(sys.exit)

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


print("Welcome {0}.\n".format(cap))
answer = 0
while answer != 1:
    menuset = input("Do you want to play? \n")
    no = pyfiglet.figlet_format("See you next time!")


    if menuset == "yes":
        print("\nAlright, let's play!")
        time.sleep(1)
        clear()
        answer += 1
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
        answer += 1
    else:
         print("Command is unavaliable, try again!\n")

easy = pyfiglet.figlet_format("Easy")
medium = pyfiglet.figlet_format("Medium")
hard = pyfiglet.figlet_format("Hard")

level = 0
while level != 1:
    levels = str(input("Please select a level (easy, medium, hard): "))
    if levels == "easy":
        print(easy)
        print("\nYour chose level is: {0}\n".format(levels))
        print("Introduction:")
        print("You have to guess the word.")
        print("Help: You will see a few letters from the guessing word.")
        level +=1
        time.sleep(3.2)
        #level +=1
    elif levels == "medium":
        print(medium)
        print("\nYour chose level is: {0}\n".format(levels))
        print("Introduction:\n")
        print("You have to guess the word.")
        print("Help: You will see a few letters from the guessing word")
        level +=1
        time.sleep(3.2)
        #level +=1
    elif levels == "hard":
        print(hard)
        print("\nYour chose level is: {0}\n".format(levels))
        print("Introduction:\n")
        print("You have to guess the word.")
        print("You won't see any letters from the guessing word.")
        level +=1
        time.sleep(3.2)
        #level +=1
    else:
       print("\nYou typed something wrong! Try again.")


clear()
goodluck = pyfiglet.figlet_format("Good Luck!\n")
print(goodluck)

f = open('countries-and-capitals.txt', 'r+')
words = f.read()
f.close()
print(words)

time.sleep(0.65)
#clear()

word = random.choice(words)
guesses = ""

#medium
index = random.choice(word)

if levels == "medium":
    for char in word:
        if char != index:
            word = word.replace(char, "_")
    print(word)

#easy
if levels == "easy":
    x = []
    index2 = random.choice(word)
    x.append(index2)
    index3 = random.choice(word)
    if index3 not in x:
        x.append(index3)
    else:
        while index3 in x:
            index3 = random.choice(word)
            if index3 not in x:
                x.append(index3)
    for char in word:
        if char not in x:
            word = word.replace(char, "_")
    print(word)


#alphabet: abcdefghijklmnopqrstuvwxyz .lower
#alp = "abcdefghijklmnopqrstuvwxyz"
#alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZ .upper

#value = "Tree 5"

# Uppercase the string.
#x = value.upper()
#print(x)

win = pyfiglet.figlet_format("You win!")

lives = 12
while lives > 0:
    print("\nLives: " + str(lives))
    failed = 0
    for char in word:
        if char in guesses:
            print(char + " ", end="")
        else:
            print("_ ", end="")
            failed += 1
    if failed == 0:
        print("\n"+win)
        print("\nThe word is:", word)
        break
    if lives == 11:
        print("\n _________________________")
    if lives == 10:
        print("\n\n               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("   ____________|____________")
    if lives == 9:
        print("\n\n    ___________ ")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("   ____________|____________")
    if lives == 8:
        print("\n\n    ___________ ")
        print("            \  |")
        print("             \ |")
        print("              \|")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("   ____________|____________")
    if lives == 7:
        print("\n\n    ___________ ")
        print("   |        \  |")
        print("   |         \ |")
        print("   |          \|")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("   ____________|____________")
    if lives == 6:
        print("\n\n    ___________ ")
        print("   |        \  |")
        print("   |         \ |")
        print("   |          \|")
        print("   O           |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("   ____________|____________")
    if lives == 5:
        print("\n\n    ___________ ")
        print("   |        \  |")
        print("   |         \ |")
        print("   |          \|")
        print("   O           |")
        print("   |           |")
        print("   |           |")
        print("               |")
        print("               |")
        print("   ____________|____________")
    if lives == 4:
        print("\n\n    ___________ ")
        print("   |        \  |")
        print("   |         \ |")
        print("   |          \|")
        print("   O           |")
        print("  /|           |")
        print(" / |           |")
        print("               |")
        print("               |")
        print("   ____________|____________")
    if lives == 3:
        print("\n\n    ___________ ")
        print("   |        \  |")
        print("   |         \ |")
        print("   |          \|")
        print("   O           |")
        print("  /|\          |")
        print(" / | \         |")
        print("               |")
        print("               |")
        print("   ____________|____________")
    if lives == 2:
        print("\n\n    ___________ ")
        print("   |        \  |")
        print("   |         \ |")
        print("   |          \|")
        print("   O           |")
        print("  /|\          |")
        print(" / | \         |")
        print("  /            |")
        print(" /             |")
        print("   ____________|____________")
    if lives == 1:
        print("\n\n    ___________ ")
        print("   |        \  |")
        print("   |         \ |")
        print("   |          \|")
        print("   O           |")
        print("  /|\          |")
        print(" / | \         |")
        print("  / \          |")
        print(" /   \         |")
        print("   ____________|____________")

    guess = input("\n\nGuess the character: ")
    if guess in guesses:
        print("You already used this letter")
    if guess not in word and guess not in guesses:
        lives -= 1 #-1
    if guess not in guesses:
        guesses += guess
    print("Guessed letters: " + guesses)
