# Add a function that returns the numbers that have duplicates
def duplicates(numbers):
    return [i for index, i in enumerate(numbers) if numbers.count(i) > 1 and i not in numbers[:index]]
# Add an input variable that asks for 10 numbers
numbers = [int(input(f"input numbers {i+1} times : "))for i in range(10)]

#  Add the print statement that displays the numbers
print("the duplicates are ", duplicates(numbers))
