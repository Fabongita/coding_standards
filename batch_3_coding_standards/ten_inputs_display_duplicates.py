# Add a function that returns the numbers that have duplicates
def duplicates(numbers):
    return [i for index, i in enumerate(numbers) if numbers.count(i) > 1 and i not in numbers[:index]]
# Add an input variable that asks for 10 numbers
numbers = list(map(int, input("Enter 10 numbers seperated by comma: ").split(",")))

#  Add the print statement that displays the numbers
print("the duplicates are ", duplicates(numbers))
