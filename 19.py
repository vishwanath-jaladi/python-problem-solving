# Program: Student Pass/Fail Analysis
# Description: This program calculates the average marks and counts
# the number of students who passed and failed using a function.

marks = [35, 71, 55, 90, 28]
def student_result(marks):
    pass_count=0
    fail_count=0
    average_marks=sum(marks)/len(marks)
    for i in marks:
        if i>=40:
            pass_count+=1
        else:
            fail_count+=1
    return average_marks,pass_count,fail_count
average,pass_count,fail_count=student_result(marks)
print("Average:", average,"\nPassed:",pass_count,"\nFailed",fail_count)

