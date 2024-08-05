import random
import time

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

# New functionalities in version 5
def leaderboard_entry(username, attempts):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{username}: {attempts} attempts\n")

def display_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            print("\nLeaderboard:")
            print(file.read())
    except FileNotFoundError:
        print("No leaderboard data found.")

def enhanced_number_guessing_game_v5():
    print("Welcome to the Enhanced Number Guessing Game Version 5!")
    load_game_stats()
    display_leaderboard()
    
    number_to_guess = set_difficulty()
    guess = None
    attempts = 0
    max_attempts = 10
    
    username = input("Enter your username: ")
    
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
    if success:
        leaderboard_entry(username, attempts)

# New functionalities in version 6
def timed_gameplay():
    start_time = time.time()
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

    end_time = time.time()
    time_taken = end_time - start_time
    
    success = guess == number_to_guess
    if not success:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}. Better luck next time!")
    
    display_stats(attempts, max_attempts, success)
    print(f"Time taken: {time_taken:.2f} seconds")
    
    save_game_stats(attempts, max_attempts, success, number_to_guess)
    return time_taken, success

def leaderboard_entry_with_time(username, attempts, time_taken):
    attempts = attempts
    with open("leaderboard_with_time.txt", "a") as file:
        file.write(f"{username}: {attempts} attempts, {time_taken:.2f} seconds\n")

def display_leaderboard_with_time():
    try:
        with open("leaderboard_with_time.txt", "r") as file:
            print("\nLeaderboard:")
            print(file.read())
    except FileNotFoundError:
        print("No leaderboard data found.")

def enhanced_number_guessing_game_v6():
    print("Welcome to the Enhanced Number Guessing Game Version 6!")
    load_game_stats()
    display_leaderboard_with_time()
    
    username = input("Enter your username: ")
    
    time_taken, success = timed_gameplay()
    
    if success:
        leaderboard_entry_with_time(username, attempts, time_taken)
    
    if play_again():
        enhanced_number_guessing_game_v6()
    else:
        print("Thanks for playing! Goodbye!")

# New functionalities in version 7
def multi_level_game():
    print("Welcome to the Multi-Level Number Guessing Game!")
    
    level = 1
    total_attempts = 0
    max_levels = 3
    
    while level <= max_levels:
        print(f"\n--- Level {level} ---")
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
                print(f"Congratulations! You guessed the number in level {level}.")
                break

            print(f"Attempts left: {max_attempts - attempts}")
        
        if guess != number_to_guess:
            print(f"Sorry, you've run out of attempts. The number was {number_to_guess}. Moving to the next level.")
        
        total_attempts += attempts
        level += 1
    
    print("\nGame Over!")
    print(f"Total attempts used across all levels: {total_attempts}")

def enhanced_number_guessing_game_v7():
    multi_level_game()
    
    if play_again():
        enhanced_number_guessing_game_v7()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    enhanced_number_guessing_game_v7()
