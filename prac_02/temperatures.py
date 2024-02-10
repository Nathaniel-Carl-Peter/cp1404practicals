"""
CP1404/CP5632 - Practical 02 - temperature conversion

Pseudocode:

def main
    display menu
    get choice
    while choice not Q
        if choice = C
            get ceclcius
            fahrenheit = celsius * 9.0 / 5 + 32
            display fahrenheit
        else if choice = F
            get fahrenheit
            celsius = 5 / 9 * (fahrenheit - 32)
            display celcius
        else
            invalid option
        get choice
    quit
"""
# Use 2 functions (NOT one!) for converting Celsius to Fahrenheit and vice versa.
# Important: Remember SRP - functions should do one thing, so these should be simple calculation functions.
# Do not get user input or print output in the functions - do those things outside.

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Convert temparatures"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_celsius_to_fahrenheit()
        elif choice == "F":
            convert_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius():
    """Convert fahrenheit to celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} F")


def convert_celsius_to_fahrenheit():
    """Convert celsius to fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()
