import random
import time

# Terminal colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Computer picks a secret number between 1 and 50
secret_number = random.randint(1, 50)
attempts = 0

print("\n==========================================")
print(CYAN + "   🎯 WELCOME TO THE NUMBER GUESSING GAME 🎯" + RESET)
print("==========================================")
print("I am thinking of a secret number between 1 and 50.")
print("Can you guess what it is?\n")
# Keep looping until the player guesses the right number
while True:
    guess = int(input("🔢 Enter your guess (1-50): "))
    attempts = attempts + 1

    if guess < secret_number:
        print(YELLOW + "📉 Too low! Try a higher number.\n" + RESET)
    elif guess > secret_number:
        print(RED + "📈 Too high! Try a lower number.\n" + RESET)
    else:
        print("\n==========================================")
        print("Checking...")
        time.sleep(1)
        print(GREEN + f"🎉 BINGO! The secret number was {secret_number}!" + RESET)
        print(CYAN + f"🏆 You found it in {attempts} attempts!" + RESET)
        print("==========================================\n")
        break