# Program: Rotate a List to the Left
# Description: This program uses a function to rotate the elements
# of a list to the left by a given number of positions.


numbers = [10, 20, 30, 40, 50]
k = 3
def rotate_left(numbers,k):
    new_list=[]
    k=k%len(numbers)
    for i in range(k,len(numbers)):
            new_list.append(numbers[i])
    for i in range(k):
        new_list.append(numbers[i])
    return new_list
print(rotate_left(numbers,k))
