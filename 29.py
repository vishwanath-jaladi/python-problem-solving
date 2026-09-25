# Program: Frequency Count of Numbers
# Description: This program uses a dictionary to count how many times
# each number occurs in a list.

numbers =  [4, 7, 2, 7, 9, 4, 7]
def frequency_count(numbers):    
    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number]+=1
        else:
            frequency[number]=1
        # your logic

    return frequency
print(frequency_count(numbers))