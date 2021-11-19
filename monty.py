#!/usr/bin/env python3
import random


def prepare_doors(door_count):
    """Build up the doors, herd the goats, hide the car"""
    car_door = random.randint(1, door_count)
    doors = {}
    for door in range(1, door_count + 1):
        if door == car_door:
            doors[door] = "car"
        else:
            doors[door] = "goat"
    return doors


def users_choice(door_count):
    """gathers users input and checks if valid"""
    uc = 0
    while True:
        uc = input("Which door do you want to open? Enter 1, 2 or 3: ")
        if uc.isnumeric():
            if int(uc) <= door_count:
                return int(uc)
            else:
                print("Thats more than there is doors!")
        elif not uc.isnumeric():
            print("Oh cmon, that is not even a number!")


def main(door_count):
    print("""
Welcome to the Monty Hall Simulator!

You are presented with three doors.
Behind two of them are goats, but behind one of them is a car!
Choose the door and take home the prize behind it!
 ___   ___   ___
|   | |   | |   |
| 1 | | 2 | | 3 |
|___| |___| |___|
    """)

    doors = prepare_doors(door_count)
    first_choice = users_choice(door_count)
    alternatives = list(doors.keys())
    alternatives.remove(first_choice)
    # Finds the other door with goat behind to present to the player
    goat_doors = []
    for k, v in doors.items():
        if k == first_choice or v == "car":
            continue
        else:
            goat_doors.append(k)
    goat_door = random.choice(goat_doors)
    alternatives.remove(goat_door)
    alt_door = alternatives[0]
    print("You have chosen door number {}".format(first_choice))
    print("What if I told you that there is a goat behind dooe number {}?".format(
        str(goat_door)))
    print("Do you want to stick with door number {} or prefer to switch to door number {}?".format(
        str(first_choice), str(alt_door)))
    # Player can now choose to open the other remaining door or to stick with
    # their original choice of door
    while True:
        final_choice = input("Enter the door number: ")
        if final_choice.isnumeric():
            final_choice = int(final_choice)
            if final_choice in (first_choice, alt_door):
                break
        else:
            print("You can only choose between door number {} or {}".format(
                str(first_choice), str(alt_door)))
    # Revealing the players prize
    if doors[final_choice] == "car":
        print("Congratulations! You just won a car!")
    else:
        print("Congratulations! You just won a goat!")


if __name__ == "__main__":
    door_count = 3
    main(door_count)
