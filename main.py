import random

# Basic number guessing game
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0
    max_attempts = 10

    while guess != number_to_guess and attempts < max_attempts:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")
        
        print(f"Attempts left: {max_attempts - attempts}")
    
    if guess != number_to_guess:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}. Better luck next time!")

def play_again():
    while True:
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay in ['yes', 'no']:
            return replay == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Additional functionality in version 2
def get_valid_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def set_difficulty():
    print("Select difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            if choice == '1':
                return random.randint(1, 50)
            elif choice == '2':
                return random.randint(1, 100)
            elif choice == '3':
                return random.randint(1, 200)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def enhanced_number_guessing_game():
    print("Welcome to the Enhanced Number Guessing Game!")
    number_to_guess = set_difficulty()
    guess = None
    attempts = 0
    max_attempts = 10

    while guess != number_to_guess and attempts < max_attempts:
        guess = get_valid_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")
        
        print(f"Attempts left: {max_attempts - attempts}")
    
    if guess != number_to_guess:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}. Better luck next time!")

# New functionalities in version 3
def show_hint(number_to_guess, guess):
    hint = ""
    if abs(number_to_guess - guess) <= 5:
        hint = "You're very close!"
    elif abs(number_to_guess - guess) <= 10:
        hint = "You're close!"
    else:
        hint = "You're far off!"
    print(f"Hint: {hint}")

def display_stats(attempts, max_attempts, success):
    print("\nGame Statistics:")
    print(f"Total attempts: {attempts}")
    print(f"Maximum attempts allowed: {max_attempts}")
    if success:
        print("You won the game!")
    else:
        print("You lost the game!")

def enhanced_number_guessing_game_v3():
    print("Welcome to the Enhanced Number Guessing Game Version 3!")
    number_to_guess = set_difficulty()
    guess = None
    attempts = 0
    max_attempts = 10

    while guess != number_to_guess and attempts < max_attempts:
        guess = get_valid_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
            show_hint(number_to_guess, guess)
        elif guess > number_to_guess:
            print("Too high! Try again.")
            show_hint(number_to_guess, guess)
        else:
            print("Congratulations! You guessed the number.")
        
        print(f"Attempts left: {max_attempts - attempts}")
    
    success = guess == number_to_guess
    if not success:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}. Better luck next time!")
    
    display_stats(attempts, max_attempts, success)

# New functionalities in version 4
def save_game_stats(attempts, max_attempts, success, number_to_guess):
    with open("game_stats.txt", "a") as file:
        file.write("Game Statistics:\n")
        file.write(f"Total attempts: {attempts}\n")
        file.write(f"Maximum attempts allowed: {max_attempts}\n")
        file.write(f"Number to guess: {number_to_guess}\n")
        if success:
            file.write("Result: Won\n\n")
        else:
            file.write("Result: Lost\n\n")

def load_game_stats():
    try:
        with open("game_stats.txt", "r") as file:
            print("\nPrevious Game Statistics:")
            print(file.read())
    except FileNotFoundError:
        print("No previous game statistics found.")

def enhanced_number_guessing_game_v4():
    print("Welcome to the Enhanced Number Guessing Game Version 4!")
    load_game_stats()
    number_to_guess = set_difficulty()
    guess = None
    attempts = 0
    max_attempts = 10

    while guess != number_to_guess and attempts < max_attempts:
        guess = get_valid_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
            show_hint(number_to_guess, guess)
        elif guess > number_to_guess:
            print("Too high! Try again.")
            show_hint(number_to_guess, guess)
        else:
            print("Congratulations! You guessed the number.")
        
        print(f"Attempts left: {max_attempts - attempts}")
    
    success = guess == number_to_guess
    if not success:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}. Better luck next time!")
    
    display_stats(attempts, max_attempts, success)
    save_game_stats(attempts, max_attempts, success, number_to_guess)

if __name__ == "__main__":
    while True:
        enhanced_number_guessing_game_v4()
        if not play_again():
            print("Thanks for playing! Goodbye!")
            break
