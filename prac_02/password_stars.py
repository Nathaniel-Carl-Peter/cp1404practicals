"""
CP1404 - Prac02 - Password Stars
Date: 09/02/24
"""

"""
get user password
display *
"""

# Version 1
MINIMUM_LENGTH = 4

user_password = input(f"Enter password with the minimum characters of {MINIMUM_LENGTH}: ")
while len(user_password) < MINIMUM_LENGTH:
    print("Invalid password")
    user_password = input(f"Enter password with the minimum characters of {MINIMUM_LENGTH}: ")
print("*" * len(user_password))
