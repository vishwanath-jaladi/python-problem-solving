# Program: Analyze a List
# Description: Finds the largest number, smallest number, average,
# and count of numbers above the average using a function.
numbers = [10, 20, 5, 40, 25]
def analyze_list(numbers):
    largest=numbers[0]
    smallest=numbers[0]
    no_above_avg=0
    average=sum(numbers)/len(numbers)
    for i in numbers:
        if i>largest:
            largest=i
        if i<smallest:
            smallest=i
        if i>average:
            no_above_avg+=1
    return largest,smallest,average,no_above_avg
largest,smallest,average,no_above_avg=analyze_list(numbers)
print("Largest:",largest,"\nSmallest:",smallest,"\nAverage:",average,"\nAbove average:",no_above_avg)