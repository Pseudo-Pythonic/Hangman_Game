import random

name = input("What is your name?\n>>> ")
print(f"Hello {name.title()} ! Welcome to the game of Hangman!")
print("Guess the characters below !")

words = ["apple",
         "python",
         "human",
         "words",
         "red",
         "bat",
         "aeroplane",
         "railway",
         "train",
         "pious"
         "million",
         "java"
]

word = random.choice(words)
turns = 12
guesses = " "

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win!")
        break

    guess = input("Enter your guess: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong Choice!")
        print(f"You have {turns} turns left!")

    if turns == 0:
        print("You lose!")
        print(f"The actual word was {word}")

