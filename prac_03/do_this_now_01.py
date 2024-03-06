FILENAME = "teststar.txt"

# with method used
# with open(FILENAME, 'r') as in_file:
#     for line in in_file:
#         if line[0] == "#":
#             print(line)

# Without with method
in_file = open(FILENAME, 'r')
for line in in_file:
    if line[0] == "#":
        print(line)
in_file.close()
