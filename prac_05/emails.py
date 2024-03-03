"""
CP1404 - Prac 05- Emails
Date: 03/02/2024
Nathaniel Carl Peter
"""

"""
Pseudo:

def main
    email_to_names = {}
    get email
    while email != ""
        get name from email
        get confirmation
        if confirmation != Y and confirmation != ""
            get name
        add email and name to list
        get email
    for name, email in email to names:
        print email and names


"""


# Write a program that stores users' emails (unique keys) and names (values) in a dictionary.
# Ask the user for their email until they enter a blank one.
# Use a separate function to extract a name from the email as in the example below.
# You should find the following methods useful: split, join, title

def main():
    """Main Email Program"""
    email_to_names = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n): ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ").title()
        email_to_names[email] = name
        email = input("Email: ")
    for email, name in email_to_names.items():
        print(f"{name}: ({email})")


def get_name_from_email(email):
    """Get name from Email"""
    prefix = email.split('@')[0]
    # print(prefix) # Check output of prefix
    parts = prefix.split('.')
    # print(parts) # Check output of parts
    name = " ".join(parts).title()
    # print(name) # Check output for name
    return name


main()
