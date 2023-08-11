import random
import time
CYAN = "\033[34m"
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
ORANGE = "\033[38;5;208m"

# THE GAME
def best_two_out_of_three():
    data = {
        "user_round_score" : 0,
        "user_game_score" : 0,
        "opponent_round_score" : 0,
        "opponent_game_score" : 0,
        "play_game" : True
    }

    # Start Menu
    while True:
        print(f'{YELLOW}Hello, this is Best Two Out of Three!\nType "a" to roll or "b" to quit.\nWhoever rolls higher (you or the computer) wins the round.\nThe best two out of three wins!\nIn the event of ties, continue to re-roll until one of you emerges victorios.\nHAVE FUN!\n{RESET}')
        initialize = input(f"{GREEN} Choose an option\n A. Play game      B. Exit\n {RESET}")

        if initialize.lower() == "a":
            data["play_game"] = True
            break
        elif initialize.lower() == "b":
            give_score(data, resume=False)
            break

    while data["play_game"] is True:

        choice = input(f"{CYAN} Choose an option\n A. Roll Dice      B. Exit\n {RESET}")
        if choice.lower() == "a":
            # User's roll
            user_roll = random.randint(1, 6)

            print(f"You rolled {user_roll}")
            time.sleep(1)

            # Computer's roll
            opponent_roll = random.randint(1, 6)

            print(f"Your opponent rolled {opponent_roll}")

            # Determine score for round 
            if user_roll < opponent_roll:
                data["opponent_round_score"] += 1
                end_round("lost", data)
            elif user_roll > opponent_roll:
                data["user_round_score"] += 1
                end_round("won", data)
            else:
                data["opponent_round_score"] += 1
                data["user_round_score"] += 1
                end_round("tie", data)

        # Quit game
        elif choice.lower() == "b":
            give_score(data, resume=False)

# Display outcome of roll
def end_round(outcome, data):
    time.sleep(1)
    if outcome == "tie":
        print(f"{ORANGE} The roll tied! {RESET}")
    else:
        print(f"{ORANGE} You {outcome} that round {RESET}")

    time.sleep(1)
    return tally_points(data)

# Determine if game is over
def tally_points(data):
    finished = False
    option_to_restart = None
    scores_to_win = [2, 3]

    # User wins
    if data["user_round_score"] in scores_to_win and data["opponent_round_score"] < 2:
        finished = True
        option_to_restart = input(f"{GREEN} You won Best Two Out of Three! Play again?\n Y / N\n {RESET}")
        
        data["user_game_score"] += 1

    # Computer wins
    elif data["opponent_round_score"] in scores_to_win and data["user_round_score"] < 2:
        finished = True
        option_to_restart = input(f"{RED} You lost Best Two Out of Three. Try again?\n Y / N\n {RESET}")
        
        data["opponent_game_score"] += 1

    # Tie breaker
    elif data["user_round_score"] > 1 and data["opponent_round_score"] > 1 and data["user_round_score"] == data["opponent_round_score"]:
        print(f"{YELLOW} Tie game! Reroll! {RESET}")

    # Tie breaker result
    # user wins 
    elif data["user_round_score"] > data["opponent_round_score"] and data["user_round_score"] != 1:
        finished = True
        option_to_restart = input(f"{GREEN} You won Best Two Out of Three! Play again?\n Y / N\n {RESET}")
        data["user_game_score"] += 1

    # computer wins 
    elif data["user_round_score"] < data["opponent_round_score"] and data["opponent_round_score"] != 1:
        finished = True
        option_to_restart = input(f"{RED} You lost Best Two Out of Three. Try again?\n Y / N\n {RESET}")
        data["opponent_game_score"] += 1

    if option_to_restart is not None:
        while option_to_restart.lower() not in ["y", "n"]:
            option_to_restart = input("Please enter 'Y' or 'N': ")

    if finished == True:
        return end_game_or_new_game(option_to_restart, data)

# Start new game or finish
def end_game_or_new_game(option_to_restart, data):
    if option_to_restart.lower() == "n":
        return give_score(data, resume=False)
    elif option_to_restart.lower() == "y":
        return give_score(data, resume=True)

# Tell game score, if applicable
def give_score(data, resume=False):
    if not resume:
        if data["user_game_score"] or data["opponent_game_score"] != 0:
            print(f"Good game! Your score was {data['user_game_score']}, and the computer's score was {data['opponent_game_score']}")
        else:
            print("No problem! I'm here when you want to play.")
        data["play_game"] = False

    else:
        data["user_round_score"] = 0
        data["opponent_round_score"] = 0
        print(f"The score is {data['user_game_score']} (you) to {data['opponent_game_score']} (computer)")

print(best_two_out_of_three())