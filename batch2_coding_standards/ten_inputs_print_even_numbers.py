#Add a function that sums up the number of even numbers
def even(numbers):
    return(sum(1 for i in numbers if i % 2 == 0))
#Add an input variable for the 10 numbers
numbers =[int(input("input number"+str(i+1)+":"))for i in range(10)]
#print statement for the results
print("the number of even numbers are", even(numbers))