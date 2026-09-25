# Program: Sum Numbers Using Functions
# Description: This program takes multiple numbers from the user using
# a function and calculates their total using another function.

no=int(input("How many numbers:"))
numbers=[]
def get_numbers():
    for i in range(no):
        numbers.append(int(input(f"Enter nuber {i+1}:")))
    return numbers
def calculate_sum(numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum

print("Total:",calculate_sum(get_numbers()))