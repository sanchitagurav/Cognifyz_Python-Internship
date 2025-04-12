import random

def number_guesser():
    print("🎯 Welcome to the Number Guesser Game!")

    # Get range from user
    try:
        min_range = int(input("Enter the minimum number: "))
        max_range = int(input("Enter the maximum number: "))

        if min_range >= max_range:
            print("Invalid range! Minimum should be less than maximum.")
            return

        secret_number = random.randint(min_range, max_range)
        attempts = 0

        while True:
            guess = int(input(f"Guess a number between {min_range} and {max_range}: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                break

    except ValueError:
        print("Please enter valid numbers!")

# Run the game
number_guesser()
