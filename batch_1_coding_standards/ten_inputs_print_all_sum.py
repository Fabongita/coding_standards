#Define a function that returns the sum of all ten inputs
def summation(numbers):
    return sum(numbers)
#Use list comprehension to input 10 the 10 numbers
numbers = [int(input("input number " + str(i + 1) + " times: ")) for i in range(10)]
#Use a print statement to show the result
print("the sum of the 10 numbers is", summation(numbers))
