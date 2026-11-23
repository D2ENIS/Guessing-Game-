# Python Number Guessing Game

A command-line guessing game where the computer generates a secret number between 1 and 50 and guides the player with high/low hints.

## Features
- **Random Number Generation:** Picks a new secret number every round using Python's `random` module.
- **Interactive Hints:** Tells the player whether each guess is too high or too low.
- **Attempt Counter:** Tracks how many guesses it takes to win.
- **Colored Terminal Output:** Highlights hints and victory messages in the terminal.

## How to Run
Make sure Python 3 is installed on your computer, then run:
```bash
python guessing_game.py
```

## What I Learned
- Generating random numbers with `random.randint()`
- Converting user input from text to integers with `int()`
- Repeating game turns with `while` loops and `break`
- Handling multiple conditions with `if / elif / else` and f-strings
