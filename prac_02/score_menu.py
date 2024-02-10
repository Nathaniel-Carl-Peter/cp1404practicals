"""
CP1404 - Programming 2 - Score Menu
Date: 10/02/2024
"""

# (G)et a valid score (must be 0-100 inclusive)
# (P)rint result (copy or import your function to determine the result from score.py)
# (S)how stars (this should print as many stars as the score)
# (Q)uit

MENU = "(V)alid score\n(S)tars\n(Q)uit"


def main():
    """Main score program"""
    print(MENU)
    choice = input(">>> ").upper()
    if choice == "V":
        # Determined score
        score = get_score()
        grade = define_grade(score)
        print(grade)
    if choice == "S":
        # Print number of stars
        user_number = get_valid_number()
        print_number_of_stars(user_number)
    else:
        print("Invalid choice")
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


def get_valid_number():
    """Get valid number"""
    user_number = int(input(f"Enter valid number: "))
    return user_number


def print_number_of_stars(user_number):
    """Print number of stars"""
    for i in range(user_number):
        print("*", end="")
    print()


def get_score():
    """Get score from the user"""
    score = float(input("Enter grade: "))
    return score


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


main()
