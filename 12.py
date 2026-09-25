# Program: Dictionary Update
# Description: Creates a student dictionary, adds a new key,
# updates existing values, and displays the dictionary keys.
student={ "name":"vj",
          "age":19,
          "branch":"aiml",
          "marks":8.45}
student["city"]="Kalaburagi"
student["age"]=20
student["marks"]=9.1
for i in student:
    print(i)









#numbers = [2, 4, 5, 7]
#def square_numbers(numbers):
#    new_list=[]
#    for i in numbers:
#        new_list.append(i*i)
#    return new_list
#print(square_numbers(numbers))
#numbers = [-4, 2, 7, -8, 10, 3, 0, 6]
#def count_positive_even(numbers):
#    count=0
#    for number in numbers:
#        if number%2==0 and number>=0:
#            count+=1
#    return count
#print("Positive even count:",count_positive_even(numbers))
