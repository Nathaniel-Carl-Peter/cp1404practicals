"""
CP1404 - Programming 2
Date: 10/02/2024
"""

# (G)et a valid score (must be 0-100 inclusive)
# (P)rint result (copy or import your function to determine the result from score.py)
# (S)how stars (this should print as many stars as the score)
# (Q)uit

MENU = "(V)alid score\n (S)tars\n (Q)uit"


def main():
    """Main score program"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "V":
            score = float(input("Enter grade: "))
            print(define_grade(score))
        elif choice == "S":
            user_number = int(input(f"Enter number: "))
            while len(user_number) < score:
                print("Too low")
                user_number = int(input(f"Enter number: "))
            print("*" * len(user_number))
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


def define_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
