import random

randomnum = random.randint(1, 100)

try:
    guess = int(input("Guess a number between 1 and 100: "))

    def num_guessing(guess):
        trial = 0

        while trial < 7:
            trial += 1

            if guess == randomnum:
                print("You won!")
                return

            if guess > randomnum:
                print("Guess lower")
            else:
                print("Guess higher")

            if trial < 7:
                guess = int(input("Guess again: "))

        print("You lost! The number was", randomnum)

    num_guessing(guess)

except:
    print("Invalid input. Please enter a number between 1 and 100.")