import random


def main():
    count = 1
    lower = 1
    upper = 1000
    hidden = random.randint(lower, upper)

    while count <= 10:
        user_guess = input(f"Enter your guess from {lower} to {upper}: ")

        while not user_guess.isnumeric():
            print("Invalid input. Please enter a number!")
            user_guess = input(f"Enter your guess from {lower} to {upper}: ")

        user_guess = int(user_guess)
        if user_guess < lower or user_guess > upper:
            print("Invalid input. Please enter a number within the range!")
            continue
        if user_guess == hidden:
            print(f"You got it! The hidden number is {hidden}")
            print(f"It took you {count} guess(es).")
            break
        elif user_guess > hidden:
            upper = user_guess - 1
        else:
            lower = user_guess + 1

        print(f"Wrong! Guess count: {count}")
        count += 1


if __name__ == '__main__':  # ture, only when you're running this file
    main()
