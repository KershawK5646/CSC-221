'''
Kyler Kershaw
11/04/19
M4HW1

Question 3:
In a previous assignment, we used a list to simulate a queue (First In, First Out) data structure.
Write a program that takes 5 string values from a user, adds (enqueues) them to a queue , and then removes (dequeues)
them from the queue, printing them out in FIFO order.

Question 4:
Implement the same functionality as Question 3, but this time with a Queue class that uses Node objects to hold the
internal structure of the stack. You will find it much easier for this problem to use the TwoWayNode object since a
queue adds to the tail and removes from the head.
'''

import MyNodeClass as mnc

# Main class
def main():
    menuLoop = True
    while menuLoop == True:
        mainMenu()
        menuSelection = getUserInput()
        if menuSelection == 1:
            print("Question1")
            question1()
            menuLoop = goAgain()
        elif menuSelection == 2:
            print("Question2")
            question2()
            menuLoop = goAgain()
        elif menuSelection == 3:
            print("Question3")
            question3()
            menuLoop = goAgain()
        elif menuSelection == 4:
            print("Question4")
            question4()
            menuLoop = goAgain()
        else:
            print("Exit")
            print("Goodbye...")
            menuLoop = False

# Main menu
def mainMenu():
    print("Please make a selection:")
    print("1) Question 1.")
    print("2) Question 2.")
    print("3) Question 3.")
    print("4) Question 4.")
    print("5) Quit.")

# Get user input
def getUserInput():
    while True:
        try:
            userNumber = int(input("Enter a number: "))
            break
        except ValueError:
            print("\n This is not a number. Please enter a number.")

    return userNumber

def getUserString():
    userString = input("Please enter a name: ")
    return userString

def goAgain():
    print("Return to main menu?")
    print("1) Yes")
    print("2) No, EXIT")
    repeatSelection = getUserInput()
    if repeatSelection == 1:
        return True
    elif repeatSelection == 2:
        return False

def question1():
    question1Stack = []
    print(question1Stack)
    for count in range(5):
        question1Stack.append(getUserString())
        print(question1Stack)
    for index in question1Stack:
        question1Stack.pop()
        print(question1Stack)


def question2():
    myStack = mnc.Stack()
    for count in range(5):
        myStack.push(getUserString())
    myStack.printStack()

    for count in range(5):
        myStack.pop()
        myStack.printStack()
    # print empty stack
    myStack.printStack()

def question3():
    x=3

def question4():
    x=4


if __name__ == '__main__':
    main()