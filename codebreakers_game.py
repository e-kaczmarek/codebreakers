#
# Codebreakers Gaming Platform
#
# By Elyse Kaczmarek
#
#

from random import random

def rps():
    # rock-paper-scissors game
    print("\nWelcome to Rock-Paper-Scissors!\n")
    rps = ['rock', 'paper', 'scissors']
    computer_choice = rps[int(random()*3)]
    user_input = input("Rock, Paper, or Scissors? ")
    while (user_input.lower() not in rps):
        print("I didn't understand you. Please input a choice of rock, paper, or scissors.")
        user_input = input("Rock, Paper, or Scissors? ")
    choices = "You chose " + user_input.lower() + " and the computer chose " + computer_choice + '!'
    if (user_input.lower() == computer_choice):
        print(choices)
        print("It's a tie!")
    elif ((user_input.lower() == 'rock') and (computer_choice == 'scissors')):  #rock beats scissors
        print(choices)
        print("You won!!!")
    elif ((user_input.lower() == 'paper') and (computer_choice == 'rock')): #paper beats rock
        print(choices)
        print("You won!!!")
    elif ((user_input.lower() == 'scissors') and (computer_choice == 'paper')): #scissors beats paper
        print(choices)
        print("You won!!!")
    else: #you lost
        print(choices)
        print("Better luck next time!")
    input()
    main_menu()


def gtn():
    # guess the number game
    print("\nWelcome to Guess the Number!")
    print("You have 3 chances to guess my number between 1 and 10. Good luck!")
    chances = 3
    computer_num = str(int(random()*10) + 1)
    while (chances != 0):
        chances -= 1
        user_choice = input("Choose your number! ")
        if (user_choice == computer_num):
            print("You won!!!")
            break
        print("\nThat was not my number :/")
        print('You have', chances, 'chances remaining.\n')
        if (chances == 0):
            print("My number was " + computer_num)
    input()
    main_menu()

def m8b():
    # magic eight ball game
    print("\nWelcome to Magic 8 Ball!")
    yes = 'Yes!'
    no = 'Nope.'
    maybe = "There's a chance"
    meh = 'The spirits are tired today. Try calling again later.'
    idk = 'How should I know?'
    shrug = '¯\_(ツ)_/¯'
    magic_list = [yes, no, maybe, meh, idk, shrug]
    answer = magic_list[int(random()*len(magic_list))]
    question = input("Ask the spirits a question... ")
    print('\n' + answer)
    input()
    main_menu()


def main_menu():
    # begins right after program is run
    # prints a series of menu options and directs user to
    # whichever game they choose
    print('-----------------------------')
    print("Hello! Welcome to the Codebreakers gaming platform.\n")
    print("This is the main menu.\n")
    print("Here are the games we currently offer:")
    print('1: Rock-Paper-Scissors')
    print('2: Guess the number!')
    print('3: Magic Eight Ball')
    print('Q: Quit Main Menu')
    user_input = input('Which game would you like to play? ')
    while (user_input not in '123qQ'):
        print("Sorry, I didn't quite catch that.")
        user_input = input("Please select the number of the game you would like \
to play, or type 'Q' to quit the main menu. ")
    
    if (user_input == '1'):
        rps()
    elif (user_input == '2'):
        gtn()
    elif (user_input == '3'):
        m8b()
    else:
        return

# running the game -- keeps returning to the main menu until user quits

main_menu()
print("Thanks for playing!")
