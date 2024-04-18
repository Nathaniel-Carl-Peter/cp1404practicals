"""
Cp1404 - SilverServiceTaxi Class -
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise attributes of SilverTaxi"""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        """Output as string"""
        return f'{super().__str__()} plus flagfall ${self.flagfall:.2f}'

    def get_fare(self):
        """Get fare"""
        return self.flagfall + super().get_fare()

# Add a new attribute, fanciness, which is a float that scales (multiplies) the price_per_km. Pass the fanciness value into the constructor and multiply self.price_per_km by it.
# Note that here we can get the initial base price using Taxi.price_per_km, then customise our object's instance variable, self.price_per_km. So, if the class variable (for all taxis) goes up, the price change is inherited by all SilverServiceTaxis.
# If you're not sure about this, please ask! Don't go on without "getting it".
#
# SilverServiceTaxi also has an extra charge for each new fare, so add a flagfall class variable set to 4.50.
#
# Add or override whatever method you need to (think about it...) in order to calculate the fare.
#
# Write a __str__ method so that you can add the flagfall to the end. E.g., for a Hummer with a fanciness of 4, it should display like:
