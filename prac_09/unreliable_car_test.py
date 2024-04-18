"""
CP1404/CP5632 Practical
Unreliable car test
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Taxi testing"""
    # Cars with different state of reliability status
    nice_car = UnreliableCar('Good Car', 100, 85)
    shady_car = UnreliableCar('Sussy Car', 100, 8)

    # Attempt to drive car a number of times
    for i in range(1, 12):
        print(f'Drive {i}km')
        print(f"{nice_car.name:12} drove {nice_car.drive(i):2}km")
        print(f"{shady_car.name:12} drove {shady_car.drive(i):2}km")
    print()

    # Print state of cars
    print(nice_car)
    print(shady_car)


main()
