# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:05:11 2019

@author: kyler

Advanced Python Module 1 HW.

Create a function that randomly generates 2 numbers and
returns a touple of two possible one-didget integers.

Use that function in the script to prompt the user with a 
multiplication question.

For a correct answer, display message "Very good!" and ask another quesiton.

For an incorrect answer, display "No. Please try again" and let the student 
try the same question until a correct answer is achieved. 
"""
import random

def makeNums(difficulty):
    """
    Difficulty 1:
    Generate 2 random 1 digit numbers and return them at 
    
    Difficulty 2:
    Generate 2 random numbers and return them. Numbers may be 
    single or double digit.
    """
    if (difficulty == 1):
        # Make tupl with random numbers
        numberTupl = (random.randint(0,9),random.randint(0,9))   
        return numberTupl
    else:
        numberTupl = (random.randint(0,99),random.randint(0,99))
        return numberTupl

def getUserAnswer():
    """
    This function gets user input and validates it to make sure it is a number.
    """
    while True:
        try:
            userAnswer = int(input("Enter your answer: "))
            break
        except ValueError:
            print("That was not a number. Please Enter a number: \n")
    
    return userAnswer

def goAgain():
    """
    This asks the user if they want to repeat the last set of 
    problems they were working on.
    """
    goAgain = input("Would you like to go again? 'Y/N'")
    goAgain = goAgain.lower()
    format()
    if (goAgain == 'y'):
        repeat = True
        return repeat
    elif(goAgain == 'n'):
        repeat = False
        return repeat
    

def questions(difficultySelection):
    """
    This is the difficulty 1 option. It will ask the user multiplication 
    questions involving single and digit numbers.
    """
    repeat = True
    difficulty = difficultySelection
    while repeat == True:
        #Get the random numbers
        numbers = makeNums(difficulty)
        answerWrong = True
        while (answerWrong == True):
            #Calculate the answer to the question
            questionAnswer = numbers[0] * numbers[1]
            
            #Form and ask the question
            print("How much is " + str(numbers[0]) + " times " + 
                  str(numbers[1]))
            
            #Get user answer
            userAnswer = int(getUserAnswer())
            
            #Compare user answer to actual answer
            if (userAnswer == questionAnswer):
                goodAnswer()
                answerWrong = False
            else:
                badAnswer()
                answerWrong = True
        
        repeat = goAgain()


def goodAnswer():
    """
    This function holds a set of replies if the user answers correctly and
    randomly selects one and returns it.
    """
    # Good answers
    randomChoice = random.randint(1,5)
    if (randomChoice == 1):
        print("Very good!")
    elif(randomChoice == 2):
        print("Great!")
    elif(randomChoice == 3):
        print("Fantastic!")
    elif(randomChoice == 4):
        print("Un-Bad!")
    elif(randomChoice == 5):
        print("Nice!")
    
    
def badAnswer():
    """
    This function holds a set of replies if the user answers incorrectly and
    randomly selects one and returns it.
    """
    # Bad answers
    randomChoice = random.randint(1,5)
    if (randomChoice == 1):
        print("Try again!")
    elif(randomChoice == 2):
        print("Good shot...Try again!")
    elif(randomChoice == 3):
        print("Not quite...Try again!")
    elif(randomChoice == 4):
        print("Give it another shot!")
    elif(randomChoice == 5):
        print("No.")

def intro():
    """
    This function introduces the user to the program and explains what it does.
    """
    format()
    print("This program will ask you to multiplication questions based on "+
          "the difficulty you select. Please choose a number from the menu "+
          "below: ")
    format()

def menu():
    """
    This function displays the main application menu to the user.
    """
    print("1. Easy")
    print("2. Difficult")
    print("3. Exit")
    format()
    
def format():
    """
    This function created a bar of '=' to seperate the output and help make
    it easier to read. 
    """
    print("="*45)

def main():
    # Introduce the program
    intro()
    #Control the while loop
    appGo = True
    #Loop to keep user in the program.
    while (appGo == True):
        # Call the menu
        menu()
        # Evaluate the user's menu selection
        menuSelection = getUserAnswer()
        # Ignore entries that are out of scope
        if (menuSelection <=0 or menuSelection>3):
            print("Invalid input. Please enter a number from the menu.")
        #Difficulty 1
        elif(menuSelection == 1):
            questions(menuSelection)
        #Difficulty 2
        elif (menuSelection == 2):
            questions(menuSelection)
        # Quit
        elif (menuSelection == 3):
            print("Exiting the application...Goodbye")
            appGo = False
            break
main()