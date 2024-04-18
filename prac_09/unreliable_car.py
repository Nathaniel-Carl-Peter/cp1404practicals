"""
CP1404 - Unreliable Car
"""

from car import Car
import random


class UnreliableCar(Car):
    """Unreliable Car class"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive to check the car's reliability"""
        random_number = random.randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
            # Continue with the regular driving logic
            distance_driven = super().drive(distance)
            # You can add any additional behavior specific to UnreliableCar here
            # (e.g., logging reliability failures, etc.)
            return distance_driven
