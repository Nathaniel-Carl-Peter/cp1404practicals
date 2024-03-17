from prac_06.guitar import Guitar


def test():
    """Guitar test program"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    print(guitar)


test()

"""
Output:

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
