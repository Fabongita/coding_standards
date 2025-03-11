# Add a function that returns the numbers that have duplicates
def duplicates(numbers):
    return [x for i in numbers if i in numbers == True]
# Add an input variable that asks for 10 numbers
numbers = [int(input("input the number "+ str(i+1)+ ":" ))for i in range(10)]

#  Add the print statement that displays the numbers
print("the duplicates are ", duplicates(numbers))