"""
A basic Rock-Paper-Scissors game with enhanced input validation.
The program allows the user to play Rock-Paper-Scissors against the computer. It ensures
valid input values with clear error messages and allows the user to specify whether to play
again after each round. The game outputs ASCII art representing the choices of both the user
and the computer.
Functions:
- read_user_choice: Reads and validates the user's choice for Rock, Paper, or Scissors.
- read_play_again: Reads and validates whether the user wants to play another round.
"""
import random
from enum import IntEnum, StrEnum


ASCII_ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
ASCII_PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
ASCII_SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


"""
Shorter version and as expected in course.
"""
# ASCII_LIST = [ASCII_ROCK, ASCII_PAPER, ASCII_SCISSORS]
# user_choice = int(input("What do ypu choice? Rock (1), Paper (2), Scissors (3)? "))
# computer_choice = random.randint(1, 3)
# print(f"User chose: \n{ASCII_LIST[user_choice - 1]}\n"
#       f"Computer chose: \n{ASCII_LIST[computer_choice - 1]}")
# if user_choice == computer_choice:
#     print("It's a draw!")
# elif (user_choice == 1 and computer_choice == 3) or \
#         (user_choice == 2 and computer_choice == 1) or \
#         (user_choice == 3 and computer_choice == 2):
#     print("You win!")
# else:
#     print("You lose!")


"""
As upgrade of this program I propose add validation to input: non empty, non spaces, entity specific checks.
"""
class Choice(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(StrEnum):
    DRAW = "draw"
    WIN = "win"
    LOSE = "lose"


ASCII_DICT = {
    Choice.ROCK: ASCII_ROCK,
    Choice.PAPER: ASCII_PAPER,
    Choice.SCISSORS: ASCII_SCISSORS,
}


def read_user_choice() -> Choice:
    while True:
        raw = input(
            f"Choose {Choice.ROCK.name.title()} ({Choice.ROCK}), "
            f"{Choice.PAPER.name.title()} ({Choice.PAPER}), "
            f"{Choice.SCISSORS.name.title()} ({Choice.SCISSORS}): "
        ).strip()
        try:
            return Choice(int(raw))
        except ValueError:
            print(f"Error: Enter {Choice.ROCK}, {Choice.PAPER}, or {Choice.SCISSORS}.")

def read_play_again() -> bool:
    while True:
        raw = input("Play again? (y/n): ").strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("Error: Please enter 'y' or 'n'. Try again.")

def get_result(user: Choice, computer: Choice) -> Result:
    if user == computer:
        return Result.DRAW
    winning_pairs = {
        (Choice.ROCK, Choice.SCISSORS),
        (Choice.PAPER, Choice.ROCK),
        (Choice.SCISSORS, Choice.PAPER),
    }
    return Result.WIN if (user, computer) in winning_pairs else Result.LOSE

while True:
    user_choice = read_user_choice()
    computer_choice = random.choice(tuple(Choice))
    print(
        f"User chose: \n{ASCII_DICT[user_choice]}\n"
        f"Computer chose: \n{ASCII_DICT[computer_choice]}"
    )
    result = get_result(user_choice, computer_choice)
    if result == Result.DRAW:
        print("It's a draw!")
    elif result == Result.WIN:
        print("You win!")
    else:
        print("You lose!")
    if not read_play_again():
        print("Bye!")
        break
