# Number Guessing Game

## Overview

Welcome to the Number Guessing Game! This project is a fun and interactive game where players try to guess a randomly generated number within a specified range. This version of the game includes various features such as difficulty levels, user profiles, game summaries, leaderboards, and advanced statistics.

## Features

- **Basic Gameplay:** A simple number guessing game where players try to guess a number within a specified range.
- **Difficulty Levels:** Choose from easy, medium, or hard modes which determine the range of numbers.
- **Hints:** Provides hints to help players guess the number more accurately.
- **Leaderboard:** Track top scores and display them.
- **User Profiles:** Save and display user profiles including attempts and scores.
- **Game Summaries:** Save and display summaries of each game played, including username, score, and time taken.
- **Multi-Level Gameplay:** Play through multiple levels with increasing difficulty.
- **Simulation and Advanced Statistics:** Simulate games and provide detailed statistics about gameplay performance.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/pragunsrv/number-guessing-game.git
   cd number-guessing-game
   ```

2. **Ensure you have Python installed:** This project is compatible with Python 3.6 and above. You can download Python from [python.org](https://www.python.org/downloads/).

3. **Install Dependencies:** If there are any additional dependencies (not needed for this version but useful for further extensions), you can install them using pip.

## Usage

1. **Run the Game:**
   ```bash
   python number_guessing_game.py
   ```

2. **Game Instructions:**
   - Start the game and choose a difficulty level.
   - Guess the number within the allowed number of attempts.
   - After finishing a game, view statistics and optionally play again.

3. **Features:**
   - You will be prompted to enter your username.
   - The game will provide hints if your guess is too high or too low.
   - You can view the leaderboard and user profiles at any time during the game.
   - The game will save summaries of your sessions and display advanced statistics.

## File Descriptions

- `number_guessing_game.py`: Main game script with all functionalities.
- `game_stats.json`: Stores game statistics including attempts and success.
- `highscores.json`: Stores top scores for the game.
- `user_profiles.json`: Stores user profiles with their scores and attempts.
- `leaderboard.json`: Stores leaderboard entries with usernames and attempts.
- `leaderboard_with_time.json`: Stores leaderboard entries with time taken for each game.
- `game_summary.json`: Stores detailed game summaries including username, score, and time taken.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Create a pull request describing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
