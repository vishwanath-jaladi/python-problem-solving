# Program: Find Sum of Even Numbers
# Description: This program uses a function to find and calculate
# the sum of all even numbers in a list.

numbers = [10, 7, 4, 9, 12, 5]
def find_sum_of_even(numbers):
    total=0
    for number in numbers:
        if number%2==0:
            total+=number
    return total
print("Even Sum:",find_sum_of_even(numbers))
