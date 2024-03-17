CURRENT_YEAR = 2013
VINTAGE = 50


class Guitar:
    """Represent a Car object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Output as a str"""
        return f"Guitar: {self.name} ({self.year}), worth ${self.cost}"

    """Guitar 1:       Gibson L-5 CES (1922), worth $ 16,035.40 (vintage)"""

    def get_age(self):
        """Get age of guitar"""
        return CURRENT_YEAR - self.year

    def vintage(self):
        """Indentify if guitar is vintage"""
        return self.get_age() >= CURRENT_YEAR
