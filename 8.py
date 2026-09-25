# Program: Count Numbers Above Average
# Description: Calculates the average of numbers and counts how many
# numbers are greater than the average.
n=int(input("Enter n value:"))
no=[]
count=0
for i in range(n):
    no.append(int(input(f"Enter no {i+1}:")))
average=sum(no)/n
for i in range(n):
    if average<no[i]:
        count+=1
print("average",average)
print("count",count)