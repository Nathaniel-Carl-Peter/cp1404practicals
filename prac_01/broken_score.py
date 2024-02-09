"""
CP1404/CP5632 - Practical
Date: 02/02/2024
Author: Nathaniel Carl Peter
Broken program to determine score status
Rewrite the following program using the most efficient if, elif, else structure you can.
"""

# https://peps.python.org/pep-0020/
# Check Indenting.
# Flat is better than nested quote from "The Zen of Python".
# Use less if, elif conditions.
# Check boundary conditions (E.g. Rather than > 50, use >= 50 since score of 50 is considered passable)
# Use less if/elsif condition

"""
Pseudo:
get_score
if score < 0 or > 100:
    display Invalid score
else if score >= 90:
    display Excellent
else if score >= 50:
    display Passable
else
    display Bad
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
