from prac_06.guitar import Guitar


def test():
    """Guitar test program"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 1500)
    # print(guitar)
    print(f"{guitar.name} get_age() - Expected {95}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {9}. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")
    print(f"My guitar: {name}, first made in {year} ${cost}")


test()

"""
Gibson L-5 CES get_age() - Expected 100. Got 100
Another Guitar get_age() - Expected 9. Got 9
Gibson L-5 CES is_vintage() - Expected True. Got True
Another Guitar is_vintage() - Expected False. Got False
"""
