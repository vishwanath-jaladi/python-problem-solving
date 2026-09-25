# Program: Count Even Numbers
# Description: This program uses a function to count the number
# of even values in a list.
list_no = [10, 7, 4, 9, 12, 6]
def count_even(numbers):
    count=0
    for i in numbers:
        if i %2==0:
            count+=1
    return count
print(count_even(list_no))
