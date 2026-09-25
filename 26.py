# Program: Move Last Element to Front
# Description: This program creates a new list by moving the last element
# of the original list to the beginning.

numbers = [10, 20, 30, 40]
new_list=[]

new_list.append(numbers[len(numbers)-1])
    
for i in range(len(numbers)-1):
    new_list.append(numbers[i])

print(new_list)


