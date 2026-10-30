# Write a Python program that:
# 1. Stores a secret number in a variable.
# 2. Asks the user to guess the number.
# 3. Uses a while loop to keep asking until the user guesses correctly.
# 4. If the guess is too high, print "Too high!"
# 5. If the guess is too low, print "Too low!"
# 6. When the guess is correct, print "Congratulations! You guessed it."

import random 

number= random.randint(1,100)
guess = int(input("Guess a number between 1 to 100: "))
while guess!= number:
    guess= int(input("try again to guess number between 1 to 100"))
    if guess > number:
        print("guess number is too high ")
    elif guess < number:
        print("guess number is too low ")
    else:
        print ("congratulation you guess it right ")
   