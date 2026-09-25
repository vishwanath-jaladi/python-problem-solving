# Program: Find Missing Number
# Description: This program searches for a missing number in a sequence
# by checking which number is not present in the list.

numbers=[1, 2, 3, 6, 5]
for i in range(1,len(numbers)+2):
    if i not in numbers:
        print(i)

