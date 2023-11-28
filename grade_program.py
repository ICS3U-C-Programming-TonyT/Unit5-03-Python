#!/usr/bin/env python3
# Created By: Tony Tran
# Date: November. 27, 2023
# This program will return you a percentage using you level.


import statistics


def calc_mark(level):
    grade_array = {
        "4+": statistics.median([95, 100]),
        "4": statistics.median([87, 94]),
        "4-": statistics.median([80, 86]),
        "3+": statistics.median([77, 79]),
        "3": statistics.median([73, 76]),
        "3-": statistics.median([70, 72]),
        "2+": statistics.median([67, 69]),
        "2": statistics.median([63, 66]),
        "2-": statistics.median([60, 62]),
        "1+": statistics.median([57, 59]),
        "1": statistics.median([53, 56]),
        "1-": statistics.median([50, 52]),
    }
    if level in grade_array:
        return grade_array[level]
    else:
        print(f"{level} is not a valid level.")


def main():
    print("Levels: 4+, 4, 4-, 3+, 3, 3-, 2+, 2, 2-, 1+, 1, 1-")
    user_level = input("Enter the level you want converted to a percentage: ")
    if user_level.lower() == "r":
        print(f"{user_level} has a middle percentage of 45%.")
    else:
        grade = calc_mark(user_level)
        print(f"Level {user_level} has a middle percentage of {grade}%")


if __name__ == "__main__":
    main()
