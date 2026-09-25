# Program: Move Zeros to the End
# Description: This program uses a function to move all zero values
# to the end of a list while keeping the non-zero values in their
# original order.
numbers = [0, 1, 0, 3, 12]
def move_zeros(numbers):
    new_list=[]
    for number in numbers:
        if number!=0:
            new_list.append(number)
    for number in numbers:
        if number==0:
            new_list.append(number)
    return new_list
print(move_zeros(numbers))
