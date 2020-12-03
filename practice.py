import random
import pyfiglet
import sys
import time
import os



loading = "Loading.."
dot = "..."
dot2 = "......"
no = pyfiglet.figlet_format("See you next time!")
def clear(): os.system('clear')
reminder = pyfiglet.figlet_format("Friendly Reminder")
print(reminder+"\nIf you would like to quit, just type exit.\n")
for i in loading:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.35)
clear()

banner = pyfiglet.figlet_format("Hangman")
print(banner)



name = input("Before we start, please type your name: ")
if not name:
        name = "player"
if name in ['exit','Exit']:
    print(no)
    time.sleep(0.4)
    sys.exit()
cap = name.capitalize()
clear()


print("Welcome {0}!\n".format(cap))
answer = 0
while answer != 1:
    menuset = input("Do you want to play?\n")
    if menuset in ['exit','Exit']:
        print(no)
        time.sleep(0.4)
        sys.exit()
    elif menuset == "yes":
        print("\nAlright, let's play!")
        time.sleep(0.7)
        clear()
        answer += 1
    elif menuset == "no":
        clear()
        print(no)
        time.sleep(1.5)
        for r in dot:
            sys.stdout.write(r)
            sys.stdout.flush()
            time.sleep(0.2)
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
    if levels in ['exit','Exit']:
        print(no)
        time.sleep(0.4)
        sys.exit()
    elif levels == "easy":
        clear()
        print(easy)
        print("Your chose level is: {0}\n".format(levels))
        print("Introduction:\n")
        print("You have to guess the word.")
        print("Help: You will get a few letters from the guessing word.")
        for i in dot2:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.9)
        level +=1
    elif levels == "medium":
        clear()
        print(medium)
        print("Your chose level is: {0}\n".format(levels))
        print("Introduction:\n")
        print("You have to guess the word.")
        print("Help: You will get a few letters from the guessing word")
        for i in dot2:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.9)
        level +=1
    elif levels == "hard":
        clear()
        print(hard)
        print("Your chose level is: {0}\n".format(levels))
        print("Introduction:\n")
        print("You have to guess the word.")
        print("You won't get any letters from the guessing word.")
        for i in dot2:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.9)
        level +=1
        #time.sleep(3.2)
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

time.sleep(0.5)
clear()

word = random.choice(words)
guessword = word
#medium
index = random.choice(word)

if levels == "medium":
    print("Hint: ")
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
    print("Hint: ")
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

guesses = ""
lives = 12
print("\nLives: "+ str(lives))
while lives > 0:
    failed = 0
    for char in guessword:
        if char in guesses:
            print(char + " ", end="")
        else:
            print("_ ", end="")
            failed += 1
    if failed == 0:
        print("\n"+win)
        print("\nThe word is:", guessword)
        break

    guess = input("\n\nGuess the character: ")
    if guess in ['exit','Exit']:
        print(no)
        time.sleep(0.4)
        sys.exit()
    if guess in guesses:
        print("You already used this letter.\n")
    if guess not in guessword and guess not in guesses:
        lives -= 1 #-1
    if guess not in guesses:
        guesses += guess
    #print("Guessed letters: " + guesses)
    if lives == 11:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses)
        print("\n\n\n\n\n\n\n")
        print("\n   ________________")
    if lives == 10:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses)
        print("\n               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("   ____________|___")
    if lives == 9:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses)
        print("       ____________  ")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("   ____________|___")
    if lives == 8:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses)
        print("       ____________  ")
        print("            \  |")
        print("             \ |")
        print("              \|")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("   ____________|___")
    if lives == 7:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses)
        print("      ____________  ")
        print("      |     \  |")
        print("      |      \ |")
        print("      |       \|")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("   ____________|___")
    if lives == 6:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses)
        print("      ____________    ")
        print("      |     \  |")
        print("      |      \ |")
        print("      |       \|")
        print("      O        |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("   ____________|___")
    if lives == 5:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses)
        print("      ____________ ")
        print("      |     \  |")
        print("      |      \ |")
        print("      |       \|")
        print("      O        |")
        print("      |        |")
        print("      |        |")
        print("               |")
        print("               |")
        print("   ____________|___")
    if lives == 4:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses)
        print("      ____________ ")
        print("      |     \  |")
        print("      |      \ |")
        print("      |       \|")
        print("      O        |")
        print("     /|        |")
        print("    / |        |")
        print("               |")
        print("               |")
        print("   ____________|___")
    if lives == 3:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses) 
        print("      ____________  ")
        print("      |     \  |")
        print("      |      \ |")
        print("      |       \|")
        print("      O        |")
        print("     /|\       |")
        print("    / | \      |")
        print("               |")
        print("               |")
        print("   ____________|___")
    if lives == 2:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses)
        print("      ____________   ")
        print("      |     \  |")
        print("      |      \ |")
        print("      |       \|")
        print("      O        |")
        print("     /|\       |")
        print("    / | \      |")
        print("     /         |")
        print("    /          |")
        print("   ____________|___")
    if lives == 1:
        clear()
        print("Lives: " + str(lives))
        print("Guessed letters: " + guesses)
        print("      ____________   ")
        print("      |     \  |")
        print("      |      \ |")
        print("      |       \|")
        print("      O        |")
        print("     /|\       |")
        print("    / | \      |")
        print("     / \       |")
        print("    /   \      |")
        print("   ____________|___")
    if lives == 0:
        print("The word was:",guessword)
