"""
Prac06
Guitars Main program
"""
from prac_06.guitar import Guitar

"""
Pseudo:

def main
    guitars = []
    get guitar name
    for guitar in guitars
    display guitars
"""


def main():
    """Guitar client program"""
    guitars = []
    print("My guitars!")
    name = input("Enter name: ").title()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add, )
        print(f"{guitar_to_add}, added")
        name = input("Name: ")

    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))

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

"""
Sample output:

My guitars!
Name: Fender Stratocaster
Year: 2014
Cost: $765.4
Fender Stratocaster (2014) : $765.40 added.

Name:

... snip ...

These are my guitars:
Guitar 1:       Gibson L-5 CES (1922), worth $ 16,035.40 (vintage)
Guitar 2:        Line 6 JTV-59 (2010), worth $  1,512.90
Guitar 3:  Fender Stratocaster (2014), worth $    765.40
"""
