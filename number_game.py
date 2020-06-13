"""
Python Web Development Techdegree, Treehouse
Project 1 - Number Guessing Game, Ryan A. Whitney, June - 2020
--------------------------------
"""

from random import randint

def username_intake():
    user = str()
    user = str(input('Please enter your user name: '))
    while len(user) == False:
        print('Well we can\'t call you nothing, please try again!\n')
        user = str(input('Please enter your user name: '))
    return user


def get_user_guess():
    guess = int()
    flag = True
    while flag:
        try:
            guess = int(input('\nPlease enter a guess between 1 & 10: '))
            if guess < 11 and guess > 0:
                flag = False
            else:
                print('Your signal broke up, please try a guess between 1 & 10!\n')
        except ValueError:
            print('Houston we have a problem, please try again! \n')
    return guess
   
    
def replay_option(score): 
    high_score = int(score)
    choice = (input("Would you like to play again? Enter [y]es or [n]o: ")).lower()

    while choice == 'y':
        print("\nWe're sure glad to have you back!\n")
        print("The current high score to beat is {} guesses!\n".format(high_score))
        print('We know you can do it!')
        main_program()
              
        
    if choice == 'n':
        print('\nThanks for Playing!\n')
        exit()
   

def main_program():
    correct_answer = randint(1,10)
    # print(correct_answer)
    
    score = 1
    print('\n\nWelcome to the Number Guessing Game!\n')
    user_name = username_intake()
    print('\nWelcome on board, {}! We\'re glad to have you here!\n'.format(user_name))
    
    user_guess = get_user_guess()
        
    if user_guess != correct_answer:
        if user_guess < correct_answer:
            score += 1
            print('\nYou\'re coming in a little low, try higher!\n')
            get_user_guess()
        elif user_guess > correct_answer:
            score += 1
            print('\nYou\'re coming in a little high, try lower!\n')
            get_user_guess()
    if user_guess == correct_answer:
            if score == 0:
                score = 1
                print("The Eagle Has Landed!  You've guessed it!\n")
                print("It took you {} attempts to guess the correct number!\n".format(score))
                return score
            elif score != 0:
                print("The Eagle Has Landed!  You've guessed it!\n")
                print("It took you {} attempts to guess the correct number!\n".format(score))
                return score
          
high_score = main_program()

replay_option(high_score)
