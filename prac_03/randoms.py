import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
print(random.uniform(1, 101))

# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?
# smallest = 5
# largest = 17

# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# smallest = 3 and largest = 9
# Could line 2 have produced a 4?
# Line 2 cannot produce a line just to the step of 2: example 3 + 2 = 5
#  if it were a for loop the output would be: 3, 5, 7, 9

# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# smallest = 3.6902717807420067 and largest = 100.59739705486234
#
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
