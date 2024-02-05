#choose a number between 1 to 100 
from random import randint

EASY_LEVEL_TRIES = 10
HARD_LEVEL_TRIES = 5

#check user answer against actuan chosen number
def check_answer(guess,answer):
    
    if guess > answer:
        print('too high')
    elif guess < answer:
        print('too low')
    else:
        print("you've got it! Correct number was {answer}")

#function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty: Type 'easy' or 'hard' :")
    if level == "easy":
        return EASY_LEVEL_TRIES
    else:
        return HARD_LEVEL_TRIES
        

print("Welcome to the number guess game!")
print("I'm thinking of a number between 1 and 100")
answer = randint(1,100)
print(f'the answer is : {answer}')
tries =  set_difficulty()
print(f'You have {tries} remaining to guess the number.')

guess = int(input("Guess the number: ")) 
check_answer(guess, answer)
