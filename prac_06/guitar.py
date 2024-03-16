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

    def vintage(self):
        if self.year > 50:
            return "vintage"
        else:
            return ""

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance
