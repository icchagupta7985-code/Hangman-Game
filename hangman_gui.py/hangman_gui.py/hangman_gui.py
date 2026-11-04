import tkinter as tk
from tkinter import messagebox
import random

# Word list
WORDS = [
    "PYTHON", "LAPTOP", "KEYBOARD", "PROGRAM",
    "COMPUTER", "DEVELOPER", "SOFTWARE",
    "INTERNET", "DATABASE", "HANGMAN"
]

MAX_ATTEMPTS = 6

# Main window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("900x750")
root.resizable(True, True)
root.minsize(750, 650)
root.configure(bg="#151526")

# Game variables
secret_word = ""
guessed_letters = set()
wrong_guesses = 0
game_over = False

BG = "#151526"
CARD = "#22223A"
PURPLE = "#9B8CFF"
WHITE = "#FFFFFF"
GREEN = "#35D39A"
RED = "#FF657A"


def draw_hangman():
    canvas.delete("all")

    # Gallows
    canvas.create_line(40, 230, 180, 230, fill=WHITE, width=5)
    canvas.create_line(75, 230, 75, 25, fill=WHITE, width=5)
    canvas.create_line(75, 25, 155, 25, fill=WHITE, width=5)
    canvas.create_line(155, 25, 155, 55, fill=WHITE, width=5)

    # Body parts according to wrong guesses
    if wrong_guesses >= 1:
        canvas.create_oval(
            130, 55, 180, 105,
            outline=RED, width=4
        )

    if wrong_guesses >= 2:
        canvas.create_line(
            155, 105, 155, 165,
            fill=RED, width=4
        )

    if wrong_guesses >= 3:
        canvas.create_line(
            155, 120, 120, 145,
            fill=RED, width=4
        )

    if wrong_guesses >= 4:
        canvas.create_line(
            155, 120, 190, 145,
            fill=RED, width=4
        )

    if wrong_guesses >= 5:
        canvas.create_line(
            155, 165, 125, 205,
            fill=RED, width=4
        )

    if wrong_guesses >= 6:
        canvas.create_line(
            155, 165, 185, 205,
            fill=RED, width=4
        )


def update_word():
    display = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    word_label.config(text=display)

    if all(letter in guessed_letters for letter in secret_word):
        end_game(True)


def update_attempts():
    attempts_label.config(
        text=f"Incorrect guesses: {wrong_guesses}/{MAX_ATTEMPTS}"
    )


def guess_letter(letter):
    global wrong_guesses

    if game_over or letter in guessed_letters:
        return

    guessed_letters.add(letter)

    # Update selected button
    buttons[letter].config(
        state="disabled",
        bg="#44445C"
    )

    if letter in secret_word:
        buttons[letter].config(bg="#176B50")
        update_word()
    else:
        buttons[letter].config(bg="#713444")
        wrong_guesses += 1
        draw_hangman()
        update_attempts()

        if wrong_guesses >= MAX_ATTEMPTS:
            end_game(False)


def end_game(won):
    global game_over
    game_over = True

    for button in buttons.values():
        button.config(state="disabled")

    if won:
        status_label.config(
            text="YOU WON! 🎉",
            fg=GREEN
        )
        messagebox.showinfo(
            "Congratulations!",
            f"You guessed the word: {secret_word}"
        )
    else:
        status_label.config(
            text="GAME OVER!",
            fg=RED
        )
        messagebox.showinfo(
            "Game Over",
            f"The correct word was: {secret_word}"
        )


def new_game():
    global secret_word, guessed_letters
    global wrong_guesses, game_over

    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    game_over = False

    status_label.config(
        text="Guess the hidden word!",
        fg=PURPLE
    )

    update_word()
    update_attempts()
    draw_hangman()

    for letter, button in buttons.items():
        button.config(
            state="normal",
            bg="#383852"
        )


# Heading
title = tk.Label(
    root,
    text="HANGMAN GAME",
    font=("Arial", 27, "bold"),
    bg=BG,
    fg=PURPLE
)
title.pack(pady=(20, 5))

subtitle = tk.Label(
    root,
    text="Guess the word before the hangman is complete!",
    font=("Arial", 11),
    bg=BG,
    fg="#B8B8CC"
)
subtitle.pack(pady=5)

# Main game card
main_frame = tk.Frame(root, bg=CARD, padx=20, pady=15)
main_frame.pack(padx=30, pady=15, fill="both", expand=True)

# Drawing area
canvas = tk.Canvas(
    main_frame,
    width=230,
    height=245,
    bg=CARD,
    highlightthickness=0
)
canvas.pack(pady=5)

# Word display
word_label = tk.Label(
    main_frame,
    text="",
    font=("Courier", 25, "bold"),
    bg=CARD,
    fg=WHITE
)
word_label.pack(pady=10)

# Attempts
attempts_label = tk.Label(
    main_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg=CARD,
    fg=RED
)
attempts_label.pack(pady=5)

# Status
status_label = tk.Label(
    main_frame,
    text="Guess the hidden word!",
    font=("Arial", 13, "bold"),
    bg=CARD,
    fg=PURPLE
)
status_label.pack(pady=5)

# Keyboard
keyboard_frame = tk.Frame(main_frame, bg=CARD)
keyboard_frame.pack(pady=12)

buttons = {}

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for index, letter in enumerate(letters):
    row = index // 9
    col = index % 9

    button = tk.Button(
        keyboard_frame,
        text=letter,
        font=("Arial", 11, "bold"),
        width=4,
        height=1,
        bg="#383852",
        fg=WHITE,
        activebackground=PURPLE,
        activeforeground=WHITE,
        relief="flat",
        command=lambda l=letter: guess_letter(l)
    )

    button.grid(
        row=row,
        column=col,
        padx=3,
        pady=4
    )

    buttons[letter] = button

# New game button
restart_button = tk.Button(
    main_frame,
    text="↻  NEW GAME",
    font=("Arial", 12, "bold"),
    bg=PURPLE,
    fg="#151526",
    activebackground="#B5A9FF",
    relief="flat",
    padx=25,
    pady=9,
    command=new_game
)
restart_button.pack(pady=10)

# Start game
new_game()

# Run application
root.mainloop()