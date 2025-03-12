# Add a function that returns the numbers that have duplicates
def duplicates(numbers):
    x = []
    return [i for i in numbers if numbers.count(i) > 1 and i not in x]
# Add an input variable that asks for 10 numbers
numbers = list(map(int, input("Enter 10 numbers seperated by space: ").split()))

#  Add the print statement that displays the numbers
print("the duplicates are ", duplicates(numbers))

"""
x = []
numbers = [int(input("input the number "+ str(i+1)+ ":" ))for i in range(10)]
for i in numbers:
    if numbers.count(i) > 1 and i not in x:
        x.append(i)
    
    
print(f"the duplicates are {x}")
"""        