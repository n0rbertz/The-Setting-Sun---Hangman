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
        lives -= 1  # -1
    if guess not in guesses:
        guesses += guess
    print("Guessed letters: " + guesses)



