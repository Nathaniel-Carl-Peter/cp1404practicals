"""
CP1404 - Prac 04

Ask the user for their username. If the username is in the above list of authorised users,
print "Access granted", otherwise print "Access denied".
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input(f"Enter name: ")
while username not in usernames:
    print("Access denied")
    username = input(f"Enter name: ")
print("Access granted")
