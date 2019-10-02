'''
Start: 9/14/2019
End:

1. Complete exercises 4.10, and 4.11. In addition, store the user's guesses in a list, and when they
correctly guess the number, show them the guesses they made.

2. Complete exercise 5.6.

3. Complete exercise 5.22.
'''

# imports
import random

def intro():
    """
    This function introduces the user to the program
    returns none
    :return:
    """
    print("Guess the Number Game: ")
    print("I will choose a number and you will guess it. Would you like to play?")

# Generate a random number.
def getRandomNumber():
    """
    This function generates a random number between 1 and 1000 and returns it.
    :return:
    """
    randomNumber = random.randrange(1, 1000)
    return randomNumber


# Prompt the user for their guess
def promptForGuess():
    while True:
        try:
            userGuess = int(input("Enter your guess..."))
            break

        except ValueError:
            print("That was not a number. Please enter a number: ")

    return userGuess

# This function asks the user if they want to repeat the game
def goAgain():
    """
    This function asks the user if they want to go again and passes their answer as a boolean.

    The boolean is returned.
    :return:
    """

    # Validate user answer as a number.
    while True:
        # Input validation
        while True:
            try:
                print("Would you like to play again?")
                goAgainAnswer = int(input("Enter 1 for yes or two for no."))
                break

            except ValueError:
                print("That was not a number. Please enter 1 or 2: ")

        # Test answer and assign bool value
        if (goAgainAnswer <= 0 or goAgainAnswer > 2):
            print("Selected answer out of range.")

        elif (goAgainAnswer == 1):
            goAgainBool = True
            break
        else:
            goAgainBool = False
            break


    # Returns the bool value
    return goAgainBool



# Main game function
def gameLoop(randomNumber):
    """
    This function gets passed a random number and prompts the user to input a number.
    The two numbers will be compared and a response will be generated based on a the
    relationship between them.
    """

    # Start the game
    print("I'm thinking of a number between 1 and 1000...")

    # Game accumulator
    guessCount = 0

    while True:
        # Add one to accumulator
        guessCount = guessCount + 1

        # Get guess from user.
        userNumber = promptForGuess()

        # Compare the guess to the random number and generate a reply.
        if (userNumber > randomNumber):
            print("Your guess is too high...Try again!")

        elif (userNumber < randomNumber):
            print("Your guess is too low...Try again!")

        else:
            print("Congrats ", randomNumber, "is the number! \nYou guessed it in ", guessCount, "tries!")
            break

    return guessCount

# Evaluate the number of times the user guessed.
def numberOfGuessEval(numberOfGuesses):
    if (numberOfGuesses > 10):
        print("You should be able to do better.")

    else:
        print("Either you know the secret or you got lucky!")

# Define main function
def main():
    # Call the intro
    intro()

    menuLoop = True

    while (menuLoop == True):

        # Get a random number.
        randomNumber = getRandomNumber()

        # Call the game loop and pass it the random number.
        numberOfGuesses = gameLoop(randomNumber)

        numberOfGuessEval(numberOfGuesses)

        # Ask to go again
        menuLoop = goAgain()

    print("Goodbye")

main()