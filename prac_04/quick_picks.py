"""
CP1404 - Prac 04 - Quick Picks
Date: 25/02/2024
"""
import random

MAX = 45
MINIMUM = 1
NUMBER_OF_LINES = 6


def main():
    """Quick number pick program"""
    quick_picks = []
    number_of_quick_numbers = int(input("How many quick picks? "))
    print_random_numbers(number_of_quick_numbers, quick_picks)


def print_random_numbers(number_of_quick_numbers, quick_picks):
    while number_of_quick_numbers < 0:
        print("Invalid")
        number_of_quick_numbers = int(input("How many quick picks? "))
    for i in range(number_of_quick_numbers):
        for j in range(NUMBER_OF_LINES):
            number = random.randint(MINIMUM, MAX)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAX)
            quick_picks.append(number)
        quick_picks.sort()
    print(" ".join(f"{number:2}" for number in quick_picks))


main()
