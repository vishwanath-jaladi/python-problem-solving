# Program: Analyze Numbers
# Description: This program uses a function to find the largest number,
# smallest number, and count of even numbers in a list.
nums = [12, 5, 8, 21, 4, 16]
def analyse_numbers(numbers):
    largest_no=numbers[0]
    smallest_no=numbers[0]
    count=0
    for i in numbers:
        if i>largest_no:
            largest_no=i
        if i<smallest_no:
            smallest_no=i
        if i%2==0:
            count+=1
    return largest_no,smallest_no,count
largest_no,smallest_no,even_count=analyse_numbers(nums)
print(" Largest No:",largest_no,"\n Smallest no:",smallest_no,"\n Even Count:",even_count)