# Program: Search for a Number
# Description: Searches for a given number in a list and reports
# whether the number is found.
n=int(input("Enter n value:"))
no=[]

for i in range(n):
    no.append(int(input(f"Enter no {i+1}:")))
find=int(input("Enter the no to be find:"))
found=False
for i in range(n):
        if no[i]==find:
            found=True
            break
        
if found==True:
     print("Found")
else:
     print("Not Found")