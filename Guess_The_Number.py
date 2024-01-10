import random
from random import randint

print("Welcome to the Guessing Game \n"
      "You will be asked to guess and a number. \n"
      "As the computer I have guessed a number between 1 and 20. \n"
      "You will have 6 tries to guess my number if you fail you lose.")

secretNumber = randint(1 , 21)
print(secretNumber)
print(type(secretNumber))
'''
need to convert guess from string to int!!!!!!
'''
guess = input("Please select a number between 1 and 20. You have 6 tires to get it right. ")
print(guess)
guess = int(guess)

numberOfTurns = 6

while numberOfTurns > 0:
    numberOfTurns = numberOfTurns - 1

    if guess == secretNumber:
        print(f"Congratulations you guessed {guess} and  my number was {secretNumber}")
        break
    elif guess > secretNumber:
        print(f"You guess of {guess} is larger than my number")
    elif guess < secretNumber:
        print(f"Your guess of {guess} is smaller than my number")
    guess = input(f"You have {numberOfTurns} left what is your next guess? ")
    guess = int(guess)
else:
    print("You have no more guesses")


print("Thank you for playing I look forward to playing with you aging later")



