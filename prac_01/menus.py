"""
CP1404 - Prac01
Date: 02/02/2024
Author: Nathaniel Carl Peter
"""

"""

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

MENU = "Menu:\n(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice :P")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished. ;)")

