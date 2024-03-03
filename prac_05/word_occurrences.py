"""
CP1404 - Prac05 - Word Occurencies
Date: 03/03/2024
"""
# Write a program to count the occurrences of words in a string.
# The program should ask the user for a string, then print the counts of how many of each word are in the string.
word_count = {}

text = input("Text: ")
words = text.split()
for word in words:
    frequency = word_count.get(word, 0)
    word_count[word] = frequency + 1

words = list(word_count.keys())
words.sort()

max_length = max(len(word) for word in words)
for word in words:
    # print(f"{len(words)}")
    # print(word)
    print(f"{word:{max_length}}: {word_count[word]}")
"""
Output:
Text: this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2
"""
