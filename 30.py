
# Program: Find Duplicate Numbers
# Description: This program finds the duplicate numbers in a list
# and stores each repeated number only once.

numbers =  [4, 7, 2, 7, 9, 4, 7]
seen=[]
repeat=[]
for i  in numbers:
    if i not in seen:
        seen.append(i)
    else :
        if i in repeat:
            pass
        else:
            repeat.append(i)
print(seen)
print(repeat)
