"""
CP1404/CP5632 - Practical 02
Date: 10/02/2024
Author: Nathaniel Carl Peter
Socre function
"""

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
    """Get score from the user"""
    score = float(input("Enter grade: "))
    return score


main()
