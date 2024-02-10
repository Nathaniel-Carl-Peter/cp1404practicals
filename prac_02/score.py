"""
CP1404/CP5632 - Practical
Date: 10/02/2024
Author: Nathaniel Carl Peter
Socre function
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


# Your main function should ask the user for their score and print the result.
# Write a new function that takes in the user's score as a parameter and returns the result to be printed.
# Follow SRP: The function should not print it.
#
# Now add a new part to the bottom of your main function that generates a random score and prints the result.
# You do NOT need to write a different function to determine the result for the random score.
# If you've written your new function properly, you can use it.
# If you've breached SRP, then you'll see that you can't.

def main():
    """Main score program"""
    score = get_score()
    grade = define_grade(score)
    print(grade)


def define_grade(score):
    """Determine grade"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_score():
    score = float(input("Enter grade: "))
    return score


main()
