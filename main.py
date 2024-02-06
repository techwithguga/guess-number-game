#choose a number between 1 to 100 
from random import randint

EASY_LEVEL_TRIES = 10
HARD_LEVEL_TRIES = 5

#check user answer against actuan chosen number
def check_answer(guess,answer, tries):
    """checks answer against guess. Returns the number of turns remaning"""
    if guess > answer:
        print('too high')
        return tries-1
    elif guess < answer:
        print('too low')
        return tries-1
    else:
        print(f'you\'ve got it! Correct number was {answer}.')

#function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty: Type 'easy' or 'hard' :")
    if level == "easy":
        return EASY_LEVEL_TRIES
    else:
        return HARD_LEVEL_TRIES
        
def game():
    print("Welcome to the number guess game!")
    print("I'm thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f'the answer is : {answer}')
    
    tries =  set_difficulty()
    
    #repeat guessing if they get it wrong and have tries left
    guess = 0
    while guess != answer:
        print(f'You have {tries} remaining to guess the number.')

        guess = int(input("Guess the number: ")) 
        tries = check_answer(guess, answer, tries)
        if tries == 0:
            print("No tries left,you lose!")
            return
game()

