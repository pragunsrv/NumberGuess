import random
import time
import json
import os

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

def save_game_stats(attempts, max_attempts, success, number_to_guess):
    with open("game_stats.json", "a") as file:
        game_stats = {
            "attempts": attempts,
            "max_attempts": max_attempts,
            "number_to_guess": number_to_guess,
            "success": success
        }
        json.dump(game_stats, file)
        file.write('\n')

def load_game_stats():
    try:
        with open("game_stats.json", "r") as file:
            print("\nPrevious Game Statistics:")
            for line in file:
                game_stats = json.loads(line)
                print(f"Attempts: {game_stats['attempts']}, Max Attempts: {game_stats['max_attempts']}, Number: {game_stats['number_to_guess']}, Success: {'Won' if game_stats['success'] else 'Lost'}")
    except FileNotFoundError:
        print("No previous game statistics found.")

def leaderboard_entry(username, attempts):
    with open("leaderboard.json", "a") as file:
        entry = {
            "username": username,
            "attempts": attempts
        }
        json.dump(entry, file)
        file.write('\n')

def display_leaderboard():
    try:
        with open("leaderboard.json", "r") as file:
            print("\nLeaderboard:")
            for line in file:
                entry = json.loads(line)
                print(f"{entry['username']}: {entry['attempts']} attempts")
    except FileNotFoundError:
        print("No leaderboard data found.")

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
    with open("leaderboard_with_time.json", "a") as file:
        entry = {
            "username": username,
            "attempts": attempts,
            "time_taken": time_taken
        }
        json.dump(entry, file)
        file.write('\n')

def display_leaderboard_with_time():
    try:
        with open("leaderboard_with_time.json", "r") as file:
            print("\nLeaderboard with Time:")
            for line in file:
                entry = json.loads(line)
                print(f"{entry['username']}: {entry['attempts']} attempts, {entry['time_taken']:.2f} seconds")
    except FileNotFoundError:
        print("No leaderboard data found.")

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

def game_intro():
    print("Welcome to the Ultimate Number Guessing Game!")
    print("In this version, we have added more features to enhance your gaming experience.")

def save_highscore(username, score):
    try:
        with open("highscores.json", "r") as file:
            highscores = json.load(file)
    except FileNotFoundError:
        highscores = []

    highscores.append({"username": username, "score": score})
    highscores.sort(key=lambda x: x['score'])
    if len(highscores) > 10:
        highscores = highscores[:10]

    with open("highscores.json", "w") as file:
        json.dump(highscores, file, indent=4)

def display_highscores():
    try:
        with open("highscores.json", "r") as file:
            highscores = json.load(file)
            print("\nHighscores:")
            for entry in highscores:
                print(f"{entry['username']}: {entry['score']}")
    except FileNotFoundError:
        print("No highscores data found.")

def user_profile():
    try:
        with open("user_profiles.json", "r") as file:
            profiles = json.load(file)
    except FileNotFoundError:
        profiles = {}

    return profiles

def save_user_profile(username, attempts, score):
    profiles = user_profile()
    if username in profiles:
        profiles[username]['attempts'] += attempts
        profiles[username]['scores'].append(score)
    else:
        profiles[username] = {
            'attempts': attempts,
            'scores': [score]
        }

    with open("user_profiles.json", "w") as file:
        json.dump(profiles, file, indent=4)

def display_user_profile(username):
    profiles = user_profile()
    if username in profiles:
        user_profile = profiles[username]
        print(f"\nProfile for {username}:")
        print(f"Total attempts: {user_profile['attempts']}")
        print(f"Scores: {user_profile['scores']}")
    else:
        print(f"No profile found for {username}.")

def save_game_summary(username, score, time_taken):
    summary = {
        "username": username,
        "score": score,
        "time_taken": time_taken
    }
    if not os.path.exists("game_summary.json"):
        with open("game_summary.json", "w") as file:
            json.dump([summary], file, indent=4)
    else:
        with open("game_summary.json", "r") as file:
            summaries = json.load(file)
        summaries.append(summary)
        with open("game_summary.json", "w") as file:
            json.dump(summaries, file, indent=4)

def display_game_summary():
    try:
        with open("game_summary.json", "r") as file:
            summaries = json.load(file)
            print("\nGame Summaries:")
            for summary in summaries:
                print(f"Username: {summary['username']}, Score: {summary['score']}, Time Taken: {summary['time_taken']:.2f} seconds")
    except FileNotFoundError:
        print("No game summary data found.")

def enhanced_number_guessing_game_v10():
    game_intro()
    display_highscores()
    
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
    score = max_attempts - attempts if success else 0
    time_taken = 0
    if success:
        time_taken = timed_gameplay()[0]
        save_highscore(username, score)
        save_user_profile(username, attempts, score)
        save_game_summary(username, score, time_taken)
    
    display_user_profile(username)
    display_game_summary()
    
    if play_again():
        enhanced_number_guessing_game_v10()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    enhanced_number_guessing_game_v10()
