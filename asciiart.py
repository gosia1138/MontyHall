'''This ASCII art was created by Al Sweigart as part of his MontyHall
python script.
https://nostarch.com/big-book-small-python-projects'''

WELCOME = """
Welcome to the Monty Hall Simulator!

You are presented with three doors.
Behind two of them are goats, but behind one of them is a car!
Choose the door and take home the prize behind it!"""

ALL_CLOSED = """
 +------+  +------+  +------+
 |      |  |      |  |      |
 |   1  |  |   2  |  |   3  |
 |      |  |      |  |      |
 |      |  |      |  |      |
 |      |  |      |  |      |
 +------+  +------+  +------+"""

FIRST_GOAT = """
 +------+  +------+  +------+
 |  ((  |  |      |  |      |
 |  oo  |  |   2  |  |   3  |
 | /_/|_|  |      |  |      |
 |    | |  |      |  |      |
 |GOAT|||  |      |  |      |
 +------+  +------+  +------+"""

SECOND_GOAT = """
 +------+  +------+  +------+
 |      |  |  ((  |  |      |
 |   1  |  |  oo  |  |   3  |
 |      |  | /_/|_|  |      |
 |      |  |    | |  |      |
 |      |  |GOAT|||  |      |
 +------+  +------+  +------+"""

THIRD_GOAT = """
 +------+  +------+  +------+
 |      |  |      |  |  ((  |
 |   1  |  |   2  |  |  oo  |
 |      |  |      |  | /_/|_|
 |      |  |      |  |    | |
 |      |  |      |  |GOAT|||
 +------+  +------+  +------+"""

FIRST_CAR_OTHERS_GOAT = """
 +------+  +------+  +------+
 | CAR! |  |  ((  |  |  ((  |
 |    __|  |  oo  |  |  oo  |
 |  _/  |  | /_/|_|  | /_/|_|
 | /_ __|  |    | |  |    | |
 |   O  |  |GOAT|||  |GOAT|||
 +------+  +------+  +------+"""

SECOND_CAR_OTHERS_GOAT = """
 +------+  +------+  +------+
 |  ((  |  | CAR! |  |  ((  |
 |  oo  |  |    __|  |  oo  |
 | /_/|_|  |  _/  |  | /_/|_|
 |    | |  | /_ __|  |    | |
 |GOAT|||  |   O  |  |GOAT|||
 +------+  +------+  +------+"""

THIRD_CAR_OTHERS_GOAT = """
 +------+  +------+  +------+
 |  ((  |  |  ((  |  | CAR! |
 |  oo  |  |  oo  |  |    __|
 | /_/|_|  | /_/|_|  |  _/  |
 |    | |  |    | |  | /_ __|
 |GOAT|||  |GOAT|||  |   O  |
 +------+  +------+  +------+"""


DOOR_ART = {
    "welcome": WELCOME,
    "all_closed": ALL_CLOSED,
    "goat1": FIRST_GOAT,
    "goat2": SECOND_GOAT,
    "goat3": THIRD_GOAT,
    "car1": FIRST_CAR_OTHERS_GOAT,
    "car2": SECOND_CAR_OTHERS_GOAT,
    "car3": THIRD_CAR_OTHERS_GOAT
}
