# Hangman Game - Python Mini Project
# A simple text-based Hangman game for beginners.

import random

# Predefined list of 5 words
words = ["python", "laptop", "keyboard", "program", "computer"]

# Maximum number of incorrect guesses allowed
MAX_ATTEMPTS = 6

def play_game():
    """Plays one complete round of Hangman."""
    secret_word = random.choice(words)   # pick a random word
    guessed_letters = []                 # all letters tried so far
    wrong_guesses = 0                    # count of incorrect guesses

    print("\n==============================")
    print("   WELCOME TO HANGMAN GAME")
    print("==============================")
    print("The word has", len(secret_word), "letters.")
    print("You can make only", MAX_ATTEMPTS, "incorrect guesses.")

    while True:
        # Build the word display: correct letters shown, others hidden
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display = display + letter + " "
            else:
                display = display + "_ "

        print("\nWord:", display)
        print("Guessed letters:", guessed_letters)
        print("Remaining attempts:", MAX_ATTEMPTS - wrong_guesses)

        # Check win: no underscores left
        if "_" not in display:
            print("\nCongratulations! You won! The word was:", secret_word)
            break

        # Check loss: no attempts left
        if wrong_guesses == MAX_ATTEMPTS:
            print("\nGame Over! You lost. The correct word was:", secret_word)
            break

        # Take the player's guess
        guess = input("Guess a letter: ").lower()

        # Validate input: exactly one alphabet letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter (a-z).")
        # Prevent repeated guesses
        elif guess in guessed_letters:
            print("You already guessed '" + guess + "'. Try a different letter.")
        else:
            guessed_letters.append(guess)
            if guess in secret_word:
                print("Good guess! '" + guess + "' is in the word.")
            else:
                wrong_guesses = wrong_guesses + 1
                print("Sorry, '" + guess + "' is not in the word.")
# Main program: keep playing until the user says no
while True:
    play_game()
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice != "yes" and choice != "y":
        print("Thanks for playing Hangman! Goodbye.")
        break