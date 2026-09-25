# Program: Find All Occurrences of a Number
# Description: This program uses a function to find and return all indexes
# where a given target number occurs in a list.

numbers = [10, 7, 25, 7, 40, 7, 25]
def find_number(numbers, target):
    index=[]
    for i in range(len(numbers)):
        if numbers[i]==target:
             index.append(i)
    return index
print(find_number(numbers,25))

