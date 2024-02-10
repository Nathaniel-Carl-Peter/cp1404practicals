"""
CP1404 - Programming 2
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
    while choice != "Q":
        if choice == "V":
            score = get_score()
            grade = define_grade(score)
            print(grade)
        elif choice == "S":
            user_number = int(input(f"Enter valid number: "))
            while user_number < score:
                user_number = int(input(f"Enter valid number: "))
            print("*" * len(user_number))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


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
