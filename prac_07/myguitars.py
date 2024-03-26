FILENAME = 'guitars.csv'
import csv
from guitar import Guitar


def load_file(filename):
    guitars = []
    in_file = open(filename, "r")
    for line in in_file:
        parts = line.strip().split(',')
        year = int(parts[1])
        cost = float(parts[2])
        guitar_added = Guitar(parts[0], year, cost)
        guitars.append(guitar_added, )
        # guitars.append(line.strip())
        # print(line.strip(), end=", ")
        # print(guitars)
    print()
    in_file.close()
    return guitars


def main():
    """Guitar client program"""
    guitars = load_file(FILENAME)
    print("My guitars!")
    name = input("Enter name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add, )
        print(f"{guitar_to_add}, added")
        name = input("Name: ")

    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))

    if guitars:
        print("These are my guitars")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars")


if __name__ == '__main__':
    main()
    # load_file(FILENAME)
