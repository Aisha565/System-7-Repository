
import random


def calculator():
    # Get numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # Perform the selected operation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers.")


def guessing_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    print("\nGuess the number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 10:
                print("Enter a number between 1 and 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Correct! You won.")
                break

        except ValueError:
            print("Please enter a whole number.")


def main():
    # Display the main menu
    while True:
        print("\n--- Python Mini Programs ---")
        print("1. Calculator")
        print("2. Number Guessing Game")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            guessing_game()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
