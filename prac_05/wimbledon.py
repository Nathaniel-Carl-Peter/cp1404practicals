"""
CP1404 - Prac05 - Module 5
Wimbledon
Date: 02/02/2024
Author: Nathaniel Carl Peter
"""
import csv

# Write a program to read this file, process the data and display processed information.
# the champions and how many times they have won.
# the countries of the champions in alphabetical order


FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Main program for Wimbledon records"""
    data = load_data(FILENAME)
    champion_count, countries = process_data(data)
    print_data(champion_count, countries)


def process_data(data):
    """Create dictionary for countries and championships"""
    champion_count = {}
    countries = set()
    for record in data:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_count[record[INDEX_CHAMPION]] = 1
    return champion_count, countries


def load_data(filename):
    """Load data from CSV file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove Header
        for line in in_file:
            # print(line) # Check output
            parts = line.strip().split(',')
            # print(parts) # Check output
            records.append(parts)
    return records


def print_data(champion_count, countries):
    print("Wimbledon Champion records: ")
    for name, count in champion_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
