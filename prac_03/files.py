OUTPUT_NAME_FILE = "name.txt"
OUTPUT_NUMBERS = "numbers.txt"

name = input("Enter name: ").title()
out_file = open(OUTPUT_NAME_FILE, "w")
print(name, file=out_file)
out_file.close()

# (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as above)
# then prints,"Your name is Bob" (or whatever the name is in the file).
name = input("Enter name: ").title()
out_file = open(OUTPUT_NAME_FILE, "w")
print(f"Your name is {name}", file=out_file)
out_file.close()
print(f"Your name is {name}")

# Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:

out_file = open(OUTPUT_NUMBERS, "w")
user_number1 = int(input(">>> "))
user_number2 = int(input(">>> "))
result = user_number1 + user_number2
print(result, file=out_file)
out_file.close()

# Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers.

total = 0
in_file = open(OUTPUT_NUMBERS, "r")
for line in in_file:
    user_number = int(line)
    total += 1
in_file.close()
print(total)
