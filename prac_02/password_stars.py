"""
CP1404 - Prac02 - Password Stars
Date: 09/02/24
"""

"""
def main
    get user password
    display *
"""

MINIMUM_LENGTH = 4


def main():
    """Main Password Program"""
    user_password = get_password()
    print_stars(user_password)


def print_stars(user_password):
    """Print number *"""
    print("*" * len(user_password))


def get_password():
    """Get password with error checking"""
    user_password = input(f"Enter password with the minimum characters of {MINIMUM_LENGTH}: ")
    while len(user_password) < MINIMUM_LENGTH:
        print("Invalid password")
        user_password = input(f"Enter password with the minimum characters of {MINIMUM_LENGTH}: ")
    return user_password


main()
