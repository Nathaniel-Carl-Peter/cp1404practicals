from taxi import Taxi


def test():
    """Taxi class test"""
    my_taxi = Taxi('Prius 1', 100, 1.23)
    my_taxi.drive(40)
    my_taxi.current_fare_distance()
    print()


test()

# Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
# Drive the taxi 40 km
# Print the taxi's details and the current fare
# Restart the meter (start a new fare) and then drive the car 100 km
# Print the details and the current fare
