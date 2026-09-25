# Program: Rotate a List to the Right
# Description: This program uses a function to rotate the elements
# of a list to the right by a given number of positions.

numbers = [10, 20, 30, 40, 50]
k = 8
def rotate_right(numbers, k):
    new_list=[]
    
    k=(k%len(numbers))
    for i in range(k):
        new_list.append(numbers[len(numbers)-k+i])
    for i in range(len(numbers)-k):
        new_list.append(numbers[i])
    return new_list
print(rotate_right(numbers,k))

    