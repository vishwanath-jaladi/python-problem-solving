# Program: Student Marks Report
# Description: Calculates the total, average, highest marks, lowest marks,
# and number of passed and failed students.
no=int(input("Enter no of students:"))
marks=[]
pass_count=0
fail_count=0
for i in range(no):
    marks.append(int(input(f"Enter marks for student {i+1}:")))
total_makas=sum(marks)
average_marks=total_makas/no
highest_marks=marks[0]
for i in range(1,no):
    if marks[i]>highest_marks:
        highest_marks=marks[i]
lowest_marks=marks[0]
for i in range(1,no):
    if marks[i]<lowest_marks:
        lowest_marks=marks[i]
for mark in marks:
    if mark>=40:
        pass_count+=1
    else:
        fail_count+=1
print("-----------Students Report-----------")
print("Total Marks:", total_makas)
print("Average Marks:", round(average_marks))
print("Highest Maarks:",highest_marks)
print("Lowest marks:",lowest_marks)
print("Number of students who passed:", pass_count)
print("Number of students who failed:",fail_count)
               
