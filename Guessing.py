import random

def print_trophy():
    print("  _______ ")
    print(" |_____|  ")
    print(" |_____|  ")
    print(" |_____|  ")
    print("   |||    ")
    print("   |||    ")
    print("   |||    ")

def print_smiley_face():
    print("  *******  ")
    print(" *       * ")
    print("*  O   O  *")
    print("*    ∆    *")
    print(" *  \\//  * ")
    print("  *     *  ")
    print("   *****   ")

def get_valid_integer_input(prompt, error_message="Invalid input. Please enter a valid number."):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print(error_message)

def play_game(difficulty_settings):
    range_start, range_end, max_attempts = difficulty_settings
    secret_number = random.randint(range_start, range_end)

    print(f"\nI'm thinking of a number between {range_start} and {range_end}.\n")

    for attempt in range(1, max_attempts + 1):
        guess = get_valid_integer_input(f"Attempt {attempt}/{max_attempts}: Enter your guess: ")

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} tries.")
            return attempt

    print(f"\nSorry, you've used all {max_attempts} attempts. The secret number was {secret_number}.")
    return max_attempts + 1

def main():
    print("### Guess the Number Game ###")

    high_scores = {"easy": float('inf'), "medium": float('inf'), "hard": float('inf'), "custom": float('inf')}

    while True:
        print("\nMain Menu:")
        print("1. Play the Game")
        print("2. View High Scores")
        print("3. Quit")

        choice = input("Enter the number of your choice (1/2/3): ").strip()

        if choice == "1":
            print("\nChoose a difficulty level:")
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            print("4. Custom")

            difficulty_choice = input("Enter the number of your choice (1/2/3/4): ").strip()

            if difficulty_choice == "1":
                difficulty = "easy"
            elif difficulty_choice == "2":
                difficulty = "medium"
            elif difficulty_choice == "3":
                difficulty = "hard"
            elif difficulty_choice == "4":
                range_start = get_valid_integer_input("Enter the lower bound for the range: ")
                range_end = get_valid_integer_input("Enter the upper bound for the range: ")
                max_attempts = get_valid_integer_input("Enter the number of attempts: ")
                difficulty = "custom"
                difficulty_settings = (range_start, range_end, max_attempts)
            else:
                print("Invalid choice. Please select a valid option.")
                continue

            high_scores[difficulty] = min(high_scores[difficulty],
                                          play_game((1, 50 + int(difficulty_choice), 10 - int(difficulty_choice) // 2)))

        elif choice == "2":
            print("\nHigh Scores:")
            for difficulty, score in high_scores.items():
                print(f"{difficulty.capitalize()}: {score if score != float('inf') else 'N/A'} tries")
            print_trophy()  # Print trophy after high scores

        elif choice == "3":
            print_smiley_face()  # Print smiley face when quitting
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
