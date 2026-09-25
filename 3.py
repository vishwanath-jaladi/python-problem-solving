# Program: Find the Smallest Number
# Description: Finds the smallest number among the numbers entered by the user.
n=int(input("Enter n value:"))
smallest=int(input("Enter no 1:"))
for i in range(2,n+1):
    number=int(input(f"Enter no {i}:"))
    if smallest>number:
        smallest=number
print("Smallest:", smallest)