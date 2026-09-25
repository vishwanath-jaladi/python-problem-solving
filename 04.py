# Program: Count Even and Odd Numbers
# Description: Counts the number of even and odd values entered by the user.

n=int(input("Enter n value:"))
even=0
odd=0
for i in range(n):
    number=int(input(f"Enter no {i+1}:"))
    if number%2==0:
        even+=1
    else:
        odd+=1
print(f"Total even numbers: {even}")
print(f"Total odd numbers: {odd}")