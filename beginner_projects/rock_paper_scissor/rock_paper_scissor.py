import random


choices = ['rock','paper','scissor']
available_commands = ['r','p','s']


def play_again():
    print("( y => yes | n => no )")
    play_again = input("wanna play again? ").lower()
    return play_again == "y"


game_on = True
while game_on:
    computer_choice = random.choice(choices)
    print("Game Started")
    print("how to play : r => rock | p => paper | s => scissor")
    player_choice = input("ok now write and enter your choice: ").lower()

    if player_choice not in available_commands:
        print("\ninvalid command")
        continue

    if player_choice == "r":
        if computer_choice == "scissor":
            print("you won :)")
            print(f"computer chose: {computer_choice}")
            game_on = play_again()

        elif computer_choice == "rock":
            print("it's a draw :|")
            print(f"computer chose: {computer_choice}")
            game_on = play_again()

        else:    
            print("you lost :(")
            print(f"computer chose: {computer_choice}")
            game_on = play_again()


    elif player_choice == "p":
        if computer_choice == "scissor":
            print("you lost :(")
            print(f"computer chose: {computer_choice}")
            game_on = play_again()

        elif computer_choice == "paper":
            print("it's a draw :|")
            print(f"computer chose: {computer_choice}")
            game_on = play_again()

        else:    
            print("you won :)")
            print(f"computer chose: {computer_choice}")
            game_on = play_again()


            
    elif player_choice == "s":
        if computer_choice == "scissor":
            print("it's a draw :|")
            print(f"computer chose: {computer_choice}")
            game_on = play_again()

        elif computer_choice == "rock":
            print("you lost :(")
            print(f"computer chose: {computer_choice}")
            game_on = play_again()

        else:    
            print("you won :)")
            print(f"computer chose: {computer_choice}")
            game_on = play_again()