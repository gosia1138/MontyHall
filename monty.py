#!/usr/bin/env python3
import random
from asciiart import DOOR_ART


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
        uc = input("\nWhich door do you want to open? Enter 1, 2 or 3: ")
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
Choose the door and take home the prize behind it!""")
    print(DOOR_ART["all_closed"])
    doors = prepare_doors(door_count)
    first_choice = users_choice(door_count)
    alternatives = list(doors.keys())
    alternatives.remove(first_choice)
    # Finds the other door with goat behind to present to the player and gets
    # the car door number to use in the final reveal.
    goat_doors = []
    car_door = -1
    for k, v in doors.items():
        if v == "car":
            car_door = k
        if k == first_choice:
            continue
        else:
            goat_doors.append(k)
    goat_door = random.choice(goat_doors)
    alternatives.remove(goat_door)
    alt_door = alternatives[0]
    print("\nYour choice: door number {}".format(first_choice))
    print("\nWhat if I told you that there is a goat behind door number {}?".format(
        str(goat_door)))
    print(DOOR_ART["goat{}".format(goat_door)])
    print("Do you want to stick with door number {} or prefer to swap for door number {}?".format(
        str(first_choice), str(alt_door)))
    # Player can now choose to open the other remaining door or to stick with
    # their original choice of door
    while True:
        final_choice = input("Do you want to swap? (y/n)")
        if final_choice in ['y', 'Y']:
            final_choice = alt_door
            break
        if final_choice in ['n', 'N']:
            final_choice = first_choice
            break
    # Revealing the players prize
    if doors[final_choice] == "car":
        print(DOOR_ART["car{}".format(car_door)])
        print("\nCongratulations! You just won a car!")
    else:
        print(DOOR_ART["car{}".format(car_door)])
        print("\nCongratulations! You just won a goat!")


if __name__ == "__main__":
    door_count = 3
    main(door_count)
