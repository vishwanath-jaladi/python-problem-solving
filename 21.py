# Program: First Non-Repeating Number
# Description: This program uses a dictionary to count the frequency
# of each number and finds the first number that occurs only once.


numbers = [4, 5, 1, 1, 4, 5,6]
def first_non_repeating(numbers):
    freq={}
    for i in numbers:
        if i in freq:
            freq[i]=freq[i]+1
        else:
            freq[i]=1
    for value,count in freq.items():
        if count==1:
            return (value)
    return 0
print(first_non_repeating(numbers))