# Program: Student Result
# Description: Takes a student's marks in three subjects and calculates
# total marks, percentage, and pass/fail result.

marks_of_3=[]
name=input("Enter student name:")
for i in range(1,4):
    marks_of_3.append(int(input(f"Enter marks for subject{i} (out of 100):")))
total_marks=sum(marks_of_3) 
percentage=(total_marks/300 )*100
print(f"Student name{name}:")
print(f"total marks of {name} is:",total_marks,"(out of 300)")
print("Total percentage is:" , percentage)
if percentage>=40:
    print("Result: Pass")
else:
    print("Result:Fail")
