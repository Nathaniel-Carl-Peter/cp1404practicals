"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    ValueError occurs if the user input is not a valid number (example: instead of number, it's a letter instead)
2. When will a ZeroDivisionError occur?
    If user input is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Another version of the code to avoid a ZeroDivisionError

numerator = int(input("Enter the numerator: "))
while numerator == 0:
    print("Invalid numerator")
    numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
while denominator == 0 and numerator == 0:
    print("Invalid denominator")
    denominator = int(input("Enter the denominator: "))
fraction = numerator / denominator
print(fraction)
