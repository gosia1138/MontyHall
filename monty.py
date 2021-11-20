#!/usr/bin/env python3
import random
from asciiart import DOOR_ART


def play_game():
    print(DOOR_ART["all_closed"])
    # generate car door
    car_door = str(random.randint(1, 3))

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
        decision = input("Do you want to swap? (y/n)").lower()
        if decision == "y":
            final_choice = alt_door
            break
        if decision == "n":
            final_choice = first_choice
            break

    # Revealing the prize
    print(DOOR_ART["car{}".format(car_door)])
    if final_choice == car_door:
        print("\nCongratulations! You just won a car!")
        return "car", decision
    else:
        print("\nCongratulations! You just won a goat!")
        return "goat", decision


def simulate_game(mode):
    car_door = str(random.randint(1, 3))
    first_choice = str(random.randint(1, 3))  # simulate user choosing door
    while True:  # find door with a goat to present to user
        goat_door = str(random.randint(1, 3))
        if goat_door != car_door and goat_door != first_choice:
            break
    alt_door = str(6 - int(goat_door) - int(first_choice))  # swap door

    # swapping or sticking to the first choice depending on mode
    if mode == "swap":
        final_choice = alt_door
    else:
        final_choice = first_choice

    # Revealing the prize
    if final_choice == car_door:
        return "car"
    else:
        return "goat"


def results(results_swap, results_stick):
    # results when swapping:
    swap_goats = results_swap.count("goat")
    swap_cars = results_swap.count("car")
    print("Swapping:")
    print("{:<6} {:<3} {}".format("Cars", swap_cars, "|" * swap_cars))
    print("{:<6} {:<3} {}".format("Goats", swap_goats, "|" * swap_goats))
    # results when not swapping:
    stick_goats = results_stick.count("goat")
    stick_cars = results_stick.count("car")
    print("Not swapping:")
    print("{:<6} {:<3} {}".format("Cars", stick_cars, "|" * stick_cars))
    print("{:<6} {:<3} {}".format("Goats", stick_goats, "|" * stick_goats))


def main():
    # Greet user and explain rules of the game
    print(DOOR_ART["welcome"])

    print("Would you like to (p)lay or (s)imulate 100 games")
    while True:  # user can choose to play manually or make a simulation
        mode = input("> ").lower()
        if mode == "p" or mode == "s":
            break

    results_swap = []
    results_stick = []

    if mode == "p":  # user playing manualy until q is pressed
        while True:
            prize, swap = play_game()
            if swap == "y":
                results_swap.append(prize)
            else:
                results_stick.append(prize)
            results(results_swap, results_stick)
            whats_next = input("Press Enter to play again or type q to quit ")
            if whats_next == "q":
                break

    else:  # running 100 simualtions for each case
        for i in range(100):
            prize = simulate_game("swap")
            results_swap.append(prize)
        for i in range(100):
            prize = simulate_game("stick")
            results_stick.append(prize)
        results(results_swap, results_stick)


if __name__ == "__main__":
    main()
