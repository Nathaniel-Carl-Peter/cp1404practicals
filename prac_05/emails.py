"""
CP1404 - Prac 05- Emails
Date: 03/02/2024
Nathaniel Carl Peter
"""

"""
Pseudo:

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
    # print(prefix)
    parts = prefix.split('.')
    # print(parts)
    name = " ".join(parts).title()
    # print(name)
    return name


main()
"""
Output:

Email: lindsay.ward@jcu.edu.au
Is your name Lindsay Ward? (Y/n)
Email: abe@gmail.com
Is your name Abe? (Y/n) y
Email: jimbo546@hotmail.com
Is your name Jimbo546? (Y/n) no
Name: Jim Boh
Email: 

Lindsay Ward (lindsay.ward@jcu.edu.au)
Abe (Abe@gmail.com)
Jim Boh (jimbo546@hotmail.com)
"""
