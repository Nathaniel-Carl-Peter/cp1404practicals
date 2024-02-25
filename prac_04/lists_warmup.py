numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])  # 3
print(numbers[-2])  # 9
print(numbers[3])  # 1
print(numbers[:1])  # [3]
print(5 in numbers)  # True
print(7 in numbers)  # False
print("3" in numbers)  # False
print(numbers + [6, 5, 3])  # 40 [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[-1] = "ten"
# Change the last element of numbers to 1
numbers[6] = 1
# Print all the elements from numbers except the first two (slice)
print(numbers[2:])
# Print whether 9 is an element of numbers
# True
