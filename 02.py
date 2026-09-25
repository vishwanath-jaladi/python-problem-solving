# Program: Find the Largest Number
# Description: Finds the largest number among the numbers entered by the user.

n=int(input("ENter n value:"))
largest=int(input("Enter no 1:"))
for i in range(2,n+1):
    number=int(input(f"Enter no {i}:"))
    if largest<number:
        largest=number
print("Largest:", largest)