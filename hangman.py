import random #for the random order

name = input("Enter your name: ")
print("Good Luck", name+ "!")
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
# Function will choose one random
# word from this list of words
word = random.choice(words)
print("\nHangman Singeplayer\nGuess the word")
guesses = ""
# any number of turns can be used here
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
    guesses += guess
    if guess not in word: #Not in the list
        lives -= 1 #-1 
