import random


words_list = ['javascript', 'python', 'php', 'dart','csharp', 'golang', 'django','laravel', 'nodejs']

selected_word = random.choice(words_list)

guess_limit = int(input("set the times you want to guess: "))

if(guess_limit < 1):
    print('Invalid input')

selected_word_length = len(selected_word)

all_letters = ''
current_guess = ''


while guess_limit > 0:
    current_guess = input(f"word's length = {selected_word_length} \nguess the word: ")
    all_letters +=  current_guess

    for letter in selected_word.lower():
        if letter in all_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    # after the loop to show the correct letters, we check if the word was correct or not       
    if (current_guess.lower() == selected_word):
        print("\n***********************")
        print("Congratulations! You got it right.")
        print(f"word was {selected_word}")
        print("***********************")
        break
    else:
        guess_limit -= 1

        if(guess_limit==0):
            print("\n***********************")
            print("Sorry, you ran out of guesses.")
            print(f"the word was {selected_word}.")
            print("***********************")
            break
        else:
            print(f"\n\nYou have {guess_limit} guesses remaining.")
            print("***********************")

