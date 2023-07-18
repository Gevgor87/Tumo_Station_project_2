from random import randint
from time import sleep
def game():
    dice = []
# Dice pictures for print -------------------
    dice_pic = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")}
#-----------------------------------------------

    input("To roll dices press enter: ")

# Random choice 2 dices-------------------------
    for _ in range(2):
        dice.append(randint(1, 6))
# ----------------------------------------------

# Printing dices and their sum-------------------
    for line in range(5):
        for die in dice:
            print(dice_pic.get(die)[line], end="")
        print()

    total = sum(dice)
    print(f"\nTotal {total}")
#----------------------------------------------

# Game Body------------------------------------
    if total == 7 or total == 11:
        sleep(0.5)
        print("\n\tCONGRATULATIONS YOU WIN")
    elif total == 2 or total == 3 or total == 12:
        sleep(0.5)
        print("\n\t\tCraps\n\tSorry Casino Wins")
    else:
        goal = total
        sleep(0.5)
        print(f"\n\tTHE GOAL NUMBER IS {goal}")
        while True:
            dice = []
            sleep(0.5)
            input("\nTo roll dices press enter: ")
            for _ in range(2):
                dice.append(randint(1, 6))

            for line in range(5):
                for die in dice:
                    print(dice_pic.get(die)[line], end="")
                print()

            total = sum(dice)
            if total == 7:
                sleep(0.5)
                print(f"\t\tUPS {total}\n\tSorry Casino Wins")
                break
            elif total == goal:
                sleep(0.5)
                print("\t\tGOAL NUMBER\n\tCONGRATULATIONS YOU WIN")
                break
            else:
                sleep(0.5)
                print(f"\nTotal is {total} but goal number is {goal}")
#--------------------------------------------------

# Lanch game--------------------------------------
if __name__ == "__main__":
    game()