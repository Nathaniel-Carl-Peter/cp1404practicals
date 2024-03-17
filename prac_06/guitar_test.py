from prac_06.guitar import Guitar


def test():
    """Guitar test program"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", )
    print(guitar)

    print(f"My guitar: {name}, first made in {year} ${cost}")


test()

"""
Gibson L-5 CES get_age() - Expected 100. Got 100
Another Guitar get_age() - Expected 9. Got 9
Gibson L-5 CES is_vintage() - Expected True. Got True
Another Guitar is_vintage() - Expected False. Got False
"""
