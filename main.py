#choose a number between 1 to 100 
from random import randint

def check_answer(guess,answer):
    if guess > answer:
        print('too high')
    elif guess < answer:
        print('too low')
    else:
        print("you've got it! Correct number was {answer}")


print("Welcome to the number guess game!")
print("I'm thinking of a number between 1 and 100")
answer = randint(1,100)

guess = input("Guess the number: ")    

