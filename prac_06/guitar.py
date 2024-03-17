"""
CP1404 - Guitar Class
"""

CURRENT_YEAR = 2013
VINTAGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Output as a string"""
        return f"Guitar: {self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Get age of guitar based on 2013"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Identify if guitar is vintage"""
        return self.get_age() >= VINTAGE
