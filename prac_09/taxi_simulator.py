from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def print_menu():
    """Print menu"""
    print("q)uit, c)hoose taxi, d)rive")


def display_taxis():
    """Prints taxis in list"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print()
    print('Taxis Available:')
    for i, taxi in enumerate(taxis):
        print(f'{i:2} - {taxi}')


def main():
    """Main program"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print('Lets drive!')
    print_menu()
    choice = input().lower()
    while choice != 'q':
        if choice == 'c':
            print('c')
            display_taxis(taxis)
        elif choice == 'd':
            print('d')
        else:
            print('Invalid input')
        print_menu()
        choice = input().lower()
    print('Thanks')


def get_valid_number(prompt):
    """Get valid number input"""
    valid_input = False
    while not valid_input:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Number must be >= 0")
            else:
                return number
        except ValueError:
            print("Invalid input; enter a valid number")


def get_valid_text(prompt):
    """Get valid text input"""
    text = input(prompt).title()
    while not len(text):
        print("Input can not be blank")
        text = input(prompt).title()
    return text

if __name__ == '__main__':
    # main()
    display_taxis()