#guessig game
import random

def guessGAme():
    guess_num = random.randint(1,100)

    while True:

        guess = int(input("Enter a number between 1-100 to guess: "))

        if guess != guess_num:
            if guess > guess_num:
                print("Lower")
            elif guess < guess_num:
                print("Higher")
        elif guess == guess_num:
            print("Yay you successfully guessed the number: ", guess_num)
            break
        else:
            print("Invalid Input")

guessGAme()