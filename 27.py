# Program: Find Missing Numbers in a Range
# Description: This program finds the smallest and largest values
# in a list and prints the numbers missing between them.
numbers = [15, 12, 16, 11, 13]

smallest = numbers[0]
largest = numbers[0]
for current_no in numbers:
    if current_no<smallest:
        smallest=current_no
    if current_no>largest:
        largest=current_no
for i in range(smallest,largest):
    if i not in numbers:
        print(i)