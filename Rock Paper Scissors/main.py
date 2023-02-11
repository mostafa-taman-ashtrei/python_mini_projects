import os
import random
from draw_choices import draw

options = ["rock", "paper", "scissors"]
playing, invalid = True, False


def choose_winner(player, computer):
    # It's a tie
    if player == computer:
        return ("it's a tie |:")

    # The Player Won
    elif ((player == "rock" and computer == "scissors") or
          (player == "paper" and computer == "rock") or
            (player == "scissors" and computer == "paper")):
        return ("You won, congratulations (:")

    # The Computer Won
    else:
        return ("You lost, better luck next time ):")


while playing:
    if not invalid:
        print("Choose rock, paper or scissors")

    else:
        print("Invalid option, please choose a valid option")
        invalid = False

    print("Or enter q to quit")

    player_choice = input().lower()
    computer_choice = random.choice(options)

    if player_choice in options:
        print(f"You picked {player_choice} {draw(player_choice)}")
        print("------------------------------------------------------------")
        print(f"The computer picked {computer_choice} {draw(computer_choice)}")
        print("------------------------------------------------------------")
        print(choose_winner(player_choice, computer_choice))

    elif player_choice == 'q':
        playing = False

    else:
        invalid = True

    # Clear the screen & play again
    if playing and not invalid:
        replay = input(
            "Wanna play again? Type y to replay\nor enter anything else to end the game\n").lower()
        print()
        playing = replay == "y"

    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
