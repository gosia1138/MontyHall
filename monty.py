#!/usr/bin/env python3
import random
from asciiart import DOOR_ART


def main():
    print("""
Welcome to the Monty Hall Simulator!

You are presented with three doors.
Behind two of them are goats, but behind one of them is a car!
Choose the door and take home the prize behind it!""")
    print(DOOR_ART["all_closed"])

    # generate car door
    car_door = random.randint(1, 3)

    while True:  # prompt user for door number
        print("Please choose door number 1, 2 or 3:")
        first_choice = input("> ")
        if first_choice == "1" or first_choice == "2" or first_choice == "3":
            break

    while True:  # find door with a goat to present to user
        goat_door = str(random.randint(1, 3))
        if goat_door != car_door and goat_door != first_choice:
            break

    alt_door = str(6 - int(goat_door) - int(first_choice))  # swap door

    # Presenting goat door and prompting user if want to swap
    print("\nWhat if I told you that there is a goat behind door number {}?".format(
        str(goat_door)))
    print(DOOR_ART["goat{}".format(goat_door)])
    print("Do you still want to open door number {} or swap for door number {}?".format(
        str(first_choice), str(alt_door)))

    while True:  # users choice to swap or stick
        decision = input("Do you want to swap? (y/n)")
        if decision in ['y', 'Y']:
            final_choice = alt_door
            break
        if final_choice in ['n', 'N']:
            final_choice = first_choice
            break

    # Revealing the prize
    if final_choice == car_door:
        print(DOOR_ART["car{}".format(car_door)])
        print("\nCongratulations! You just won a car!")
    else:
        print(DOOR_ART["car{}".format(car_door)])
        print("\nCongratulations! You just won a goat!")


if __name__ == "__main__":
    main()
