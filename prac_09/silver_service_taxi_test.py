"""Cp1404 Silver Taxi Service Test"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi testing"""
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)  # name, price_per_km, current_fare_distance
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())
    hummer = SilverServiceTaxi('Hummer', 200, 4)  # name, price_per_km, current_fare_distance
    hummer.drive(0)
    print(hummer)
    print(f'${hummer.get_fare():.2f}')


main()
