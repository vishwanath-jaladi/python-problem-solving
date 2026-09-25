# Program: Second Largest Number
# Description: Finds the second-largest number from a list of numbers.
n=int(input("Enter n value:"))
no=[]
for i in range(n):
    no.append(int(input(f"Enter no {i+1}:")))
largest=no[0]
second_lar=no[1]
for number in no[2,]:
    if number>=largest:
            second_lar=largest
            largest=number
    elif number>=second_lar:
         second_lar=number
    else:
         continue

print(second_lar)
        