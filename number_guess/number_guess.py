import random

first_range_of_guess = int(input("give me the first number in your range: "))
second_range_of_guess = int(input("now the second number: "))

selected_number = random.randint(first_range_of_guess, second_range_of_guess)

guess = 0
guessed = False
guess_left = 10


while(guessed == False and guess_left != 0 ):
    guessed_number = int(input(f"guess the number ({guess_left} guess left): "))
    if(guessed_number == selected_number):
        guess += 1
        guess_left -= 1
        print(f"congrats you guessed the number correctly :) \n number of guess to win: {guess}")
        guessed = True
    elif(guessed_number > selected_number):
        guess += 1
        guess_left -= 1
        print(f"nope you guessed higher \n number of guess left: {guess_left}")
    elif(guessed_number < selected_number):
        guess += 1
        guess_left -= 1
        print(f"nope you guessed lower \n number of guess left: {guess_left}")



if(guessed == False):
    print(f"well the number was {selected_number} by the way (you lose sorry)")        