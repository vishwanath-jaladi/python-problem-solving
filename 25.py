# Program: Custom List Rearrangement
# Description: This program creates a new list by rearranging elements
# of an existing list using index-based loops.

numbers = [10, 20, 30, 40]
new_list=[]
#new_list.append(numbers[len(numbers)-2])
for i in range(len(numbers)-2,0,-1):
    new_list.append(numbers[len(numbers)-i])
for i in range(len(numbers)-2):
    new_list.append(numbers[i])
print(new_list)
