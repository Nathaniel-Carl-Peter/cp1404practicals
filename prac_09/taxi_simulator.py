from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Main program"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print('Lets drive!')
    print_menu()
    choice = input('>>> ').lower()
    while choice != 'q':
        if choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = get_valid_float_number('Drive how far? ')
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print('Invalid input')
        print(f'Bill to date: {total_bill:.2f}')
        print_menu()
        choice = input('>>> ').lower()
    print(f'Total bill: ${total_bill:.2f}')
    print('Taxis are now: ')
    display_taxis(taxis)
    print('Finished')


def choose_taxi(taxis):
    display_taxis(taxis)
    taxi_choice = get_valid_number('Choose taxi: ')
    try:
        current_taxi = taxis[taxi_choice]
    except IndexError:
        print('Invalid input: Choice not in list')
    return current_taxi


def print_menu():
    """Print menu"""
    print("q)uit, c)hoose taxi, d)rive")


def display_taxis(taxis):
    """Prints taxis in list"""
    print('Taxis available:')
    for i, taxi in enumerate(taxis):
        print(f'{i:2} - {taxi}')


def get_valid_float_number(prompt):
    """Get valid number input"""
    valid_input = False
    while not valid_input:
        try:
            number = float(input(prompt))
            if number < 0:
                print("Number must be >= 0")
            else:
                return number
        except ValueError:
            print("Invalid input; enter a valid number")


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


def run_tests():
    """Run tests to show workings of Car and Taxi classes."""
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus.odometer)
    print(bus)

    # drive bus (input/loop is oblivious to fuel)
    distance = int(input("Drive how far? "))
    while distance > 0:
        distance_travelled = bus.drive(distance)
        print(f"{bus} travelled {distance_travelled}")
        distance = int(input("Drive how far? "))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


if __name__ == '__main__':
    # main()
    # display_taxis()
    run_tests()
