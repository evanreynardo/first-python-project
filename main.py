import random
import time

while True:
    print("ROCK PAPER SCISSORS")
    print("Choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    user_input = input("You'd play: ")

    print("Robot is thinking...")
    time.sleep(1.5)

    random_choice = random.choice(["Rock", "Paper", "Scissors"])

    user_input_fixed = user_input.strip().capitalize()

    if user_input_fixed not in ["Rock", "Paper", "Scissors"]:
        print("U should play either rock, paper or scissors")
        print("Generating again...")
        time.sleep(1.5)
        continue

    if user_input_fixed == random_choice:
        print("Tie, you both chose the same choice")

    elif user_input_fixed == "Rock" and random_choice == "Paper":
        print("Robot wins, YOU: ROCK | ROBOT: PAPER")
    elif user_input_fixed == "Rock" and random_choice == "Scissors":
        print("You win, YOU: ROCK | ROBOT: SCISSORS")

    elif user_input_fixed == "Scissors" and random_choice == "Rock":
        print("Robot wins, YOU: SCISSORS | ROBOT: ROCK")
    elif user_input_fixed == "Scissors" and random_choice == "Paper":
        print("You win, YOU: SCISSORS | ROBOT: PAPER")

    elif user_input_fixed == "Paper" and random_choice == "Scissors":
        print("Robot wins, YOU: PAPER | ROBOT: SCISSORS")
    elif user_input_fixed == "Paper" and random_choice == "Rock":
        print("You win, YOU: PAPER | ROBOT: ROCK")


    user_input_continue = input("Wanna play again? (y/n): ")
    if user_input_continue.strip().lower() == "y":
        print("Generating again...")
        time.sleep(1.5)
        continue
    elif user_input_continue.strip().lower() == "n":
        print("Thanks for playing, have a good day!")
        break
    else:
        print("I think u missclicked but anyways i don't wanna play again, bye")
        break
    
    

    